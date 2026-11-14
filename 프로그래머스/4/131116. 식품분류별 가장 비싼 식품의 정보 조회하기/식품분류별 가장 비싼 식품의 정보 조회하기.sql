# 식품분류별 가장 비싼 식품의 정보 조회하기

# 테이블 정보
# -> FOOD_PRODUCT 테이블이 있고, 식품 ID / 식품 이름 / 식품 분류 / 식품 가격 등이 존재합니다.

# 문제
# FOOD_PRODUCT 테이블에서 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회
# 이 때, 식품 분류가 '과자','국','김치','식용유'인 경우만 출력시키고, 결과는 식품 가격을 기준으로 내림차순을 진행해야한다!

# SELECT CATEGORY
#      , MAX(PRICE) AS 'CATEGORY_MAX'
# FROM FOOD_PRODUCT
# WHERE CATEGORY IN ('과자','국','김치','식용유')
# GROUP BY CATEGORY

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