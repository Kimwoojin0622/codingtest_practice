# 2022년 1월의 도서 판매량을 합산해야됨.
# 그러기 위해서 BOOK 테이블 기준으로 BOOK_SALES 테이블 LEFT JOIN (INNER JOIN 도 가능)
# BOOK 테이블은 - 책관련 / BOOK_SALES는 판매량 관련
SELECT B.CATEGORY
     , SUM(BS.SALES) AS 'TOTAL_SALES'
FROM BOOK AS B
  INNER JOIN BOOK_SALES AS BS ON B.BOOK_ID = BS.BOOK_ID
# 2022년 1월의 카테고리 별 도서 판매량이기에, DATE_FORMAT을 사용해서 조건을 걸어야함
WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-01'
# 카테고리 별로 판매량을 집계하기 위해 카테고리명 기준으로 GROUP BY를 진행
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY ASC;