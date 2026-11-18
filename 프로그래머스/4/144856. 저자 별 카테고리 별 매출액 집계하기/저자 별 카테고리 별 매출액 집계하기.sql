# 저자 별 카테고리 별 매출액 집계하기
# 테이블 1 -> BOOK 테이블
  # 책 ID, 카테고리, 작가 ID, 가격, 출판 날짜
# 테이블 2 -> AUTHOR 테이블
  # 작가 ID, 작가 이름
# 테이블 3 -> BOOK_SALES 테이블
  # 책 ID, 판매일자, 판매량
  
# 문제 : 2022년 1월의 도서 판매 데이터를 기준으로 저자 별, 카테고리 별 매출액 을 구하고
# 저자 ID, 저자명, 카테고리, 매출액 리스트를 출력하는 SQL문 작성
# 결과는 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬

# 1. 2022년 1월 데이터를 추출해내기 위해, BOOK_SALES 테이블을 활용하여 WHERE절에 SALES_DATE가 2022년 1월인 데이터를 DATE_FORMAT 함수를 활용하여 추출했습니다.

# 2. 매출량 * 매출액을 진행하기 위해 BOOK 테이블과 BOOK_SALES 테이블의 JOIN을 진행했습니다.
# BOOK 테이블의 BOOK_ID와 BOOK_SALES 테이블의 BOOK_ID를 이용했습니다.

# 3. 또한, 각각의 각자분들의 카테고리별 매출 합계를 구해야되기 때문에, AUTHOR 테이블 또한 JOIN을 진행하였고, BOOK 테이블과 AUTHOR 테이블의 있는 AUTHOR_ID를 활용하여 JOIN을 진행했습니다.

# 4. 매출액을 구하기 위해, GROUP BY를 활용하여 작가 이름, 작가 아이디, 카테고리 컬럼을 GROUP BY 를 진행했습니다.

# 5. 이후, 작가별 카테고리별 합계를 구하기 위해 SUM() 집계함수를 통해 BOOK_SALES의 SALES 값과 BOOK 테이블의 PRICE 컬럼을 곱하고 SUM() 집계함수를 이용해 TOTAL_SALES를 구했습니다.

# 6. 마지막으로는 AUTHOR_ID를 기준으로 오름차순, 카테고리 별로 내림차순을 진행했습니다.

SELECT A.AUTHOR_ID
     , A.AUTHOR_NAME
     , B.CATEGORY
     , SUM(BS.SALES * B.PRICE) AS 'TOTAL_SALES'
FROM BOOK_SALES AS BS
  LEFT JOIN BOOK AS B ON BS.BOOK_ID = B.BOOK_ID
  LEFT JOIN AUTHOR AS A ON B.AUTHOR_ID = A.AUTHOR_ID
WHERE DATE_FORMAT(BS.SALES_DATE, '%Y-%m') = '2022-01'
GROUP BY A.AUTHOR_NAME, A.AUTHOR_ID, B.CATEGORY
ORDER BY A.AUTHOR_ID ASC, B.CATEGORY DESC;