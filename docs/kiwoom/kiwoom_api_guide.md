# REST API 이해하기

## REST API란 무엇인가요?
REST API는 API의 한 종류로, "Representational State Transfer"의 약자입니다. 데이터를 주고받는 방식 중 하나로, URL(주소)과 HTTP 메서드(GET, POST 등)을 사용하여 서버와 통신합니다. 쉽게 말하자면, REST API는 인터넷을 통해 요청을 보내고 응답을 받는 "규칙"입니다. 예를 들어 우리가 인터넷 브라우저에서 특정 웹페이지를 열 때, 브라우저는 URL을 통해 요청을 보내고 해당 데이터를 받아옵니다. REST API도 이와 비슷하게 프로그램이 서버에 요청을 보내고 데이터를 받아오는 방식입니다.

## REST API의 기본 동작 방식
* **URL(주소):** 데이터를 요청하거나 보낼 위치를 나타냅니다. 예: `https://api.kiwoom.com/api/dostk/ordr`
* **HTTP 메서드:** 서버와 어떤 작업을 할지 정하는 방식입니다.
  * `GET`: 데이터를 가져오는 요청
  * `POST`: 새로운 데이터를 보내는 요청
  * `PUT`: 데이터를 수정하는 요청
  * `DELETE`: 데이터를 삭제하는 요청

REST API는 간단하고 직관적입니다. REST 방식을 사용하지 않는다면, 데이터를 주고받기 위해 복잡한 프로토콜이나 별도의 파일 변환 작업이 필요할 수 있습니다. 파일 저장 및 처리 과정에서 시간이 오래 걸리고, 서버와 클라이언트 간에 통신 오류가 발생할 가능성이 높습니다. 반면 REST API를 사용하면 간단한 코드로 데이터를 주고받을 수 있습니다.

```python
url = 'https://api.kiwoom.com/api/dostk/ordr'
data = {
    '종목코드': '039490',
    '주문수량': 1,
    '매매구분': '시장가'
}
response = requests.post(url, json=data)
```

REST API는 URL과 HTTP 메서드만 알면 서버와 통신하여 데이터를 받을 수 있습니다. 추가적인 파일 처리나 복잡한 설정이 필요하지 않기 때문에 대부분의 프로그래밍 언어에서 쉽게 사용할 수 있습니다.

여기서 사용한 `requests`는 Python의 requests 라이브러리를 이용한 것인데 requests 라이브러리는 REST API와 같은 HTTP 기반의 요청을 쉽게 처리할 수 있도록 도와주는 도구입니다. HTTP 요청(GET, POST 등)을 간단한 코드로 작성할 수 있어 REST API 작업에 자주 사용됩니다. requests를 활용하면, 데이터를 요청하거나 서버에 보낼 때 복잡한 작업을 줄이고 효율적으로 통신할 수 있습니다.

## JSON이란?
JSON은 "JavaScript Object Notation"의 약자로, 데이터를 저장하거나 교환할 때 사용하는 매우 간단하고 직관적인 형식입니다. REST API를 통해 데이터를 주고받을 때, 데이터 표현 형식으로 주로 JSON형식을 사용합니다. (cf. JSON 외에도 XML, RSS 등 다양한 표현 형식이 있습니다.)

JSON의 구조는 다음과 같은 기본 요소로 구성됩니다:
* **키(Key)와 값(Value):** JSON 데이터는 키와 값으로 이루어진 쌍으로 구성됩니다. 키는 데이터를 설명하는 이름이고, 값은 그 키에 해당하는 데이터를 나타냅니다.
* **데이터 타입:** JSON에서 값은 다양한 데이터 타입을 가질 수 있습니다. 문자열, 숫자, 불리언 값, 배열, 객체 등이 포함됩니다. 예를 들어 문자열은 `'039490'`, 숫자는 `1`, 불리언 값은 `true` 또는 `false`로 표현됩니다. 배열은 여러 값을 나열한 형태로, 예를 들어 `["039490", "000660"]`처럼 구성할 수 있습니다. 객체는 여러 키-값 쌍으로 구성된 데이터 그룹으로, 예를 들어 `{ "종목코드": "039490", "주문수량": 1 }`와 같은 구조를 가집니다.
* **중첩 구조:** JSON은 객체 안에 객체를 포함하거나 배열 안에 객체를 포함하는 등 복잡한 데이터를 표현할 수 있는 유연한 구조를 가지고 있습니다.

아래는 키움증권 주식을 1주 시장가로 매수하기 위한 JSON 데이터 예시입니다:

```json
{
   "종목코드": "039490",
   "주문수량": 1,
   "매매구분": "시장가"
}
```

이 데이터를 보면, `"종목코드"`라는 키에는 `"039490"`이라는 값이 들어 있고, `"주문수량"`에는 숫자 `1`이 들어 있습니다. `"매매구분"`에는 `"시장가"`라는 문자열이 들어 있습니다.

### JSON의 장점은?
JSON은 우선, 사람이 읽기에 매우 쉽습니다. JSON은 직관적인 구조를 가지고 있어서 데이터를 쉽게 이해할 수 있습니다. 또한, 대부분의 프로그래밍 언어에서 JSON을 쉽게 파싱(해석)하고 생성할 수 있어 컴퓨터가 처리하기에도 용이합니다. 게다가 JSON은 널리 사용되는 표준 데이터 형식이기 때문에 다양한 시스템 간에 쉽게 호환됩니다.

JSON은 API와 데이터 통신을 할 때 중요한 역할을 합니다. REST API를 효과적으로 사용하려면 JSON 형식을 잘 이해하는 것이 큰 도움이 됩니다.

## 매수주문 따라해보기
이제 API를 사용해 주식을 매수하는 방법을 코드로 나누어 설명드리겠습니다.

### 1. 요청할 URL 구성
* **URL(주소):** 데이터를 요청하거나 보낼 위치를 나타냅니다. 예: `https://api.kiwoom.com/api/dostk/ordr`

```python
host = 'https://api.kiwoom.com' # 실전투자 서버
endpoint = '/api/dostk/ordr' # 매수 주문 API
url = host + endpoint
```

Host는 API 서버의 기본 주소로, 요청을 처리하는 서버의 위치를 나타냅니다. 예를 들어, 여기에서는 실전 투자 환경의 API 서버 주소인 `https://api.kiwoom.com`이 사용됩니다. Endpoint는 API가 제공하는 특정 기능에 접근하기 위한 경로입니다. 매수 주문의 경우 `/api/dostk/ordr`라는 경로를 사용하여 해당 기능을 호출합니다. Host와 Endpoint를 조합하여 최종적으로 요청할 URL을 구성합니다.

### 2. 헤더(Header)란?
헤더는 API 요청에 필요한 추가 정보를 담고 있는 부분입니다. 요청을 처리하는 데 필요한 메타데이터나 인증 정보를 포함하며, 서버가 요청을 이해하고 처리할 수 있도록 도와줍니다.

**헤더 구성 요소**

```python
headers = {
    'Content-Type': 'application/json;charset=UTF-8',  # 요청 데이터의 형식
    'authorization': f'Bearer {token}',  # 인증 토큰
    'cont-yn': cont_yn,  # 연속조회 여부
    'next-key': next_key,  # 연속조회 키
    'api-id': 'kt10000',  # 요청하는 TR 이름
}
```

### 3. 바디(Body)란?
바디는 API 요청에서 전달할 주요 데이터를 포함하는 부분입니다. 바디에는 매매와 관련된 세부 정보가 JSON 형식으로 포함됩니다.

**바디 구성 요소**

```python
data = {
    'dmst_stex_tp': 'KRX',  # 거래소 구분 (예: KRX)
    'stk_cd': '039490',  # 주문할 종목코드 (키움증권)
    'ord_qty': '1',  # 주문 수량
    'ord_uv': '',  # 주문 단가 (시장가 주문은 빈 값)
    'trde_tp': '3',  # 매매 구분 (3: 시장가 주문)
    'cond_uv': '',  # 조건 단가 (해당 사항 없으면 빈 값)
}
```

