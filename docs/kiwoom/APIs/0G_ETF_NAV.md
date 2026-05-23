# ETF NAV (0G)

## 1. 기본 정보
- **메뉴 위치**: 국내주식 > 실시간시세 > ETF NAV(0G)
- **API 명**: ETF NAV
- **API ID**: 0G
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
  - **36** (String, , 선택): NAV
  - **37** (String, , 선택): NAV전일대비
  - **38** (String, , 선택): NAV등락율
  - **39** (String, , 선택): 추적오차율
  - **20** (String, , 선택): 체결시간
  - **10** (String, , 선택): 현재가
  - **11** (String, , 선택): 전일대비
  - **12** (String, , 선택): 등락율
  - **13** (String, , 선택): 누적거래량
  - **25** (String, , 선택): 전일대비기호
  - **667** (String, , 선택): ELW기어링비율
  - **668** (String, , 선택): ELW손익분기율
  - **669** (String, , 선택): ELW자본지지점
  - **265** (String, , 선택): NAV/지수괴리율
  - **266** (String, , 선택): NAV/ETF괴리율

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
                "069500"
            ],
            "type": [
                "0G"
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
                '36': '+7488.27',
                '37': '+9.57',
                '38': '+0.13',
                '39': '1.82',
                '20': '105732',
                '10': '+7485',
                '11': '+45',
                '12': '+0.60',
                '13': '16874',
                '25': '2',
                '265': '+10.04',
                '266': '-0.04'
            },
            'type': '0G',
            'name': 'ETF NAV',
            'item': '069500'
        }
    ],
    'trnm': 'REAL'
}
```

