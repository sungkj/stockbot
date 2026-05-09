import os
import asyncio
import aiohttp
from utils.logger import setup_logger

logger = setup_logger(__name__)

class KiwoomApiTask:
    def __init__(self, keys_dir='kiwoom_keys'):
        self.name = "키움증권 API 연동"
        self.base_url = "https://api.kiwoom.com"
        self.keys_dir = keys_dir
        self.credentials = {}  # {account: {'appkey': '', 'secretkey': ''}}
        self.tokens = {}       # {account: 'access_token'}
        
    async def initialize(self):
        """초기화: 키 파일 로드 및 전체 계좌 토큰 발급 (plan.md 1, 2단계)"""
        self._load_keys()
        await self._issue_all_tokens()

    def _load_keys(self):
        """kiwoom_keys 디렉토리에서 계좌별 인증 정보(App/Secret Key)를 로드합니다."""
        if not os.path.exists(self.keys_dir):
            logger.warning(f"[{self.name}] {self.keys_dir} 디렉토리가 존재하지 않습니다.")
            return

        for filename in os.listdir(self.keys_dir):
            if filename.endswith('_appkey.txt'):
                account = filename.split('_')[0]
                self.credentials.setdefault(account, {})
                with open(os.path.join(self.keys_dir, filename), 'r', encoding='utf-8') as f:
                    self.credentials[account]['appkey'] = f.read().strip()
            elif filename.endswith('_secretkey.txt'):
                account = filename.split('_')[0]
                self.credentials.setdefault(account, {})
                with open(os.path.join(self.keys_dir, filename), 'r', encoding='utf-8') as f:
                    self.credentials[account]['secretkey'] = f.read().strip()
        
        logger.info(f"[{self.name}] 로드된 계좌 리스트: {list(self.credentials.keys())}")

    async def _issue_all_tokens(self):
        """모든 계좌에 대해 비동기적으로 접근 토큰(Access Token)을 발급받습니다."""
        async with aiohttp.ClientSession() as session:
            tasks = [self.issue_token(session, account) for account in self.credentials]
            if tasks:
                await asyncio.gather(*tasks)

    async def issue_token(self, session, account):
        """특정 계좌의 접근 토큰을 발급받아 딕셔너리에 관리합니다."""
        url = f"{self.base_url}/oauth2/token"  # 토큰 발급 엔드포인트
        creds = self.credentials.get(account)
        if not creds:
            return
        
        data = {
            "grant_type": "client_credentials",
            "appkey": creds.get('appkey'),
            "secretkey": creds.get('secretkey')
        }
        
        try:
            async with session.post(url, json=data) as response:
                if response.status == 200:
                    res_data = await response.json()
                    self.tokens[account] = res_data.get("token")
                    logger.info(f"[{self.name}] 계좌 {account} 토큰 발급 성공")
                else:
                    logger.error(f"[{self.name}] 계좌 {account} 토큰 발급 실패 (Status: {response.status})")
        except Exception as e:
            logger.error(f"[{self.name}] 계좌 {account} 토큰 발급 중 예외 발생: {e}")

    async def fetch_api(self, endpoint, account, data=None, api_id=""):
        """키움 API 통신 공통 래퍼(Wrapper) 및 예외/Rate Limit 처리"""
        url = f"{self.base_url}{endpoint}"
        token = self.tokens.get(account)
        
        if not token:
            logger.error(f"[{self.name}] 계좌 {account}의 유효한 토큰이 없습니다. 재발급이 필요합니다.")
            return None
            
        headers = {
            'authorization': f'Bearer {token}',
            'cont-yn': 'N',      # 연속조회 여부 (기본: N)
            'next-key': '',      # 연속조회 키 (기본: 빈 문자열)
            'api-id': api_id
        }
        try:
            # 타임아웃 10초 설정 (장 점검 등 무응답 시 무한 대기 방지)
            timeout = aiohttp.ClientTimeout(total=10)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.post(url, headers=headers, json=data or {}) as response:
                    if response.status == 200:
                        res_data = await response.json()
                        print(res_data)
                        
                        # API 서버 오류코드(Rate Limit 등) 대응 - 가이드코드 1700 확인
                        if str(res_data.get('err_code', '')) == '1700' or str(res_data.get('return_code', '')) == '1700':
                            logger.warning(f"[{self.name}] API 호출 제한 도달 (Rate Limit 1700). 잠시 후 재시도합니다.")
                            await asyncio.sleep(1.5) # 백오프 대기
                            return await self.fetch_api(endpoint, account, data, api_id=api_id)
                            
                        return res_data
                    else:
                        logger.error(f"[{self.name}] API 통신 오류 (Status: {response.status})")
                        return None
        except asyncio.TimeoutError:
            logger.error(f"[{self.name}] API 호출 시간 초과 (장 점검 시간 의심)")
            return None
        except Exception as e:
            logger.error(f"[{self.name}] API 호출 중 네트워크 예외 발생: {e}")
            return None

    async def get_deposit_info(self, account):
        """계좌별 예수금 상세 조회 (kt00001)"""
        endpoint = "/api/dostk/acnt"
        data = {
            "qry_tp": "3"
        }
        return await self.fetch_api(endpoint, account, data, api_id="kt00001")

    async def get_balance_info(self, account):
        """계좌별 평가 잔고 내역 조회 (kt00018)"""
        endpoint = "/api/dostk/acnt"
        data = {
            "qry_tp": "0",
            "dmst_stex_tp": "KRX"
        }
        return await self.fetch_api(endpoint, account, data, api_id="kt00018")

    def _safe_cast(self, val, to_type, default=0):
        """문자열 내 콤마 제거나 빈 문자열 등을 안전하게 타입 변환하는 유틸리티 메서드"""
        try:
            if isinstance(val, str):
                val = val.replace(',', '').strip()
            if not val:
                return default
            return to_type(val)
        except (ValueError, TypeError):
            return default

    def _parse_and_format(self, results):
        """API 원본 응답 데이터를 텔레그램 메시지 포맷으로 가공합니다."""
        if not results:
            return "⚠️ 조회된 계좌 데이터가 없습니다."

        lines = ["📊 *[키움증권 계좌 잔고 요약]* 📊\n"]

        for account, data in results.items():
            dep_data = data.get("예수금") or {}
            bal_data = data.get("잔고") or {}

            if data.get("error"):
                lines.append(f"🏦 *계좌번호:* `{account}`")
                lines.append("⚠️ 데이터를 불러오지 못했습니다. (통신 오류 또는 장 점검 의심)\n")
                lines.append("\n" + "➖"*15 + "\n")
                continue

            lines.append(f"🏦 *계좌번호:* `{account}`")

            # --- 1. 예수금 파싱 (가이드 및 일반적 TR 응답 기준) ---
            d2_pymn_alow_amt = self._safe_cast(dep_data.get("d2_pymn_alow_amt"), int)
            lines.append(f"💰 *D+2 출금가능금액:* {d2_pymn_alow_amt:,}원\n")

            # --- 2. 총 잔고 요약 파싱 ---
            bal_summary = bal_data.get('output1', bal_data) if isinstance(bal_data, dict) else {}
            if isinstance(bal_summary, list) and len(bal_summary) > 0:
                bal_summary = bal_summary[0]

            total_buy = self._safe_cast(bal_summary.get("총매입금액", 0), int)
            total_eval = self._safe_cast(bal_summary.get("총평가금액", 0), int)
            total_profit = self._safe_cast(bal_summary.get("총평가손익금액", 0), int)
            total_yield = self._safe_cast(bal_summary.get("총수익률(%)", 0.0), float)

            lines.append("📋 *[계좌 요약]*")
            lines.append(f"• 총 매입금액: {total_buy:,}원")
            lines.append(f"• 총 평가금액: {total_eval:,}원")
            
            profit_icon = "🔴" if total_profit > 0 else "🔵" if total_profit < 0 else "⚫"
            lines.append(f"• 총 평가손익: {profit_icon} {total_profit:,}원 ({total_yield:+.2f}%)\n")

            # --- 3. 개별 종목 상세 파싱 ---
            items = bal_data.get('output2', bal_data.get('items', [])) if isinstance(bal_data, dict) else []
            if isinstance(items, list) and items:
                lines.append("📝 *[보유 종목 상세]*")
                for idx, item in enumerate(items, 1):
                    if not isinstance(item, dict):
                        continue
                    name = item.get("종목명", "알수없음").strip()
                    qty = self._safe_cast(item.get("보유수량", 0), int)
                    profit = self._safe_cast(item.get("평가손익", 0), int)
                    rate = self._safe_cast(item.get("수익률(%)", 0.0), float)
                    
                    item_icon = "🔺" if profit > 0 else "🔻" if profit < 0 else "➖"
                    lines.append(f"{idx}. {name}: {qty}주 | {item_icon} {profit:,}원 ({rate:+.2f}%)")
            else:
                lines.append("📝 보유 중인 종목이 없습니다.")

            lines.append("\n" + "➖"*15 + "\n")

        return "\n".join(lines).strip()

    async def run(self):
        logger.info(f"실행 중: {self.name}")
        
        try:
            if not self.tokens:
                await self.initialize()
                
            if not self.tokens:
                return "⚠️ 키움증권 인증 토큰 발급에 실패하여 데이터를 조회할 수 없습니다.", None
                
            results = {}
            success_count = 0
            
            for account in self.credentials:
                deposit_data = await self.get_deposit_info(account)
                balance_data = await self.get_balance_info(account)
                
                if deposit_data is None and balance_data is None:
                    logger.warning(f"[{self.name}] 계좌 {account} 조회 실패 (장 점검 또는 네트워크 오류 의심)")
                    results[account] = {"error": True}
                else:
                    results[account] = {"예수금": deposit_data or {}, "잔고": balance_data or {}}
                    success_count += 1
                    
            if success_count == 0 and self.credentials:
                return "⚠️ 키움증권 데이터 조회에 실패했습니다.\n(현재 장 점검 시간이거나 네트워크 연결에 문제가 있을 수 있습니다.)", None
                
            formatted_message = self._parse_and_format(results)
            return formatted_message, None
            
        except Exception as e:
            logger.error(f"[{self.name}] 데이터 수집 중 예기치 않은 오류 발생: {e}")
            return "⚠️ 키움증권 계좌 조회 중 시스템 내부 오류가 발생했습니다.", None