### 4. 요청 실행
모든 구성 요소를 준비한 뒤 API 요청 실행:

```python
response = requests.post(url, headers=headers, json=data)
```

이 코드는 HTTP POST 요청을 통해 데이터를 서버에 전송합니다. 요청에는 서버 주소, 요청 헤더, 그리고 요청 본문이 포함됩니다.
* 요청에 사용되는 `url`은 서버의 주소로, Host와 Endpoint를 조합하여 만들어집니다. 이 주소는 요청이 어디로 전송될지를 나타냅니다.
* `headers`는 요청에 포함된 추가 정보로, 데이터의 형식(예: JSON)이나 인증 정보를 전달합니다. 이를 통해 서버는 요청이 올바른 형식으로 전송되었는지 확인할 수 있습니다.
* `json`은 요청 본문에 포함된 데이터입니다. 주식 주문과 관련된 주요 정보들이 JSON 형식으로 여기에 포함됩니다. 이를 통해 서버는 요청의 내용을 처리하고 필요한 작업을 수행합니다.
* 이 요청이 전송되면 서버는 요청을 처리한 결과를 반환하며, 그 결과는 `response` 변수에 저장됩니다. 이 변수는 응답 결과의 HTTP 상태코드, 헤더, 본문 데이터를 포함하고 있습니다.

**cf. HTTP(Hypertext Transfer Protocol) 상태코드란?**
앞서 REST API는 URL과 HTTP 메서드를 사용하여 서버와 통신하는 규칙이라고 서술했었습니다.
이 HTTP 메서드로 요청을 보낼 때 요청이 성공적으로 이루어졌는지, 만일 실패했다면 어떤 이유로 실패했는지를 간단히 나타내는 코드를 HTTP 상태코드라고 합니다.
대표적인 HTTP 상태코드 몇 가지만 참고로 적어드립니다.

* `200(OK)`: 요청 성공
* `400(Bad Request)`: 요청의 문법이 잘못되어 서버가 요청을 이해할 수 없음
* `403(Forbidden)`: 클라이언트가 리소스에 접근할 권리를 갖고 있지 않음
* `404(Not Found)`: 서버에서 요청받은 리소스를 찾을 수 없음

### 5. 응답 처리
응답 결과를 확인하는 코드입니다:

```python
print('Code:', response.status_code)  # HTTP 상태 코드 출력
print('Header:', json.dumps(response.headers, indent=4, ensure_ascii=False))  # 응답 헤더 출력
print('Body:', json.dumps(response.json(), indent=4, ensure_ascii=False))  # 응답 바디 출력
```

이 출력 결과를 통해 요청이 성공했는지와 서버에서 반환한 데이터를 확인할 수 있습니다.
이처럼 REST API를 활용하면 프로그램을 통해 주식 매매를 쉽게 요청할 수 있습니다. 처음에는 조금 낯설 수 있지만, 한 번 익숙해지면 매우 편리하게 활용할 수 있습니다.

---

# Web Socket 이해하기

## WebSocket이란
웹소켓(WebSocket)은 실시간으로 데이터를 주고받는 기술입니다.
예를 들어, 주식 시세나 채팅을 할 때, 새로고침 없이도 계속 업데이트되는 정보를 본 적이 있을 겁니다. 바로 이런 기능을 가능하게 하는 것이 웹소켓입니다.

## 웹소켓과 기존 방식의 차이
우리가 웹에서 정보를 가져올 때 보통은 HTTP를 사용합니다. HTTP는 요청(Request)을 보내고 응답(Response)을 받아야 합니다.
즉, 웹페이지가 데이터를 새로 받아오려면, 계속해서 요청을 보내야 합니다.
하지만 웹소켓은 다릅니다! 한 번 연결하면, 서버와 클라이언트(사용자) 사이에 직접 연결된 통로가 생겨서 실시간으로 데이터를 주고받을 수 있습니다.

쉽게 말해. 아래와 같이 설명할 수 있습니다.
* 📢 HTTP: "야 서버야, 새로운 정보 있어?" → 서버가 답함 (필요할 때마다 계속 물어봐야 함)
* 📢 WebSocket: "서버야, 나랑 연결 유지해!" → 서버가 알아서 새로운 정보가 생기면 바로 알려줌

## 그러면 웹소켓을 왜 사용할까요?
* **실시간 데이터 전송:** 주식 시세, 채팅, 게임에서 즉시 반응이 필요할 때 사용합니다.
* **양방향 통신:** 서버도 먼저 데이터를 보낼 수 있어요! (HTTP는 요청을 보내야만 응답이 옴)
* **연결 유지:** 한 번 연결하면 계속 사용할 수 있어서 빠릅니다.

## 웹소켓 vs. HTTP 비교

| 특징 | HTTP | WebSocket |
| --- | --- | --- |
| 연결방식 | 요청할 때마다 새 연결 | 한 번 연결되면 유지 |
| 데이터 전송 방향 | 클라이언트 → 서버 (단방향) | 클라이언트 ↔ 서버 (양방향) |
| 실시간 처리 | 요청해야만 응답 | 서버가 알아서 데이터 전송 |
| 사용 예시 | 웹사이트(일반적인 브라우징) | 채팅, 주식 시세, 게임 |

## 실시간 시세 조회 따라해보기
웹소켓을 활용하는 실제 Python 코드를 하나씩 쉽게 설명하겠습니다.

### 1. 필요한 라이브러리 가져오기

**1-1. 라이브러리 다운로드**

```bash
pip install asyncio
pip install websockets
```

**1-2. 라이브러리 Import**

```python
import asyncio
import websockets
import json
```

* `asyncio`: 비동기 작업을 쉽게 처리할 수 있게 해줍니다. (비동기 작업은 요청과 응답이 동시에 일어나지 않는 방식으로, 요청을 보내고 응답을 기다리는 동기 작업과는 달리 그 응답을 기다리지 않고 또 다른 요청을 병렬적으로 보낼 수 있는 방식을 말합니다. 그렇기에 시간이 오래 걸리는 작업을 효율적으로 실행하는 방식이기도 합니다.)
* `websockets`: 웹소켓을 사용할 수 있도록 도와주는 도구입니다.
* `json`: 데이터를 JSON 형식(문자열로 변환)으로 다룰 수 있도록 합니다.

### 2. 웹소켓 서버 정보 설정

```python
SOCKET_URL = 'wss://api.kiwoom.com:10000/api/dostk/websocket'  # 접속할 주소
ACCESS_TOKEN = '사용자 AccessToken'  # 로그인 후 받은 인증 토큰
```

* `SOCKET_URL`: 키움증권의 웹소켓 서버 주소
* `ACCESS_TOKEN`: 사용자의 인증을 확인하는 키

### 3. 웹소켓 클라이언트 만들기

```python
class WebSocketClient:
    def __init__(self, uri):
        self.uri = uri
        self.websocket = None
        self.connected = False
        self.keep_running = True
```

* `self.uri`: 연결할 서버의 주소
* `self.websocket`: 실제 웹소켓 연결을 관리하는 변수
* `self.connected`: 연결 상태 (True면 연결됨, False면 끊김)

### 4. 서버에 연결하기

```python
async def connect(self):
    try:
        self.websocket = await websockets.connect(self.uri)
        self.connected = True
        print("서버와 연결을 시도 중입니다.")

        # 로그인 패킷
        param = {
            'trnm': 'LOGIN',
            'token': ACCESS_TOKEN
        }

        print('실시간 시세 서버로 로그인 패킷을 전송합니다.')
        # 웹소켓 연결 시 로그인 정보 전달
        await self.send_message(message=param)

    except Exception as e:
        print(f'Connection error: {e}')
        self.connected = False
```

* `websockets.connect(self.uri)`: 웹소켓 서버에 연결을 시도합니다.
* 연결이 성공하면 `self.connected = True`로 변경합니다.

### 5. 메시지 보내기

