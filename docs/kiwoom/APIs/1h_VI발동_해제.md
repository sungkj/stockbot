# VI발동/해제 (1h)

## 1. 기본 정보
- **메뉴 위치**: 국내주식 > 실시간시세 > VI발동/해제(1h)
- **API 명**: VI발동/해제
- **API ID**: 1h
- **Method**: POST
- **운영 도메인**: `wss://api.kiwoom.com:10000`
- **모의투자 도메인**: `wss://mockapi.kiwoom.com:10000(KRX만 지원가능)`
- **URL**: `/api/dostk/websocket`
- **Format**: JSON
- **Content-Type**: `application/json;charset=UTF-8`

## 2. Request (요청)

### Header
- **api-id** (String, 10, 필수): TR명
- **authorization** (String, 1000, 필수): 접근토큰 (토큰 지정시 토큰타입("Bearer") 붙혀서 호출 
 예) Bearer Egicyx...)
- **cont-yn** (String, 1, 선택): 연속조회여부 (응답 Header의 연속조회여부값이 Y일 경우 다음데이터 요청시 응답 Header의 cont-yn값 세팅)
- **next-key** (String, 50, 선택): 연속조회키 (응답 Header의 연속조회여부값이 Y일 경우 다음데이터 요청시 응답 Header의 next-key값 세팅)

### Body
- **trnm** (String, 10, 필수): 서비스명 (REG : 등록 , REMOVE : 해지)
- **grp_no** (String, 4, 필수): 그룹번호
- **refresh** (String, 1, 필수): 기존등록유지여부 (등록(REG)시
0:기존유지안함 1:기존유지(Default)
 0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지
해지(REMOVE)시 값 불필요)
- **data** (LIST, , ): 실시간 등록 리스트
- **- item** (String, 100, 선택): 실시간 등록 요소 (거래소별 종목코드, 업종코드
(KRX:039490,NXT:039490_NX,SOR:039490_AL))
- **- type** (String, 2, 필수): 실시간 항목 (TR 명(0A,0B....))

## 3. Response (응답)

### Header
- **api-id** (String, 10, 필수): TR명
- **cont-yn** (String, 1, 선택): 연속조회여부 (다음 데이터가 있을시 Y값 전달)
- **next-key** (String, 50, 선택): 연속조회키 (다음 데이터가 있을시 다음 키값 전달)

### Body
- **return_code** (String, , 선택): 결과코드 (통신결과에대한 코드
(등록,해지요청시에만 값 전송 0:정상,1:오류 , 데이터 실시간 수신시 미전송))
- **return_msg** (String, , 선택): 결과메시지 (통신결과에대한메시지)
- **trnm** (String, , 선택): 서비스명 (등록,해지요청시 요청값 반환 , 실시간수신시 REAL 반환)
- **data** (LIST, , 선택): 실시간 등록리스트
  - **type** (String, , 선택): 실시간항목 (TR 명(0A,0B....))
  - **name** (String, , 선택): 실시간 항목명
  - **item** (String, , 선택): 실시간 등록 요소 (종목코드)
  - **values** (LIST, , 선택): 실시간 값 리스트
  - **9001** (String, , 선택): 종목코드
  - **302** (String, , 선택): 종목명
  - **13** (String, , 선택): 누적거래량
  - **14** (String, , 선택): 누적거래대금
  - **9068** (String, , 선택): VI발동구분
  - **9008** (String, , 선택): KOSPI,KOSDAQ,전체구분
  - **9075** (String, , 선택): 장전구분
  - **1221** (String, , 선택): VI발동가격
  - **1223** (String, , 선택): 매매체결처리시각
  - **1224** (String, , 선택): VI해제시각
  - **1225** (String, , 선택): VI적용구분 (정적/동적/동적+정적)
  - **1236** (String, , 선택): 기준가격 정적 (계약,주)
  - **1237** (String, , 선택): 기준가격 동적
  - **1238** (String, , 선택): 괴리율 정적
  - **1239** (String, , 선택): 괴리율 동적
  - **1489** (String, , 선택): VI발동가 등락율
  - **1490** (String, , 선택): VI발동횟수
  - **9069** (String, , 선택): 발동방향구분
  - **1279** (String, , 선택): Extra Item

## 4. 예시 (Examples)

### Request Example
```json
{
    "trnm": "REG",
    "grp_no": "1",
    "refresh": "1",
    "data": [
        {
            "item": [
                ""
            ],
            "type": [
                "1h"
            ]
        }
    ]
}
```

### Response Example
```json
#요청
{
    'trnm': 'REG',
    'return_code': 0,
    'return_msg': ''
}

#실시간 수신
{
    'data': [
        {
            'values': {
                '9001':'005930',
                '302':'삼성전자',
                '13':'1077818',
                '14':'4201',
                '9068':'1',
                '9008':'101',
                '9075':'1',
                '1221':'4125',
                '1223':'111454',
                '1224':'111703',
                '1225':'정적',
                '1236':'3750',
                '1237':'0',
                '1238':'+10.00',
                '1239':'0.00',
                '1489':'+10.00',
                '1490':'1',
                '9069':'1',
                '1279':'+정적'
            },
            'type':'1h',
            'name':'VI발동/해제',
            'item':'005930'
        }
    ],
    'trnm':'REAL'
}
```

