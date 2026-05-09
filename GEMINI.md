📌 프로젝트 개요
언어: Python 3.13

목적: 범용 파이썬 애플리케이션 개발 및 유지보수

환경 관리: venv 또는 conda를 통한 가상환경 사용 권장

🛠 실행 및 도구 (Commands)
의존성 설치: pip install -r requirements.txt

프로그램 실행: python main.py (또는 프로젝트 진입점 파일)

코드 포맷팅: black .

정적 분석: flake8 또는 mypy .

📝 코딩 가이드라인 (Coding Rules)
언어 원칙: 모든 코드 설명, 가이드, 에이전트의 답변은 한국어로 작성한다.

표준 준수: PEP 8 스타일 가이드를 준수하여 작성한다.

명명 규칙:

  - 변수 및 함수: snake_case

  - 클래스: PascalCase

  - 상수: UPPER_SNAKE_CASE

타입 힌트: 모든 함수 정의 시 매개변수와 반환값에 Type Hints를 필수적으로 포함한다.

  예: def process_data(items: list[str]) -> int:

문서화: 복잡한 로직이 포함된 함수나 클래스에는 Docstring("""...""")을 사용하여 설명을 추가한다.

주석: 주석은 한글로 작성한다.


⚠️ 에이전트 행동 지침
에러 처리: 예외 가능성이 있는 곳에는 try-except 블록을 적절히 사용하고, 사용자에게 명확한 에러 메시지를 제공한다.

환경 변수: API 키, 비밀번호 등 민감한 정보는 절대 코드에 직접 쓰지 않고 .env 파일을 통해 로드하도록 코드를 짠다.

가독성: 한 줄이 너무 길어지지 않게 관리하며, 이해하기 어려운 복잡한 한 줄짜리 코드(List Comprehension 등)보다는 명확한 여러 줄의 코드를 선호한다.


* 현재 프로젝트
- 키움 API 관련 코드 작성 시에는 `docs/kiwoom_api_가이드.txt`와 `docs/키움 REST API 문서.xlsx`를 참고해서 작성한다.