```python
async def send_message(self, message):
    if not self.connected:
        await self.connect()  # 연결이 끊어졌다면 재연결
    if self.connected:
        # message가 문자열이 아니면 JSON으로 직렬화
        if not isinstance(message, str):
            message = json.dumps(message)

    await self.websocket.send(message)
    print(f'Message sent: {message}')
```

* 서버에 데이터를 보낼 때 JSON 형식으로 변환하여 전송합니다.
* 만약 연결이 끊어져 있다면, 자동으로 다시 연결합니다.

### 6. 서버에서 메시지 받기

```python
async def receive_messages(self):
    while self.keep_running:
        try:
            # 서버로부터 수신한 메시지를 JSON 형식으로 파싱
            response = json.loads(await self.websocket.recv())

            # 메시지 유형이 LOGIN일 경우 로그인 시도 결과 체크
            if response.get('trnm') == 'LOGIN':
                if response.get('return_code') != 0:
                    print('로그인 실패하였습니다. : ', response.get('return_msg'))
                    await self.disconnect()
                else:
                    print('로그인 성공하였습니다.')

            # 메시지 유형이 PING일 경우 수신값 그대로 송신
            elif response.get('trnm') == 'PING':
                await self.send_message(response)

            if response.get('trnm') != 'PING':
                print(f'실시간 시세 서버 응답 수신: {response}')

        except websockets.ConnectionClosed:
            print('Connection closed by the server')
            self.connected = False
            await self.websocket.close()
```

* 서버에서 새로운 메시지를 받으면 출력합니다.
* 연결이 끊기면 알림을 표시합니다.

### 7. 웹소켓 실행하기

```python
async def run(self):
    await self.connect()
    await self.receive_messages()
```

* 서버에 연결하고, 메시지를 계속 받을 준비를 합니다.

### 8. 웹소켓 종료하기

```python
async def disconnect(self):
    self.keep_running = False
    if self.connected and self.websocket:
        await self.websocket.close()
        self.connected = False
        print('Disconnected from WebSocket server')
```

* 웹소켓 연결을 종료하는 함수입니다.

### 9. 프로그램 실행하기

```python
async def main():
    # WebSocketClient 전역 변수 선언
    websocket_client = WebSocketClient(SOCKET_URL)

    # WebSocket 클라이언트를 백그라운드에서 실행합니다.
    receive_task = asyncio.create_task(websocket_client.run())

    # 실시간 항목 등록
    await asyncio.sleep(1)
    await websocket_client.send_message({
        'trnm': 'REG', # 서비스명
        'grp_no': '1', # 그룹번호
        'refresh': '1', # 기존등록유지여부
        'data': [{ # 실시간 등록 리스트
            'item': ['039490'], # 실시간 등록 요소
            'type': ['0B'], # 실시간 항목
        }]
    })

    # 수신 작업이 종료될 때까지 대기
    await receive_task

# asyncio로 프로그램을 실행합니다.
if __name__ == '__main__':
    asyncio.run(main())
```

* `WebSocketClient`를 만들어 실행합니다.
* `send_message`를 이용해 특정 주식 코드(039490)의 실시간 정보를 요청합니다.
* `asyncio.run(main())`을 사용하여 프로그램을 실행합니다.

이제 직접 실행해보면서 더 익숙해져 보시길 바라겠습니다.

___

# API 리스트

> **기능 구현을 위해서 반드시 아래 API 리스트 중 알맞은 항목을 찾아 해당 설명파일을 참고해야 한다.**

