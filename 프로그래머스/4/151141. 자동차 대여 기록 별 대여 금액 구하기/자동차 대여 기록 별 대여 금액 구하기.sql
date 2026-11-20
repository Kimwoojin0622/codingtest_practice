# 자동차 대여 기록 별 대여 금액 구하기

# 테이블 1 - CAR_REATAL_COMPANY_CAR (대여 중인 자동차들의 정보)
  # 자동차 ID, 자동차 종류, 일일 대여 요금, 자동차 옵션 리스트
  # 자동차 종류(세단, SUV, 승합차, 트럭, 리무진)
  
# 테이블 2 - CAR_RENTAL_COMPANY_RENTAL_HISTORY (자동차 대여 기록 정보)
  # 자동차 대여 기록 ID, 자동차 ID, 대여 시작일, 대여 종료일
  
# 테이블 3 - CAR_RENTAL_COMPANY_DISCOUNT_PLAN (대여 기간 종류 별 할인 정책 정보)
  # 요금 할인 정책 ID, 자동차 종류, 대여 기간 종류, 할인율(%)
  # 7일 이상 30일 미만 -> 7일 이상
  # 30일 이상 90일 미만 -> 30일 이상
  # 90일 이상 -> 90일 이상
  # 7일 미만 -> 할인 X
  
# 문제 : 3개의 테이블을 활용하여 자동차 종류가 '트럭'인 자동차의 대여 기록에 대해서 대여 기록 별로 대여 금액(FEE)을 구하여 대여 기록 ID와 대여 금액 리스트를 출력하는 SQL문 작성
# 결과는 대여 금액을 기준으로 내림차순 정렬, 대여 금액이 같은 경우 대여 기록 ID를 기준으로 내림차순 정렬

# 1. 처음은 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_CAR 테이블을 활용하여 각 HISTORY ID 별 차량을 빌린 날짜를 DATEDIFF 함수를 통해 구하고, DATEDIFF 값에 따라 7일 미만, 7일 이상, 30일 이상, 90일 이상을 정하는 CASE WHEN 문을 작성하고 CONDITION을 컬럼명으로 정함

# 2. 또한 트럭에 관한 값만 원했기 때문에, WHERE절에서 CAR_TYPE을 트럭으로 하는 조건절

# 3. 이를 기반으로 FEE를 구하려고 했기 때문에, CTE를 사용해서 NEW_TABLE이라는 테이블을 생성

# 4. 생성된 NEW_TABLE과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블을 JOIN을 진행. NEW_TABLE의 CONDITION과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN의 DURATION_TYPE을 기준으로 하여 JOIN을 진행하고, 트럭만 가져와야 되기 때문에 AND절을 활용하여 CAR_TYPE도 '트럭'으로 일치한 부분만 JOIN 진행

# 5. CASE WHEN 문을 사용해서 만약 CAR_RENTAL_COMPANY_DISCOUNT_PLAN의 DISCOUNT_RATE 부분이 NULL이라면 7일 미만이기 때문에 이럴 경우에는 DAILY_FEE와 대여 일수 DATE 컬럼을 곱함

# 6. 하지만 7일 미만이 아닌 경우에는 할인율을 곱해야되기 때문에, 1 - DISCOUNT_RATE * 0.01을 해서 5%면 0.95를 DAILY_FEE와 곱하게끔 만들고, 마지막으로는 대여 일수 DATE 컬럼을 곱함

# 7. 최종적으로는 요금을 기준으로 내림차순을 진행하고, 동일하다면 대여 기록을 기준으로 내림차순을 진행

WITH NEW_TABLE AS (
    SELECT CRCRH.HISTORY_ID
         , CRCRH.CAR_ID
         , CRCC.CAR_TYPE
         , CRCC.DAILY_FEE
         , DATEDIFF(END_DATE, START_DATE) + 1 AS 'DATE'
         , CASE
               WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 7 THEN '7일 미만'
               WHEN DATEDIFF(END_DATE, START_DATE) + 1 BETWEEN 7 AND 29 THEN '7일 이상'
               WHEN DATEDIFF(END_DATE, START_DATE) + 1 BETWEEN 30 AND 89 THEN '30일 이상'
               ELSE '90일 이상'
           END AS 'CONDITION'
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS CRCRH
      LEFT JOIN CAR_RENTAL_COMPANY_CAR AS CRCC ON CRCRH.CAR_ID = CRCC.CAR_ID
    WHERE CRCC.CAR_TYPE = '트럭'
)

SELECT NT.HISTORY_ID
     , CASE
            WHEN DISCOUNT_RATE IS NULL THEN DAILY_FEE * DATE
            WHEN DISCOUNT_RATE IS NOT NULL THEN FLOOR((DAILY_FEE * (1 - DISCOUNT_RATE * 0.01)) * DATE)
       END AS 'FEE'
FROM NEW_TABLE AS NT
  LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS CRCDP ON NT.CONDITION = CRCDP.DURATION_TYPE
        AND NT.CAR_TYPE = CRCDP.CAR_TYPE
ORDER BY FEE DESC, NT.HISTORY_ID DESC;