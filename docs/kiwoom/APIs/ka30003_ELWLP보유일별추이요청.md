# ELWLP보유일별추이요청 (ka30003)

## 1. 기본 정보
- **메뉴 위치**: 국내주식 > ELW > ELWLP보유일별추이요청(ka30003)
- **API 명**: ELWLP보유일별추이요청
- **API ID**: ka30003
- **Method**: POST
- **운영 도메인**: `https://api.kiwoom.com`
- **모의투자 도메인**: `https://mockapi.kiwoom.com(KRX만 지원가능)`
- **URL**: `/api/dostk/elw`
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
- **bsis_aset_cd** (String, 12, 필수): 기초자산코드
- **base_dt** (String, 8, 필수): 기준일자 (YYYYMMDD)

## 3. Response (응답)

### Header
- **api-id** (String, 10, 필수): TR명
- **cont-yn** (String, 1, 선택): 연속조회여부 (다음 데이터가 있을시 Y값 전달)
- **next-key** (String, 50, 선택): 연속조회키 (다음 데이터가 있을시 다음 키값 전달)

### Body
- **elwlpposs_daly_trnsn** (LIST, , 선택): ELWLP보유일별추이
  - **dt** (String, 20, 선택): 일자
  - **cur_prc** (String, 20, 선택): 현재가
  - **pre_tp** (String, 20, 선택): 대비구분
  - **pred_pre** (String, 20, 선택): 전일대비
  - **flu_rt** (String, 20, 선택): 등락율
  - **trde_qty** (String, 20, 선택): 거래량
  - **trde_prica** (String, 20, 선택): 거래대금
  - **chg_qty** (String, 20, 선택): 변동수량
  - **lprmnd_qty** (String, 20, 선택): LP보유수량
  - **wght** (String, 20, 선택): 비중

## 4. 예시 (Examples)

### Request Example
```json
{
    "bsis_aset_cd": "57KJ99",
    "base_dt": "20241122"
}
```

### Response Example
```json
{
    "elwlpposs_daly_trnsn": [
        {
            "dt": "20241122",
            "cur_prc": "-125700",
            "pre_tp": "5",
            "pred_pre": "-900",
            "flu_rt": "-0.71",
            "trde_qty": "54",
            "trde_prica": "7",
            "chg_qty": "0",
            "lprmnd_qty": "0",
            "wght": "0.00"
        }
    ],
    "return_code": 0,
    "return_msg": "정상적으로 처리되었습니다"
}
```