|   No. | API ID   | API 명             | 대분류      | 중분류    | URL                  | 설명 파일                                                             |
|------:|:---------|:------------------|:---------|:-------|:---------------------|:------------------------------------------------------------------|
|     1 | au10001  | 접근토큰 발급           | OAuth 인증 | 접근토큰발급 | /oauth2/token        | [au10001_접근토큰_발급.md](APIs/au10001_접근토큰_발급.md)                     |
|     2 | au10002  | 접근토큰폐기            | OAuth 인증 | 접근토큰폐기 | /oauth2/revoke       | [au10002_접근토큰폐기.md](APIs/au10002_접근토큰폐기.md)                       |
|     3 | ka00001  | 계좌번호조회            | 국내주식     | 계좌     | /api/dostk/acnt      | [ka00001_계좌번호조회.md](APIs/ka00001_계좌번호조회.md)                       |
|     4 | ka00198  | 실시간종목조회순위         | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka00198_실시간종목조회순위.md](APIs/ka00198_실시간종목조회순위.md)                 |
|     5 | ka01690  | 일별잔고수익률           | 국내주식     | 계좌     | /api/dostk/acnt      | [ka01690_일별잔고수익률.md](APIs/ka01690_일별잔고수익률.md)                     |
|     6 | ka10001  | 주식기본정보요청          | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10001_주식기본정보요청.md](APIs/ka10001_주식기본정보요청.md)                   |
|     7 | ka10002  | 주식거래원요청           | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10002_주식거래원요청.md](APIs/ka10002_주식거래원요청.md)                     |
|     8 | ka10003  | 체결정보요청            | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10003_체결정보요청.md](APIs/ka10003_체결정보요청.md)                       |
|     9 | ka10004  | 주식호가요청            | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka10004_주식호가요청.md](APIs/ka10004_주식호가요청.md)                       |
|    10 | ka10005  | 주식일주월시분요청         | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka10005_주식일주월시분요청.md](APIs/ka10005_주식일주월시분요청.md)                 |
|    11 | ka10006  | 주식시분요청            | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka10006_주식시분요청.md](APIs/ka10006_주식시분요청.md)                       |
|    12 | ka10007  | 시세표성정보요청          | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka10007_시세표성정보요청.md](APIs/ka10007_시세표성정보요청.md)                   |
|    13 | ka10008  | 주식외국인종목별매매동향      | 국내주식     | 기관/외국인 | /api/dostk/frgnistt  | [ka10008_주식외국인종목별매매동향.md](APIs/ka10008_주식외국인종목별매매동향.md)           |
|    14 | ka10009  | 주식기관요청            | 국내주식     | 기관/외국인 | /api/dostk/frgnistt  | [ka10009_주식기관요청.md](APIs/ka10009_주식기관요청.md)                       |
|    15 | ka10010  | 업종프로그램요청          | 국내주식     | 업종     | /api/dostk/sect      | [ka10010_업종프로그램요청.md](APIs/ka10010_업종프로그램요청.md)                   |
|    16 | ka10011  | 신주인수권전체시세요청       | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka10011_신주인수권전체시세요청.md](APIs/ka10011_신주인수권전체시세요청.md)             |
|    17 | ka10013  | 신용매매동향요청          | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10013_신용매매동향요청.md](APIs/ka10013_신용매매동향요청.md)                   |
|    18 | ka10014  | 공매도추이요청           | 국내주식     | 공매도    | /api/dostk/shsa      | [ka10014_공매도추이요청.md](APIs/ka10014_공매도추이요청.md)                     |
|    19 | ka10015  | 일별거래상세요청          | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10015_일별거래상세요청.md](APIs/ka10015_일별거래상세요청.md)                   |
|    20 | ka10016  | 신고저가요청            | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10016_신고저가요청.md](APIs/ka10016_신고저가요청.md)                       |
|    21 | ka10017  | 상하한가요청            | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10017_상하한가요청.md](APIs/ka10017_상하한가요청.md)                       |
|    22 | ka10018  | 고저가근접요청           | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10018_고저가근접요청.md](APIs/ka10018_고저가근접요청.md)                     |
|    23 | ka10019  | 가격급등락요청           | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10019_가격급등락요청.md](APIs/ka10019_가격급등락요청.md)                     |
|    24 | ka10020  | 호가잔량상위요청          | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10020_호가잔량상위요청.md](APIs/ka10020_호가잔량상위요청.md)                   |
|    25 | ka10021  | 호가잔량급증요청          | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10021_호가잔량급증요청.md](APIs/ka10021_호가잔량급증요청.md)                   |
|    26 | ka10022  | 잔량율급증요청           | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10022_잔량율급증요청.md](APIs/ka10022_잔량율급증요청.md)                     |
|    27 | ka10023  | 거래량급증요청           | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10023_거래량급증요청.md](APIs/ka10023_거래량급증요청.md)                     |
|    28 | ka10024  | 거래량갱신요청           | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10024_거래량갱신요청.md](APIs/ka10024_거래량갱신요청.md)                     |
|    29 | ka10025  | 매물대집중요청           | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10025_매물대집중요청.md](APIs/ka10025_매물대집중요청.md)                     |
|    30 | ka10026  | 고저PER요청           | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10026_고저PER요청.md](APIs/ka10026_고저PER요청.md)                     |
|    31 | ka10027  | 전일대비등락률상위요청       | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10027_전일대비등락률상위요청.md](APIs/ka10027_전일대비등락률상위요청.md)             |
|    32 | ka10028  | 시가대비등락률요청         | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10028_시가대비등락률요청.md](APIs/ka10028_시가대비등락률요청.md)                 |
|    33 | ka10029  | 예상체결등락률상위요청       | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10029_예상체결등락률상위요청.md](APIs/ka10029_예상체결등락률상위요청.md)             |
|    34 | ka10030  | 당일거래량상위요청         | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10030_당일거래량상위요청.md](APIs/ka10030_당일거래량상위요청.md)                 |
|    35 | ka10031  | 전일거래량상위요청         | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10031_전일거래량상위요청.md](APIs/ka10031_전일거래량상위요청.md)                 |
|    36 | ka10032  | 거래대금상위요청          | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10032_거래대금상위요청.md](APIs/ka10032_거래대금상위요청.md)                   |
|    37 | ka10033  | 신용비율상위요청          | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10033_신용비율상위요청.md](APIs/ka10033_신용비율상위요청.md)                   |
|    38 | ka10034  | 외인기간별매매상위요청       | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10034_외인기간별매매상위요청.md](APIs/ka10034_외인기간별매매상위요청.md)             |
|    39 | ka10035  | 외인연속순매매상위요청       | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10035_외인연속순매매상위요청.md](APIs/ka10035_외인연속순매매상위요청.md)             |
|    40 | ka10036  | 외인한도소진율증가상위       | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10036_외인한도소진율증가상위.md](APIs/ka10036_외인한도소진율증가상위.md)             |
|    41 | ka10037  | 외국계창구매매상위요청       | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10037_외국계창구매매상위요청.md](APIs/ka10037_외국계창구매매상위요청.md)             |
|    42 | ka10038  | 종목별증권사순위요청        | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10038_종목별증권사순위요청.md](APIs/ka10038_종목별증권사순위요청.md)               |
|    43 | ka10039  | 증권사별매매상위요청        | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10039_증권사별매매상위요청.md](APIs/ka10039_증권사별매매상위요청.md)               |
|    44 | ka10040  | 당일주요거래원요청         | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10040_당일주요거래원요청.md](APIs/ka10040_당일주요거래원요청.md)                 |
|    45 | ka10042  | 순매수거래원순위요청        | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10042_순매수거래원순위요청.md](APIs/ka10042_순매수거래원순위요청.md)               |
|    46 | ka10043  | 거래원매물대분석요청        | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10043_거래원매물대분석요청.md](APIs/ka10043_거래원매물대분석요청.md)               |
|    47 | ka10044  | 일별기관매매종목요청        | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka10044_일별기관매매종목요청.md](APIs/ka10044_일별기관매매종목요청.md)               |
|    48 | ka10045  | 종목별기관매매추이요청       | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka10045_종목별기관매매추이요청.md](APIs/ka10045_종목별기관매매추이요청.md)             |
|    49 | ka10046  | 체결강도추이시간별요청       | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka10046_체결강도추이시간별요청.md](APIs/ka10046_체결강도추이시간별요청.md)             |
|    50 | ka10047  | 체결강도추이일별요청        | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka10047_체결강도추이일별요청.md](APIs/ka10047_체결강도추이일별요청.md)               |
|    51 | ka10048  | ELW일별민감도지표요청      | 국내주식     | ELW    | /api/dostk/elw       | [ka10048_ELW일별민감도지표요청.md](APIs/ka10048_ELW일별민감도지표요청.md)           |
|    52 | ka10050  | ELW민감도지표요청        | 국내주식     | ELW    | /api/dostk/elw       | [ka10050_ELW민감도지표요청.md](APIs/ka10050_ELW민감도지표요청.md)               |
|    53 | ka10051  | 업종별투자자순매수요청       | 국내주식     | 업종     | /api/dostk/sect      | [ka10051_업종별투자자순매수요청.md](APIs/ka10051_업종별투자자순매수요청.md)             |
|    54 | ka10052  | 거래원순간거래량요청        | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10052_거래원순간거래량요청.md](APIs/ka10052_거래원순간거래량요청.md)               |
|    55 | ka10053  | 당일상위이탈원요청         | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10053_당일상위이탈원요청.md](APIs/ka10053_당일상위이탈원요청.md)                 |
|    56 | ka10054  | 변동성완화장치발동종목요청     | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10054_변동성완화장치발동종목요청.md](APIs/ka10054_변동성완화장치발동종목요청.md)         |
|    57 | ka10055  | 당일전일체결량요청         | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10055_당일전일체결량요청.md](APIs/ka10055_당일전일체결량요청.md)                 |
|    58 | ka10058  | 투자자별일별매매종목요청      | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10058_투자자별일별매매종목요청.md](APIs/ka10058_투자자별일별매매종목요청.md)           |
|    59 | ka10059  | 종목별투자자기관별요청       | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10059_종목별투자자기관별요청.md](APIs/ka10059_종목별투자자기관별요청.md)             |
|    60 | ka10060  | 종목별투자자기관별차트요청     | 국내주식     | 차트     | /api/dostk/chart     | [ka10060_종목별투자자기관별차트요청.md](APIs/ka10060_종목별투자자기관별차트요청.md)         |
|    61 | ka10061  | 종목별투자자기관별합계요청     | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10061_종목별투자자기관별합계요청.md](APIs/ka10061_종목별투자자기관별합계요청.md)         |
|    62 | ka10062  | 동일순매매순위요청         | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10062_동일순매매순위요청.md](APIs/ka10062_동일순매매순위요청.md)                 |
|    63 | ka10063  | 장중투자자별매매요청        | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka10063_장중투자자별매매요청.md](APIs/ka10063_장중투자자별매매요청.md)               |
|    64 | ka10064  | 장중투자자별매매차트요청      | 국내주식     | 차트     | /api/dostk/chart     | [ka10064_장중투자자별매매차트요청.md](APIs/ka10064_장중투자자별매매차트요청.md)           |
|    65 | ka10065  | 장중투자자별매매상위요청      | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10065_장중투자자별매매상위요청.md](APIs/ka10065_장중투자자별매매상위요청.md)           |
|    66 | ka10066  | 장마감후투자자별매매요청      | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka10066_장마감후투자자별매매요청.md](APIs/ka10066_장마감후투자자별매매요청.md)           |
|    67 | ka10068  | 대차거래추이요청          | 국내주식     | 대차거래   | /api/dostk/slb       | [ka10068_대차거래추이요청.md](APIs/ka10068_대차거래추이요청.md)                   |
|    68 | ka10069  | 대차거래상위10종목요청      | 국내주식     | 대차거래   | /api/dostk/slb       | [ka10069_대차거래상위10종목요청.md](APIs/ka10069_대차거래상위10종목요청.md)           |
|    69 | ka10072  | 일자별종목별실현손익요청_일자   | 국내주식     | 계좌     | /api/dostk/acnt      | [ka10072_일자별종목별실현손익요청_일자.md](APIs/ka10072_일자별종목별실현손익요청_일자.md)     |
|    70 | ka10073  | 일자별종목별실현손익요청_기간   | 국내주식     | 계좌     | /api/dostk/acnt      | [ka10073_일자별종목별실현손익요청_기간.md](APIs/ka10073_일자별종목별실현손익요청_기간.md)     |
|    71 | ka10074  | 일자별실현손익요청         | 국내주식     | 계좌     | /api/dostk/acnt      | [ka10074_일자별실현손익요청.md](APIs/ka10074_일자별실현손익요청.md)                 |
|    72 | ka10075  | 미체결요청             | 국내주식     | 계좌     | /api/dostk/acnt      | [ka10075_미체결요청.md](APIs/ka10075_미체결요청.md)                         |
|    73 | ka10076  | 체결요청              | 국내주식     | 계좌     | /api/dostk/acnt      | [ka10076_체결요청.md](APIs/ka10076_체결요청.md)                           |
|    74 | ka10077  | 당일실현손익상세요청        | 국내주식     | 계좌     | /api/dostk/acnt      | [ka10077_당일실현손익상세요청.md](APIs/ka10077_당일실현손익상세요청.md)               |
|    75 | ka10078  | 증권사별종목매매동향요청      | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka10078_증권사별종목매매동향요청.md](APIs/ka10078_증권사별종목매매동향요청.md)           |
|    76 | ka10079  | 주식틱차트조회요청         | 국내주식     | 차트     | /api/dostk/chart     | [ka10079_주식틱차트조회요청.md](APIs/ka10079_주식틱차트조회요청.md)                 |
|    77 | ka10080  | 주식분봉차트조회요청        | 국내주식     | 차트     | /api/dostk/chart     | [ka10080_주식분봉차트조회요청.md](APIs/ka10080_주식분봉차트조회요청.md)               |
|    78 | ka10081  | 주식일봉차트조회요청        | 국내주식     | 차트     | /api/dostk/chart     | [ka10081_주식일봉차트조회요청.md](APIs/ka10081_주식일봉차트조회요청.md)               |
|    79 | ka10082  | 주식주봉차트조회요청        | 국내주식     | 차트     | /api/dostk/chart     | [ka10082_주식주봉차트조회요청.md](APIs/ka10082_주식주봉차트조회요청.md)               |
|    80 | ka10083  | 주식월봉차트조회요청        | 국내주식     | 차트     | /api/dostk/chart     | [ka10083_주식월봉차트조회요청.md](APIs/ka10083_주식월봉차트조회요청.md)               |
|    81 | ka10084  | 당일전일체결요청          | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10084_당일전일체결요청.md](APIs/ka10084_당일전일체결요청.md)                   |
|    82 | ka10085  | 계좌수익률요청           | 국내주식     | 계좌     | /api/dostk/acnt      | [ka10085_계좌수익률요청.md](APIs/ka10085_계좌수익률요청.md)                     |
|    83 | ka10086  | 일별주가요청            | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka10086_일별주가요청.md](APIs/ka10086_일별주가요청.md)                       |
|    84 | ka10087  | 시간외단일가요청          | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka10087_시간외단일가요청.md](APIs/ka10087_시간외단일가요청.md)                   |
|    85 | ka10088  | 미체결 분할주문 상세       | 국내주식     | 계좌     | /api/dostk/acnt      | [ka10088_미체결_분할주문_상세.md](APIs/ka10088_미체결_분할주문_상세.md)             |
|    86 | ka10094  | 주식년봉차트조회요청        | 국내주식     | 차트     | /api/dostk/chart     | [ka10094_주식년봉차트조회요청.md](APIs/ka10094_주식년봉차트조회요청.md)               |
|    87 | ka10095  | 관심종목정보요청          | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10095_관심종목정보요청.md](APIs/ka10095_관심종목정보요청.md)                   |
|    88 | ka10098  | 시간외단일가등락율순위요청     | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka10098_시간외단일가등락율순위요청.md](APIs/ka10098_시간외단일가등락율순위요청.md)         |
|    89 | ka10099  | 종목정보 리스트          | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10099_종목정보_리스트.md](APIs/ka10099_종목정보_리스트.md)                   |
|    90 | ka10100  | 종목정보 조회           | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10100_종목정보_조회.md](APIs/ka10100_종목정보_조회.md)                     |
|    91 | ka10101  | 업종코드 리스트          | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10101_업종코드_리스트.md](APIs/ka10101_업종코드_리스트.md)                   |
|    92 | ka10102  | 회원사 리스트           | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka10102_회원사_리스트.md](APIs/ka10102_회원사_리스트.md)                     |
|    93 | ka10131  | 기관외국인연속매매현황요청     | 국내주식     | 기관/외국인 | /api/dostk/frgnistt  | [ka10131_기관외국인연속매매현황요청.md](APIs/ka10131_기관외국인연속매매현황요청.md)         |
|    94 | ka10170  | 당일매매일지요청          | 국내주식     | 계좌     | /api/dostk/acnt      | [ka10170_당일매매일지요청.md](APIs/ka10170_당일매매일지요청.md)                   |
|    95 | ka10171  | 조건검색 목록조회         | 국내주식     | 조건검색   | /api/dostk/websocket | [ka10171_조건검색_목록조회.md](APIs/ka10171_조건검색_목록조회.md)                 |
|    96 | ka10172  | 조건검색 요청 일반        | 국내주식     | 조건검색   | /api/dostk/websocket | [ka10172_조건검색_요청_일반.md](APIs/ka10172_조건검색_요청_일반.md)               |
|    97 | ka10173  | 조건검색 요청 실시간       | 국내주식     | 조건검색   | /api/dostk/websocket | [ka10173_조건검색_요청_실시간.md](APIs/ka10173_조건검색_요청_실시간.md)             |
|    98 | ka10174  | 조건검색 실시간 해제       | 국내주식     | 조건검색   | /api/dostk/websocket | [ka10174_조건검색_실시간_해제.md](APIs/ka10174_조건검색_실시간_해제.md)             |
|    99 | ka20001  | 업종현재가요청           | 국내주식     | 업종     | /api/dostk/sect      | [ka20001_업종현재가요청.md](APIs/ka20001_업종현재가요청.md)                     |
|   100 | ka20002  | 업종별주가요청           | 국내주식     | 업종     | /api/dostk/sect      | [ka20002_업종별주가요청.md](APIs/ka20002_업종별주가요청.md)                     |
|   101 | ka20003  | 전업종지수요청           | 국내주식     | 업종     | /api/dostk/sect      | [ka20003_전업종지수요청.md](APIs/ka20003_전업종지수요청.md)                     |
|   102 | ka20004  | 업종틱차트조회요청         | 국내주식     | 차트     | /api/dostk/chart     | [ka20004_업종틱차트조회요청.md](APIs/ka20004_업종틱차트조회요청.md)                 |
|   103 | ka20005  | 업종분봉조회요청          | 국내주식     | 차트     | /api/dostk/chart     | [ka20005_업종분봉조회요청.md](APIs/ka20005_업종분봉조회요청.md)                   |
|   104 | ka20006  | 업종일봉조회요청          | 국내주식     | 차트     | /api/dostk/chart     | [ka20006_업종일봉조회요청.md](APIs/ka20006_업종일봉조회요청.md)                   |
|   105 | ka20007  | 업종주봉조회요청          | 국내주식     | 차트     | /api/dostk/chart     | [ka20007_업종주봉조회요청.md](APIs/ka20007_업종주봉조회요청.md)                   |
|   106 | ka20008  | 업종월봉조회요청          | 국내주식     | 차트     | /api/dostk/chart     | [ka20008_업종월봉조회요청.md](APIs/ka20008_업종월봉조회요청.md)                   |
|   107 | ka20009  | 업종현재가일별요청         | 국내주식     | 업종     | /api/dostk/sect      | [ka20009_업종현재가일별요청.md](APIs/ka20009_업종현재가일별요청.md)                 |
|   108 | ka20019  | 업종년봉조회요청          | 국내주식     | 차트     | /api/dostk/chart     | [ka20019_업종년봉조회요청.md](APIs/ka20019_업종년봉조회요청.md)                   |
|   109 | ka20068  | 대차거래추이요청(종목별)     | 국내주식     | 대차거래   | /api/dostk/slb       | [ka20068_대차거래추이요청(종목별).md](APIs/ka20068_대차거래추이요청(종목별).md)         |
|   110 | ka30001  | ELW가격급등락요청        | 국내주식     | ELW    | /api/dostk/elw       | [ka30001_ELW가격급등락요청.md](APIs/ka30001_ELW가격급등락요청.md)               |
|   111 | ka30002  | 거래원별ELW순매매상위요청    | 국내주식     | ELW    | /api/dostk/elw       | [ka30002_거래원별ELW순매매상위요청.md](APIs/ka30002_거래원별ELW순매매상위요청.md)       |
|   112 | ka30003  | ELWLP보유일별추이요청     | 국내주식     | ELW    | /api/dostk/elw       | [ka30003_ELWLP보유일별추이요청.md](APIs/ka30003_ELWLP보유일별추이요청.md)         |
|   113 | ka30004  | ELW괴리율요청          | 국내주식     | ELW    | /api/dostk/elw       | [ka30004_ELW괴리율요청.md](APIs/ka30004_ELW괴리율요청.md)                   |
|   114 | ka30005  | ELW조건검색요청         | 국내주식     | ELW    | /api/dostk/elw       | [ka30005_ELW조건검색요청.md](APIs/ka30005_ELW조건검색요청.md)                 |
|   115 | ka30009  | ELW등락율순위요청        | 국내주식     | ELW    | /api/dostk/elw       | [ka30009_ELW등락율순위요청.md](APIs/ka30009_ELW등락율순위요청.md)               |
|   116 | ka30010  | ELW잔량순위요청         | 국내주식     | ELW    | /api/dostk/elw       | [ka30010_ELW잔량순위요청.md](APIs/ka30010_ELW잔량순위요청.md)                 |
|   117 | ka30011  | ELW근접율요청          | 국내주식     | ELW    | /api/dostk/elw       | [ka30011_ELW근접율요청.md](APIs/ka30011_ELW근접율요청.md)                   |
|   118 | ka30012  | ELW종목상세정보요청       | 국내주식     | ELW    | /api/dostk/elw       | [ka30012_ELW종목상세정보요청.md](APIs/ka30012_ELW종목상세정보요청.md)             |
|   119 | ka40001  | ETF수익율요청          | 국내주식     | ETF    | /api/dostk/etf       | [ka40001_ETF수익율요청.md](APIs/ka40001_ETF수익율요청.md)                   |
|   120 | ka40002  | ETF종목정보요청         | 국내주식     | ETF    | /api/dostk/etf       | [ka40002_ETF종목정보요청.md](APIs/ka40002_ETF종목정보요청.md)                 |
|   121 | ka40003  | ETF일별추이요청         | 국내주식     | ETF    | /api/dostk/etf       | [ka40003_ETF일별추이요청.md](APIs/ka40003_ETF일별추이요청.md)                 |
|   122 | ka40004  | ETF전체시세요청         | 국내주식     | ETF    | /api/dostk/etf       | [ka40004_ETF전체시세요청.md](APIs/ka40004_ETF전체시세요청.md)                 |
|   123 | ka40006  | ETF시간대별추이요청       | 국내주식     | ETF    | /api/dostk/etf       | [ka40006_ETF시간대별추이요청.md](APIs/ka40006_ETF시간대별추이요청.md)             |
|   124 | ka40007  | ETF시간대별체결요청       | 국내주식     | ETF    | /api/dostk/etf       | [ka40007_ETF시간대별체결요청.md](APIs/ka40007_ETF시간대별체결요청.md)             |
|   125 | ka40008  | ETF일자별체결요청        | 국내주식     | ETF    | /api/dostk/etf       | [ka40008_ETF일자별체결요청.md](APIs/ka40008_ETF일자별체결요청.md)               |
|   126 | ka40009  | ETF시간대별체결요청       | 국내주식     | ETF    | /api/dostk/etf       | [ka40009_ETF시간대별체결요청.md](APIs/ka40009_ETF시간대별체결요청.md)             |
|   127 | ka40010  | ETF시간대별추이요청       | 국내주식     | ETF    | /api/dostk/etf       | [ka40010_ETF시간대별추이요청.md](APIs/ka40010_ETF시간대별추이요청.md)             |
|   128 | ka50010  | 금현물체결추이           | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka50010_금현물체결추이.md](APIs/ka50010_금현물체결추이.md)                     |
|   129 | ka50012  | 금현물일별추이           | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka50012_금현물일별추이.md](APIs/ka50012_금현물일별추이.md)                     |
|   130 | ka50079  | 금현물틱차트조회요청        | 국내주식     | 차트     | /api/dostk/chart     | [ka50079_금현물틱차트조회요청.md](APIs/ka50079_금현물틱차트조회요청.md)               |
|   131 | ka50080  | 금현물분봉차트조회요청       | 국내주식     | 차트     | /api/dostk/chart     | [ka50080_금현물분봉차트조회요청.md](APIs/ka50080_금현물분봉차트조회요청.md)             |
|   132 | ka50081  | 금현물일봉차트조회요청       | 국내주식     | 차트     | /api/dostk/chart     | [ka50081_금현물일봉차트조회요청.md](APIs/ka50081_금현물일봉차트조회요청.md)             |
|   133 | ka50082  | 금현물주봉차트조회요청       | 국내주식     | 차트     | /api/dostk/chart     | [ka50082_금현물주봉차트조회요청.md](APIs/ka50082_금현물주봉차트조회요청.md)             |
|   134 | ka50083  | 금현물월봉차트조회요청       | 국내주식     | 차트     | /api/dostk/chart     | [ka50083_금현물월봉차트조회요청.md](APIs/ka50083_금현물월봉차트조회요청.md)             |
|   135 | ka50087  | 금현물예상체결           | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka50087_금현물예상체결.md](APIs/ka50087_금현물예상체결.md)                     |
|   136 | ka50091  | 금현물당일틱차트조회요청      | 국내주식     | 차트     | /api/dostk/chart     | [ka50091_금현물당일틱차트조회요청.md](APIs/ka50091_금현물당일틱차트조회요청.md)           |
|   137 | ka50092  | 금현물당일분봉차트조회요청     | 국내주식     | 차트     | /api/dostk/chart     | [ka50092_금현물당일분봉차트조회요청.md](APIs/ka50092_금현물당일분봉차트조회요청.md)         |
|   138 | ka50100  | 금현물 시세정보          | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka50100_금현물_시세정보.md](APIs/ka50100_금현물_시세정보.md)                   |
|   139 | ka50101  | 금현물 호가            | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka50101_금현물_호가.md](APIs/ka50101_금현물_호가.md)                       |
|   140 | ka52301  | 금현물투자자현황          | 국내주식     | 기관/외국인 | /api/dostk/frgnistt  | [ka52301_금현물투자자현황.md](APIs/ka52301_금현물투자자현황.md)                   |
|   141 | ka90001  | 테마그룹별요청           | 국내주식     | 테마     | /api/dostk/thme      | [ka90001_테마그룹별요청.md](APIs/ka90001_테마그룹별요청.md)                     |
|   142 | ka90002  | 테마구성종목요청          | 국내주식     | 테마     | /api/dostk/thme      | [ka90002_테마구성종목요청.md](APIs/ka90002_테마구성종목요청.md)                   |
|   143 | ka90003  | 프로그램순매수상위50요청     | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka90003_프로그램순매수상위50요청.md](APIs/ka90003_프로그램순매수상위50요청.md)         |
|   144 | ka90004  | 종목별프로그램매매현황요청     | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [ka90004_종목별프로그램매매현황요청.md](APIs/ka90004_종목별프로그램매매현황요청.md)         |
|   145 | ka90005  | 프로그램매매추이요청 시간대별   | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka90005_프로그램매매추이요청_시간대별.md](APIs/ka90005_프로그램매매추이요청_시간대별.md)     |
|   146 | ka90006  | 프로그램매매차익잔고추이요청    | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka90006_프로그램매매차익잔고추이요청.md](APIs/ka90006_프로그램매매차익잔고추이요청.md)       |
|   147 | ka90007  | 프로그램매매누적추이요청      | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka90007_프로그램매매누적추이요청.md](APIs/ka90007_프로그램매매누적추이요청.md)           |
|   148 | ka90008  | 종목시간별프로그램매매추이요청   | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka90008_종목시간별프로그램매매추이요청.md](APIs/ka90008_종목시간별프로그램매매추이요청.md)     |
|   149 | ka90009  | 외국인기관매매상위요청       | 국내주식     | 순위정보   | /api/dostk/rkinfo    | [ka90009_외국인기관매매상위요청.md](APIs/ka90009_외국인기관매매상위요청.md)             |
|   150 | ka90010  | 프로그램매매추이요청 일자별    | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka90010_프로그램매매추이요청_일자별.md](APIs/ka90010_프로그램매매추이요청_일자별.md)       |
|   151 | ka90012  | 대차거래내역요청          | 국내주식     | 대차거래   | /api/dostk/slb       | [ka90012_대차거래내역요청.md](APIs/ka90012_대차거래내역요청.md)                   |
|   152 | ka90013  | 종목일별프로그램매매추이요청    | 국내주식     | 시세     | /api/dostk/mrkcond   | [ka90013_종목일별프로그램매매추이요청.md](APIs/ka90013_종목일별프로그램매매추이요청.md)       |
|   153 | kt00001  | 예수금상세현황요청         | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00001_예수금상세현황요청.md](APIs/kt00001_예수금상세현황요청.md)                 |
|   154 | kt00002  | 일별추정예탁자산현황요청      | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00002_일별추정예탁자산현황요청.md](APIs/kt00002_일별추정예탁자산현황요청.md)           |
|   155 | kt00003  | 추정자산조회요청          | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00003_추정자산조회요청.md](APIs/kt00003_추정자산조회요청.md)                   |
|   156 | kt00004  | 계좌평가현황요청          | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00004_계좌평가현황요청.md](APIs/kt00004_계좌평가현황요청.md)                   |
|   157 | kt00005  | 체결잔고요청            | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00005_체결잔고요청.md](APIs/kt00005_체결잔고요청.md)                       |
|   158 | kt00007  | 계좌별주문체결내역상세요청     | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00007_계좌별주문체결내역상세요청.md](APIs/kt00007_계좌별주문체결내역상세요청.md)         |
|   159 | kt00008  | 계좌별익일결제예정내역요청     | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00008_계좌별익일결제예정내역요청.md](APIs/kt00008_계좌별익일결제예정내역요청.md)         |
|   160 | kt00009  | 계좌별주문체결현황요청       | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00009_계좌별주문체결현황요청.md](APIs/kt00009_계좌별주문체결현황요청.md)             |
|   161 | kt00010  | 주문인출가능금액요청        | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00010_주문인출가능금액요청.md](APIs/kt00010_주문인출가능금액요청.md)               |
|   162 | kt00011  | 증거금율별주문가능수량조회요청   | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00011_증거금율별주문가능수량조회요청.md](APIs/kt00011_증거금율별주문가능수량조회요청.md)     |
|   163 | kt00012  | 신용보증금율별주문가능수량조회요청 | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00012_신용보증금율별주문가능수량조회요청.md](APIs/kt00012_신용보증금율별주문가능수량조회요청.md) |
|   164 | kt00013  | 증거금세부내역조회요청       | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00013_증거금세부내역조회요청.md](APIs/kt00013_증거금세부내역조회요청.md)             |
|   165 | kt00015  | 위탁종합거래내역요청        | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00015_위탁종합거래내역요청.md](APIs/kt00015_위탁종합거래내역요청.md)               |
|   166 | kt00016  | 일별계좌수익률상세현황요청     | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00016_일별계좌수익률상세현황요청.md](APIs/kt00016_일별계좌수익률상세현황요청.md)         |
|   167 | kt00017  | 계좌별당일현황요청         | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00017_계좌별당일현황요청.md](APIs/kt00017_계좌별당일현황요청.md)                 |
|   168 | kt00018  | 계좌평가잔고내역요청        | 국내주식     | 계좌     | /api/dostk/acnt      | [kt00018_계좌평가잔고내역요청.md](APIs/kt00018_계좌평가잔고내역요청.md)               |
|   169 | kt10000  | 주식 매수주문           | 국내주식     | 주문     | /api/dostk/ordr      | [kt10000_주식_매수주문.md](APIs/kt10000_주식_매수주문.md)                     |
|   170 | kt10001  | 주식 매도주문           | 국내주식     | 주문     | /api/dostk/ordr      | [kt10001_주식_매도주문.md](APIs/kt10001_주식_매도주문.md)                     |
|   171 | kt10002  | 주식 정정주문           | 국내주식     | 주문     | /api/dostk/ordr      | [kt10002_주식_정정주문.md](APIs/kt10002_주식_정정주문.md)                     |
|   172 | kt10003  | 주식 취소주문           | 국내주식     | 주문     | /api/dostk/ordr      | [kt10003_주식_취소주문.md](APIs/kt10003_주식_취소주문.md)                     |
|   173 | kt10006  | 신용 매수주문           | 국내주식     | 신용주문   | /api/dostk/crdordr   | [kt10006_신용_매수주문.md](APIs/kt10006_신용_매수주문.md)                     |
|   174 | kt10007  | 신용 매도주문           | 국내주식     | 신용주문   | /api/dostk/crdordr   | [kt10007_신용_매도주문.md](APIs/kt10007_신용_매도주문.md)                     |
|   175 | kt10008  | 신용 정정주문           | 국내주식     | 신용주문   | /api/dostk/crdordr   | [kt10008_신용_정정주문.md](APIs/kt10008_신용_정정주문.md)                     |
|   176 | kt10009  | 신용 취소주문           | 국내주식     | 신용주문   | /api/dostk/crdordr   | [kt10009_신용_취소주문.md](APIs/kt10009_신용_취소주문.md)                     |
|   177 | kt20016  | 신용융자 가능종목요청       | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [kt20016_신용융자_가능종목요청.md](APIs/kt20016_신용융자_가능종목요청.md)             |
|   178 | kt20017  | 신용융자 가능문의         | 국내주식     | 종목정보   | /api/dostk/stkinfo   | [kt20017_신용융자_가능문의.md](APIs/kt20017_신용융자_가능문의.md)                 |
|   179 | kt50000  | 금현물 매수주문          | 국내주식     | 주문     | /api/dostk/ordr      | [kt50000_금현물_매수주문.md](APIs/kt50000_금현물_매수주문.md)                   |
|   180 | kt50001  | 금현물 매도주문          | 국내주식     | 주문     | /api/dostk/ordr      | [kt50001_금현물_매도주문.md](APIs/kt50001_금현물_매도주문.md)                   |
|   181 | kt50002  | 금현물 정정주문          | 국내주식     | 주문     | /api/dostk/ordr      | [kt50002_금현물_정정주문.md](APIs/kt50002_금현물_정정주문.md)                   |
|   182 | kt50003  | 금현물 취소주문          | 국내주식     | 주문     | /api/dostk/ordr      | [kt50003_금현물_취소주문.md](APIs/kt50003_금현물_취소주문.md)                   |
|   183 | kt50020  | 금현물 잔고확인          | 국내주식     | 계좌     | /api/dostk/acnt      | [kt50020_금현물_잔고확인.md](APIs/kt50020_금현물_잔고확인.md)                   |
|   184 | kt50021  | 금현물 예수금           | 국내주식     | 계좌     | /api/dostk/acnt      | [kt50021_금현물_예수금.md](APIs/kt50021_금현물_예수금.md)                     |
|   185 | kt50030  | 금현물 주문체결전체조회      | 국내주식     | 계좌     | /api/dostk/acnt      | [kt50030_금현물_주문체결전체조회.md](APIs/kt50030_금현물_주문체결전체조회.md)           |
|   186 | kt50031  | 금현물 주문체결조회        | 국내주식     | 계좌     | /api/dostk/acnt      | [kt50031_금현물_주문체결조회.md](APIs/kt50031_금현물_주문체결조회.md)               |
|   187 | kt50032  | 금현물 거래내역조회        | 국내주식     | 계좌     | /api/dostk/acnt      | [kt50032_금현물_거래내역조회.md](APIs/kt50032_금현물_거래내역조회.md)               |
|   188 | kt50075  | 금현물 미체결조회         | 국내주식     | 계좌     | /api/dostk/acnt      | [kt50075_금현물_미체결조회.md](APIs/kt50075_금현물_미체결조회.md)                 |
|   189 | 00       | 주문체결              | 국내주식     | 실시간시세  | /api/dostk/websocket | [00_주문체결.md](APIs/00_주문체결.md)                                     |
|   190 | 04       | 잔고                | 국내주식     | 실시간시세  | /api/dostk/websocket | [04_잔고.md](APIs/04_잔고.md)                                         |
|   191 | 0A       | 주식기세              | 국내주식     | 실시간시세  | /api/dostk/websocket | [0A_주식기세.md](APIs/0A_주식기세.md)                                     |
|   192 | 0B       | 주식체결              | 국내주식     | 실시간시세  | /api/dostk/websocket | [0B_주식체결.md](APIs/0B_주식체결.md)                                     |
|   193 | 0C       | 주식우선호가            | 국내주식     | 실시간시세  | /api/dostk/websocket | [0C_주식우선호가.md](APIs/0C_주식우선호가.md)                                 |
|   194 | 0D       | 주식호가잔량            | 국내주식     | 실시간시세  | /api/dostk/websocket | [0D_주식호가잔량.md](APIs/0D_주식호가잔량.md)                                 |
|   195 | 0E       | 주식시간외호가           | 국내주식     | 실시간시세  | /api/dostk/websocket | [0E_주식시간외호가.md](APIs/0E_주식시간외호가.md)                               |
|   196 | 0F       | 주식당일거래원           | 국내주식     | 실시간시세  | /api/dostk/websocket | [0F_주식당일거래원.md](APIs/0F_주식당일거래원.md)                               |
|   197 | 0G       | ETF NAV           | 국내주식     | 실시간시세  | /api/dostk/websocket | [0G_ETF_NAV.md](APIs/0G_ETF_NAV.md)                               |
|   198 | 0H       | 주식예상체결            | 국내주식     | 실시간시세  | /api/dostk/websocket | [0H_주식예상체결.md](APIs/0H_주식예상체결.md)                                 |
|   199 | 0I       | 국제금환산가격           | 국내주식     | 실시간시세  | /api/dostk/websocket | [0I_국제금환산가격.md](APIs/0I_국제금환산가격.md)                               |
|   200 | 0J       | 업종지수              | 국내주식     | 실시간시세  | /api/dostk/websocket | [0J_업종지수.md](APIs/0J_업종지수.md)                                     |
|   201 | 0U       | 업종등락              | 국내주식     | 실시간시세  | /api/dostk/websocket | [0U_업종등락.md](APIs/0U_업종등락.md)                                     |
|   202 | 0g       | 주식종목정보            | 국내주식     | 실시간시세  | /api/dostk/websocket | [0g_주식종목정보.md](APIs/0g_주식종목정보.md)                                 |
|   203 | 0m       | ELW 이론가           | 국내주식     | 실시간시세  | /api/dostk/websocket | [0m_ELW_이론가.md](APIs/0m_ELW_이론가.md)                               |
|   204 | 0s       | 장시작시간             | 국내주식     | 실시간시세  | /api/dostk/websocket | [0s_장시작시간.md](APIs/0s_장시작시간.md)                                   |
|   205 | 0u       | ELW 지표            | 국내주식     | 실시간시세  | /api/dostk/websocket | [0u_ELW_지표.md](APIs/0u_ELW_지표.md)                                 |
|   206 | 0w       | 종목프로그램매매          | 국내주식     | 실시간시세  | /api/dostk/websocket | [0w_종목프로그램매매.md](APIs/0w_종목프로그램매매.md)                             |
|   207 | 1h       | VI발동/해제           | 국내주식     | 실시간시세  | /api/dostk/websocket | [1h_VI발동_해제.md](APIs/1h_VI발동_해제.md)                               |

