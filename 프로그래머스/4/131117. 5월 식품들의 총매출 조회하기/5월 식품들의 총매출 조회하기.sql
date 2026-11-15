# 5월 식품들의 총매출 조회하기

# 테이블1 - FOOD_PRODUCT 테이블이 존재합니다. 컬럼은 식품 ID, 식품 이름, 식품 코드, 식품 분류, 식품 가격이 있습니다.

# 테이블2 - FOOD_ORDER 테이블이 존해합니다. 주문 ID, 제품 ID, 주문량, 생산일자, 출고일자 등이 있습니다.

# 문제 : 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회하는 쿼리문을 작성!
# 이 때, 결과는 총매출을 기준으로 내림차순 정렬, 총매출이 같다면 식품 ID를 기준으로 오름차순

# 1. FOOD_ORDER 테이블을 통해 2022년 5월에 생산된 행을 선택
# 2. WHERE 절에 DATE_FORMAT 함수를 사용해서 2022년 5월 관련 데이터를 추출
# 3. 2022년 5월에 생산된 품목들에 대해서 각 품목별 총매출을 구해야되기 때문에, JOIN을 진행했습니다. 가격은 FOOD_PRODUCT에 존재하고, 구매수량은 FOOD_ORDER에 존재하기 때문입니다.
# 4. JOIN을 진행할 때는 각 테이블에 존재하는 PRODUCT_ID를 기준으로 진행했습니다.
# 5. 이후, 2022년 5월에 여러개를 생산한 동일한 PRODUCT_ID가 존재했기 때문에, PRODUCT_ID와 PRODUCT_NAME을 GROUP BY 진행했습니다.
# 6. 총매출은 FOOD_ORDER 테이블에 있는 AMOUNT와 FOOD_PRODUCT 테이블에 있는 PRICE를 곱해서 이를 SUM()하여 구했습니다.
# 7. 마지막으로 ORDER BY를 통해 총매출 기준으로 내림차순을 진행하였고, 총매출이 동일했을시에는 PRODUCT_ID를 기준으로 오름차순하도록 쿼리문을 작성했습니다.

SELECT FO.PRODUCT_ID
     , FP.PRODUCT_NAME
     , SUM(FO.AMOUNT * FP.PRICE) AS 'TOTAL_SALES'
FROM FOOD_ORDER AS FO
  INNER JOIN FOOD_PRODUCT AS FP ON FO.PRODUCT_ID = FP.PRODUCT_ID
WHERE DATE_FORMAT(FO.PRODUCE_DATE, '%Y-%m') = '2022-05'
GROUP BY FO.PRODUCT_ID, FP.PRODUCT_NAME
ORDER BY SUM(FO.AMOUNT * FP.PRICE) DESC, FO.PRODUCT_ID ASC;