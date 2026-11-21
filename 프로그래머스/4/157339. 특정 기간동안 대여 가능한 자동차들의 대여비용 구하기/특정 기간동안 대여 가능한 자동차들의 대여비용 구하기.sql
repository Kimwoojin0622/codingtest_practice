# 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기

# 테이블 1 - CAR_RENTAL_COMPANY_CAR (대여 중인 자동차들의 정보)
  # 자동차 ID, 자동차 종류, 일일 대여 요금, 자동차 옵션 리스트
  # 1, 세단, 25000, 가죽시트/열선시트
  
# 테이블 2 - CAR_RENTAL_COMPANY_RENTAL_HISTORY (자동차 대여 기록 정보)
  # 자동차 대여 기록 ID, 자동차 ID, 대여 시작일, 대여 종료일
  # 1, 1, 2022-07-27, 2022-09-02
  
# 테이블 3 - CAR_RENTAL_COMPANY_DISCOUNT_PLAN (자동차 종류 별 대여 기간 종류 별 할인 정책)
  # 요금 할인 정책 ID, 자동차 종류, 대여 기간 종류, 할인율(%)
  # 1, 트럭, 7일 이상, 5%
  
# 문제 : 자동차 종류가 '세단' 또는 'SUV'인 자동차 중 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 자동차 ID, 자동차 종류, 대여 금액 (FEE) 리스트를 출력하는 SQL문 작성

# 결과는 대여 금액을 기준으로 내림차순 정렬, 대여 금액이 같을 경우 자동차 종류를 기준으로 오름차순 정렬, 자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬

# 1. 2022년 11월 1일부터 2022년 11월 30일까지 빌릴 수 있는 차량을 선별하기 위해, CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 END_DATE가 2022년 11월 1일보다 크거나, 작은 CAR_ID들을 DISTINCT를 통해 중복을 제거하고 추출
# 2022년 11월 1일 ~ 2022년 11월 30일까지 빌릴 수 없는 26, 13 등의 CAR_ID 등이 존재.

# 2. 다시 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블을 활용해서 WHERE 절에 #1번에서 구했던 기간 내 빌릴 수 없는 CAR_ID 들을 NOT IN을 통해 제거
# 26, 13 등 기간 내 빌릴 수 없는 CAR_ID를 제거

# 3. CAR_TYPE에 대한 조건도 걸어야 되기 때문에, CAR_RENTAL_COMPANY_CAR와 JOIN을 진행. 진행 시에는 CAR_ID 컬럼을 기준으로 JOIN을 진행

# 4. JOIN을 한 뒤, CAR_TYPE이 'SUV'와 '세단'인 차량만 추출하게끔 IN 연산자를 사용

# 5. 30일 동안의 할인율을 포함한 차량 대여 금액 FEE 컬럼을 만들기 위해 CAR_RENTAL_COMPANY_DISCOUNT_PLAN과도 JOIN을 진행. 진행 시에는 CAR_RENTAL_COMPANY_CAR에 있는 CAR_TYPE 컬럼을 기준으로 JOIN을 진행하되, AND 연산자를 활용해서 '30일 이상'의 할인율만 가져오게끔 적용

# 6. 이후 일일 대여 요금과 할인 요금인 DISCOUNT_RATE를 곱하고 30일 일수를 곱한 FEE 컬럼을 만듦. 하지만 조건에서 FEE 컬럼의 값이 50만원 이상 200만원 이하를 요구하고 있기 때문에, WHERE절에서 BETWEEN을 통해 50만원 이상 200만원 이하의 데이터만 추출

# 7. CAR_ID의 값이 여러개 중복된 데이터가 존재했기 때문에, 하나의 자동차만 뜨게끔 CAR_ID에 DISTINCT를 활용해서 중복을 제거

# 8. 마지막으로는 대여 금액을 기준으로 내림차순 정렬, 자동차 종류를 기준으로 오름차순 정렬, 자동차 ID를 기준으로 내림차순 정렬을 진행

SELECT DISTINCT CRCRH.CAR_ID
     , CRCC.CAR_TYPE
     , (CRCC.DAILY_FEE * (1 - (CRCDP.DISCOUNT_RATE * 0.01))) * 30 AS 'FEE'
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS CRCRH
  LEFT JOIN CAR_RENTAL_COMPANY_CAR AS CRCC ON CRCRH.CAR_ID = CRCC.CAR_ID
  LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS CRCDP ON CRCC.CAR_TYPE = CRCDP.CAR_TYPE
        AND CRCDP.DURATION_TYPE = '30일 이상'
WHERE CRCRH.CAR_ID NOT IN (
    SELECT DISTINCT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE >= '2022-11-01'
)
  AND CRCC.CAR_TYPE IN ('SUV', '세단')
  AND (CRCC.DAILY_FEE * (1 - (CRCDP.DISCOUNT_RATE * 0.01))) * 30 BETWEEN 500000 AND 2000000
ORDER BY FEE DESC, CRCC.CAR_TYPE ASC, CRCRH.CAR_ID DESC;