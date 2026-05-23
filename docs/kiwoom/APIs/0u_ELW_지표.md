# ELW 지표 (0u)

## 1. 기본 정보
- **메뉴 위치**: 국내주식 > 실시간시세 > ELW 지표(0u)
- **API 명**: ELW 지표
- **API ID**: 0u
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
  - **20** (String, , 선택): 체결시간
  - **666** (String, , 선택): ELW패리티
  - **1211** (String, , 선택): ELW프리미엄
  - **667** (String, , 선택): ELW기어링비율
  - **668** (String, , 선택): ELW손익분기율
  - **669** (String, , 선택): ELW자본지지점

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
                "57JBHH"
            ],
            "type": [
                "0u"
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
                '20': '111847',
                '666': '69.13',
                '1211': '0',
                '667': '1037.04',
                '668': '+44.73',
                '669': '+44.78'
            },
            'type': '0u',
            'name': 'ELW 지표',
            'item': '57JBHH'
        }
    ],
    'trnm': 'REAL'
}
```

