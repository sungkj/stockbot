import os
import asyncio
import aiohttp
from typing import Any
from utils.logger import setup_logger

logger = setup_logger(__name__)

class KiwoomApiTask:
    def __init__(self, keys_dir: str = 'kiwoom_keys') -> None:
        self.name: str = "키움증권 API 연동"
        self.base_url: str = "https://api.kiwoom.com"
        self.keys_dir: str = keys_dir
        self.credentials: dict[str, dict[str, str]] = {}  # {account: {'appkey': '', 'secretkey': ''}}
        self.tokens: dict[str, str] = {}                  # {account: 'access_token'}
        
    async def initialize(self) -> None:
        """초기화: 키 파일 로드 및 전체 계좌 토큰 발급 (plan.md 1, 2단계)"""
        self._load_keys()
        await self._issue_all_tokens()

    def _load_keys(self) -> None:
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
        
        # Fail-fast: 필수 키(appkey, secretkey) 누락 검증
        for acc, creds in self.credentials.items():
            if 'appkey' not in creds or 'secretkey' not in creds:
                raise KeyError(f"[{self.name}] 계좌 {acc}의 appkey 또는 secretkey가 누락되었습니다.")
        
        logger.info(f"[{self.name}] 로드된 계좌 리스트: {list(self.credentials.keys())}")

    async def _issue_all_tokens(self) -> None:
        """모든 계좌에 대해 비동기적으로 접근 토큰(Access Token)을 발급받습니다."""
        async with aiohttp.ClientSession() as session:
            tasks = [self.issue_token(session, account) for account in self.credentials]
            if tasks:
                await asyncio.gather(*tasks)

    async def issue_token(self, session: aiohttp.ClientSession, account: str) -> None:
        """특정 계좌의 접근 토큰을 발급받아 딕셔너리에 관리합니다."""
        url = f"{self.base_url}/oauth2/token"  # 토큰 발급 엔드포인트
        
        if account not in self.credentials:
            raise KeyError(f"[{self.name}] {account} 계좌의 인증 정보가 존재하지 않습니다.")
            
        creds = self.credentials[account]
        
        data = {
            "grant_type": "client_credentials",
            "appkey": creds['appkey'],
            "secretkey": creds['secretkey']
        }
        
        try:
            async with session.post(url, json=data) as response:
                if response.status == 200:
                    res_data = await response.json()
                    if "token" not in res_data:
                        raise KeyError(f"[{self.name}] 응답 데이터에 'token' 키가 누락되었습니다.")
                    self.tokens[account] = res_data["token"]
                    logger.info(f"[{self.name}] 계좌 {account} 토큰 발급 성공")
                else:
                    logger.error(f"[{self.name}] 계좌 {account} 토큰 발급 실패 (Status: {response.status})")
                    raise ValueError(f"토큰 발급 실패: HTTP {response.status}")
        except Exception as e:
            logger.error(f"[{self.name}] 계좌 {account} 토큰 발급 중 예외 발생: {e}")
            raise

    async def fetch_api(self, endpoint: str, account: str, data: dict[str, Any] | None = None, api_id: str = "") -> dict[str, Any] | None:
        """키움 API 통신 공통 래퍼(Wrapper) 및 예외/Rate Limit 처리"""
        url = f"{self.base_url}{endpoint}"
        
        if account not in self.tokens:
            raise KeyError(f"[{self.name}] 계좌 {account}의 유효한 토큰이 없습니다.")
            
        token = self.tokens[account]
            
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
                        
                        # API 서버 오류코드(Rate Limit 등) 대응 - 가이드코드 1700 확인
                        err_code = str(res_data.get('err_code', ''))
                        ret_code = str(res_data.get('return_code', ''))
                        if err_code == '1700' or ret_code == '1700':
                            logger.warning(f"[{self.name}] API 호출 제한 도달 (Rate Limit 1700). 잠시 후 재시도합니다.")
                            await asyncio.sleep(1.5) # 백오프 대기
                            return await self.fetch_api(endpoint, account, data, api_id=api_id)
                            
                        return res_data
                    else:
                        logger.error(f"[{self.name}] API 통신 오류 (Status: {response.status})")
                        raise ValueError(f"API 통신 오류: HTTP {response.status}")
        except asyncio.TimeoutError:
            logger.error(f"[{self.name}] API 호출 시간 초과 (장 점검 시간 의심)")
            return None
        except Exception as e:
            logger.error(f"[{self.name}] API 호출 중 네트워크 예외 발생: {e}")
            return None

    async def get_deposit_info(self, account: str) -> dict[str, Any] | None:
        """계좌별 예수금 상세 조회 (kt00001)"""
        endpoint = "/api/dostk/acnt"
        data = {
            "qry_tp": "3"
        }
        return await self.fetch_api(endpoint, account, data, api_id="kt00001")

    async def get_balance_info(self, account: str) -> dict[str, Any] | None:
        """계좌별 평가 잔고 내역 조회 (kt00018)"""
        endpoint = "/api/dostk/acnt"
        data = {
            "qry_tp": "1",
            "dmst_stex_tp": "KRX"
        }
        return await self.fetch_api(endpoint, account, data, api_id="kt00018")

    def _safe_cast(self, val: Any, to_type: type) -> Any:
        """문자열 내 콤마 제거 등 안전하게 타입 변환을 시도하며 실패 시 예외를 발생시킵니다."""
        if val is None:
            raise ValueError("변환할 값이 None입니다.")
        if isinstance(val, str):
            val = val.replace(',', '').strip()
            if not val:
                raise ValueError("변환할 문자열이 비어있습니다.")
        return to_type(val)

    def _parse_and_format(self, results: dict[str, Any]) -> str:
        """API 원본 응답 데이터를 텔레그램 메시지 포맷으로 가공합니다."""
        if not results:
            raise ValueError("조회된 계좌 데이터가 없습니다.")

        lines: list[str] = ["📊 *[키움증권 계좌 잔고 요약]* 📊\n"]

        for account, data in results.items():
            if data.get("error"):
                lines.append(f"🏦 *계좌번호:* `{account}`")
                lines.append("⚠️ 데이터를 불러오지 못했습니다. (통신 오류 또는 장 점검 의심)\n")
                lines.append("\n" + "➖"*15 + "\n")
                continue

            lines.append(f"🏦 *계좌번호:* `{account}`")

            if "예수금" not in data or "잔고" not in data:
                raise KeyError(f"계좌 {account}의 필수 데이터(예수금 또는 잔고)가 누락되었습니다.")
                
            dep_data = data["예수금"]
            bal_data = data["잔고"]

            # --- 1. 예수금 파싱 (REST API 키 기준 반영) ---
            if "d2_pymn_alow_amt" in dep_data:
                raw_d2 = dep_data["d2_pymn_alow_amt"]
            elif "dbst_bal" in dep_data:
                raw_d2 = dep_data["dbst_bal"]
            else:
                raise KeyError("예수금 데이터에서 'd2_pymn_alow_amt' 또는 'dbst_bal' 키를 찾을 수 없습니다.")
                
            d2_pymn_alow_amt = self._safe_cast(raw_d2, int)
            lines.append(f"💰 *D+2 출금가능금액:* {d2_pymn_alow_amt:,}원\n")

            # --- 2. 총 잔고 요약 파싱 (REST API 키 반영) ---
            bal_summary = bal_data
            if isinstance(bal_summary, list):
                if not bal_summary:
                    raise ValueError("잔고 요약 리스트가 비어 있습니다.")
                bal_summary = bal_summary[0]

            raw_buy = bal_summary.get("tot_pur_amt") or bal_summary.get("tot_buy_amt")
            raw_eval = bal_summary.get("tot_evlt_amt") or bal_summary.get("tot_eval_amt")
            raw_profit = bal_summary.get("tot_evlt_pl") or bal_summary.get("tot_evltv_prft") or bal_summary.get("tot_eval_pl_amt")
            raw_yield = bal_summary.get("tot_prft_rt") or bal_summary.get("tot_rtn_rt")
            
            if raw_buy is None or raw_eval is None or raw_profit is None or raw_yield is None:
                # 데이터가 없는 경우 0으로 처리
                raw_buy, raw_eval, raw_profit, raw_yield = raw_buy or "0", raw_eval or "0", raw_profit or "0", raw_yield or "0.0"

            total_buy = self._safe_cast(raw_buy, int)
            total_eval = self._safe_cast(raw_eval, int)
            total_profit = self._safe_cast(raw_profit, int)
            total_yield = self._safe_cast(raw_yield, float)

            lines.append("📋 *[계좌 요약]*")
            lines.append(f"• 총 매입금액: {total_buy:,}원")
            lines.append(f"• 총 평가금액: {total_eval:,}원")
            
            profit_icon = "🔴" if total_profit > 0 else "🔵" if total_profit < 0 else "⚫"
            lines.append(f"• 총 평가손익: {profit_icon} {total_profit:,}원 ({total_yield:+.2f}%)\n")

            # --- 3. 개별 종목 상세 파싱 (REST API 키 반영) ---
            items: list[dict[str, Any]] = bal_data.get("acnt_evlt_remn_indv_tot", [])
            if not items and isinstance(bal_data, dict):
                for key, val in bal_data.items():
                    if isinstance(val, list):
                        items = val
                        break

            if items:
                lines.append("📝 *[보유 종목 상세]*")
                for idx, item in enumerate(items, 1):
                    if not isinstance(item, dict):
                        continue
                        
                    name = item.get("stk_nm") or item.get("prdt_name") or "알수없음"
                    
                    raw_qty = item.get("rmnd_qty") or item.get("hldg_qty") or "0"
                    raw_item_profit = item.get("evltv_prft") or item.get("eval_pl_amt") or "0"
                    raw_item_rate = item.get("prft_rt") or item.get("rtn_rt") or "0.0"

                    qty = self._safe_cast(raw_qty, int)
                    profit = self._safe_cast(raw_item_profit, int)
                    rate = self._safe_cast(raw_item_rate, float)
                    
                    item_icon = "🔺" if profit > 0 else "🔻" if profit < 0 else "➖"
                    lines.append(f"{idx}. {name.strip()}: {qty:,}주 | {item_icon} {profit:,}원 ({rate:+.2f}%)")
            else:
                lines.append("📝 보유 중인 종목이 없습니다.")

            lines.append("\n" + "➖"*15 + "\n")

        return "\n".join(lines).strip()

    async def run(self) -> tuple[str, None]:
        logger.info(f"실행 중: {self.name}")
        
        try:
            if not self.tokens:
                await self.initialize()
                
            if not self.tokens:
                raise RuntimeError("인증 토큰 발급에 실패하여 데이터를 조회할 수 없습니다.")
                
            results: dict[str, Any] = {}
            success_count = 0
            
            for account in self.credentials:
                deposit_data = await self.get_deposit_info(account)
                balance_data = await self.get_balance_info(account)
                
                if deposit_data is None and balance_data is None:
                    logger.warning(f"[{self.name}] 계좌 {account} 조회 실패 (장 점검 또는 네트워크 오류 의심)")
                    results[account] = {"error": True}
                else:
                    if deposit_data is None or balance_data is None:
                        raise ValueError(f"계좌 {account}의 일부 데이터만 응답받았습니다.")
                    results[account] = {"예수금": deposit_data, "잔고": balance_data}
                    success_count += 1
                    
            if success_count == 0 and self.credentials:
                raise RuntimeError("모든 계좌의 데이터 조회에 실패했습니다. (장 점검 또는 네트워크 연결 문제)")
                
            formatted_message = self._parse_and_format(results)
            return formatted_message, None
            
        except Exception as e:
            logger.error(f"[{self.name}] 데이터 수집 중 예외 발생: {e}")
            return f"⚠️ 키움증권 계좌 조회 중 오류가 발생했습니다: {str(e)}", None