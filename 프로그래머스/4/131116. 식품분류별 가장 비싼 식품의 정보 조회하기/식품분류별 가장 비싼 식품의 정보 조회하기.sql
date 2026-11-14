# 식품분류별 가장 비싼 식품의 정보 조회하기

# 테이블 정보
# -> FOOD_PRODUCT 테이블이 있고, 식품 ID / 식품 이름 / 식품 분류 / 식품 가격 등이 존재합니다.

# 문제
# FOOD_PRODUCT 테이블에서 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회
# 이 때, 식품 분류가 '과자','국','김치','식용유'인 경우만 출력시키고, 결과는 식품 가격을 기준으로 내림차순을 진행해야한다!

# 1. FOOD_PRODUCT에 대해서 식품분류별 제일 비싼 가격을 구하기 위해서 서브쿼리에 위치해있는 쿼리문을 작성하였습니다.
# 2. CATEGORY 별로 GROUP BY를 진행하였고, 그 전에 CATEGORY에는 '과자', '국', '김치', '식용유'만 나타내어야 하기 때문에, WHERE절에 IN을 통해서 조건을 붙였습니다. 그리고 SELECT 문에 집계함수 MAX()를 활용해서 최대값을 구했습니다.
# 3. 이렇게 만든 식품분류별 최고 가격을 나타내는 가상의 테이블을 만들었고, 이를 WHERE절에 활용해서 다중행 서브쿼리를 작성했습니다. 가상의 테이블에서 만든 식품분류와 최고 가격이 일치한 행만 나오도록 작성했습니다.
# 4. 마지막으로는 가격 기준으로 내림차순을 진행해야하기 때문에, ORDER BY절에서 내림차순을 진행했습니다.

SELECT CATEGORY
     , PRICE AS 'MAX_PRICE'
     , PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) IN (
    SELECT CATEGORY
         , MAX(PRICE) AS 'CATEGORY_MAX'
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자','국','김치','식용유')
    GROUP BY CATEGORY) # 다중행 서브쿼리
ORDER BY PRICE DESC;