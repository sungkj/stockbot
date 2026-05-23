# 시스템 아키텍처 (Architecture)

## 1. 개요
Stockbot은 비동기 기반으로 동작하는 텔레그램 챗봇 시스템입니다. 키움증권 REST API와 연동하여 주식 계좌 정보를 조회하고, 주기적인 스케줄링 작업을 통해 구글 트렌드, 뉴스, 타 텔레그램 방의 정보를 모니터링하여 사용자에게 전달합니다.

## 2. 시스템 구성도 및 디렉토리 구조
프로젝트는 기능별로 모듈화되어 있으며, 각 모듈은 독립적인 역할을 수행합니다.

- **`main.py`**: 프로그램의 진입점. 텔레그램 봇 인스턴스(`TeleBotApp`)와 스케줄러(`TaskManager`)를 초기화하고 비동기 이벤트 루프를 실행합니다.
- **`core/`**: 시스템의 핵심 구동 영역.
  - `bot_app.py`: `python-telegram-bot`을 활용하여 봇 애플리케이션을 관리하고 명령어(`/start`, `/잔고`) 핸들러를 등록합니다.
  - `task_manager.py`: `JobQueue`를 활용하여 각 작업(Task)들의 주기적인 실행(스케줄링)을 관리합니다.
- **`tasks/`**: 개별 비즈니스 로직을 수행하는 모듈.
  - `kiwoom_api.py`: 키움증권 REST API와의 통신(접근 토큰 발급, 예수금 및 잔고 조회) 및 에러(Rate Limit 등) 처리를 담당합니다.
  - `google_trends.py`: 구글 트렌드 데이터 수집 및 분석을 담당합니다.
  - `news_monitor.py`: 특정 키워드에 대한 실시간 뉴스 모니터링을 수행합니다.
  - `telegram_monitor.py`: User-Bot을 활용하여 타 텔레그램 채널/그룹의 메시지를 모니터링합니다.
- **`utils/`**: 공통으로 사용되는 유틸리티 함수.
  - `logger.py`: 시스템 전반의 로깅 설정을 담당합니다.
  - `chart_drawer.py`: `matplotlib`을 이용해 수집된 데이터를 차트 이미지로 렌더링합니다.
- **설정 및 보안 데이터**:
  - `config.yaml`: 봇 토큰, 수신자 ID 등 시스템 전반의 설정값 저장.
  - `kiwoom_keys/`: 키움증권 계좌별 API 인증키(App Key, Secret Key)를 텍스트 파일 형태로 관리.

## 3. 주요 기술 스택
- **언어**: Python 3.x
- **비동기 프레임워크**: `asyncio`
- **텔레그램 봇 프레임워크**: `python-telegram-bot` (명령어 처리 및 내부 JobQueue를 통한 스케줄링)
- **HTTP 통신**: `aiohttp` (키움 API 등 외부 비동기 네트워크 요청)
- **데이터 파싱 및 설정**: `PyYAML`
- **시각화**: `matplotlib`
- **User-Bot (예정)**: `pyrogram`

## 4. 데이터 흐름 (Data Flow)
### 4.1. 스케줄링 기반 자동 발송
1. `TaskManager`에 등록된 시간에 맞춰 Task 실행 (예: 15:40 키움증권 잔고 요약).
2. `tasks.kiwoom_api` 모듈이 메모리에 저장된 Access Token을 사용하여 비동기 HTTP 요청(`aiohttp`) 전송.
3. API 응답 데이터를 파싱하고 텔레그램 메시지 포맷으로 가공.
4. `TaskManager`의 래퍼 함수가 텔레그램 API를 호출하여 사용자(`config.yaml`에 정의된 `user_id`)에게 메시지 발송.

### 4.2. 사용자 명령어 기반 즉각 응답
1. 사용자가 텔레그램에서 `/잔고` 명령어 입력.
2. `TeleBotApp`에 등록된 핸들러가 이를 감지하여 `KiwoomApiTask.run()` 호출.
3. 데이터 수집 및 가공 후 `update.message.reply_text()`를 통해 즉각 응답.

## 5. 보안 및 에러 처리
- **인증 정보 격리**: 민감 정보는 코드 내에 하드코딩하지 않고 외부 파일(`config.yaml`, `kiwoom_keys/*`)에서 로드합니다.
- **Rate Limit 대응**: 키움증권 API 호출 시 `1700` 에러(호출 제한)가 발생하면 `asyncio.sleep`을 통한 백오프(Back-off) 대기 후 재시도하는 로직이 적용되어 있습니다.
- **타임아웃 및 장 점검 대응**: API 요청 시 Timeout을 설정하여 무한 대기를 방지하며, 데이터 응답이 없는 경우 장 점검 시간으로 간주하여 안전하게 예외 처리 및 알림을 전송합니다.