---

# 오류코드

## 1. 오류코드 안내
* API 요청 결과로 변환할 수 있는 주요 오류코드 안내입니다.
* `{?}` 는 호출 시 사용된 값이나 시스템에서 반환된 상세 사유를 나타냅니다.
* API 가이드 내 'EXCEL, PDF 명세서 다운로드'를 통해 오류코드 문서를 확인하실 수 있습니다.

## 2. API 서버 오류코드

| 오류코드 | 내용 |
| :--- | :--- |
| **1501** | API ID가 Null이거나 값이 없습니다 |
| **1504** | 해당 URI에서는 지원하는 API ID가 아닙니다. API ID={?}, URI={?} |
| **1505** | 해당 API ID는 존재하지 않습니다. API ID={?} |
| **1511** | 필수 입력 값에 값이 존재하지 않습니다. 필수입력 파라미터={?} |
| **1512** | Http header에 값이 설정되지 않았거나 읽을 수 없습니다 |
| **1513** | Http Header에 authorization 필드가 설정되어 있어야 합니다 |
| **1514** | 입력으로 들어온 Http Header의 authorization 필드 형식이 맞지 않습니다 |
| **1515** | Http Header의 authorization 필드 내 Grant Type이 미리 정의된 형식이 아닙니다 |
| **1516** | Http Header의 authorization 필드 내 Token이 정의되어 있지 않습니다 |
| **1517** | 입력 값 형식이 올바르지 않습니다. 파라미터={?} 실패사유= {?} |
| **1687** | 재귀 호출이 발생하여 API 호출을 제한합니다, API ID={?} |
| **1700** | 허용된 요청 개수를 초과하였습니다. API ID={?} |
| **1901** | 시장 코드값이 존재하지 않습니다. 종목코드={?} |
| **1902** | 종목 정보가 없습니다. 입력한 종목코드 값을 확인바랍니다. 종목코드={?} |
| **1999** | 예기치 못한 에러가 발생했습니다. 실패사유={?} |
| **8001** | App Key와 Secret Key 검증에 실패했습니다 |
| **8002** | App Key와 Secret Key 검증에 실패했습니다. 실패사유={?} |
| **8003** | Access Token을 조회하는데 실패했습니다. 실패사유={?} |
| **8005** | Token이 유효하지 않습니다 |
| **8006** | Access Token을 생성하는데 실패했습니다. 실패사유={?} |
| **8009** | Access Token을 발급하는데 실패했습니다. 실패사유={?} |
| **8010** | Token을 발급받은 IP와 서비스를 요청한 IP가 동일하지 않습니다 |
| **8011** | Access Token을 발급하는데 실패했습니다. 입력값에 grant_type이 들어오지 않았습니다 |
| **8012** | Access Token을 발급하는데 실패했습니다. grant_type의 값이 맞지 않습니다 |
| **8015** | Access Token을 폐기하는데 실패했습니다. 실패사유={?} |
| **8016** | Access Token을 폐기하는데 실패했습니다. 입력값에 Token이 들어오지 않았습니다 |
| **8020** | 입력파라미터로 appkey 또는 secretkey가 들어오지 않았습니다. |
| **8030** | 투자구분(실전/모의)이 달라서 Appkey를 사용할수가 없습니다 |
| **8031** | 투자구분(실전/모의)이 달라서 Token를 사용할수가 없습니다 |
| **8040** | 단말기 인증에 실패했습니다 |
| **8050** | 지정단말기 인증에 실패했습니다 |
| **8103** | 토큰 인증 또는 단말기인증에 실패했습니다. 실패사유={?} |