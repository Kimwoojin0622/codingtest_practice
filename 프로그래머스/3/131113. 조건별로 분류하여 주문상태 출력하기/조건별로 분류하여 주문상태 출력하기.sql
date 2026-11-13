# FOOD_ORDER 테이블 - 식품 공장의 주문정보를 담은 테이블
# 주문ID, 제품ID, 주문양, 출고일자 등이 존재함.

# FOOD_ORDER 테이블에서 2022년 5월 1일을 기준으로 이전의 데이터는 '출고완료'로 표시하고
# 이 후 날짜는 '출고대기'로 표시, 미정이면 '출고미정'으로 출력해야함.

# 이를 풀기 위해서 CASE WHEN 문을 활용
SELECT ORDER_ID
     , PRODUCT_ID
     , OUT_DATE
     , CASE
           # 2022년 5월 1일을 기준으로 이전의 데이터는 '출고완료'
           WHEN DATE_FORMAT(OUT_DATE, '%Y-%m-%d') <= '2022-05-01' THEN '출고완료'
           # 이 후 날짜는 '출고대기'
           WHEN DATE_FORMAT(OUT_DATE, '%Y-%m-%d') > '2022-05-01' THEN '출고대기'
           # ELSE 문을 활용해서 나머지 값들을 '출고미정'으로 진행
           ELSE '출고미정'
       END AS '출고여부'
FROM FOOD_ORDER
# 마지막으로 주문 정보를 기준으로 오름차순이기 때문에 ORDER BY를 활용해서 오름차순 진행
ORDER BY ORDER_ID ASC;