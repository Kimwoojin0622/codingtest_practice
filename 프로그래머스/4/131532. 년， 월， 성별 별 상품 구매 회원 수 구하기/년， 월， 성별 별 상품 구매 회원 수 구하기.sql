# 년, 월, 성별 별 상품 구해 회원 수 구하기

# 테이블 1 - USER_INFO 테이블
  # 회원 ID, 성별(남자 0, 여자 1), 나이, 가입일
  
# 테이블 2 - ONLINE_SALE 테이블
  # 온라인 상품 판매 ID, 회원 ID, 상품 ID, 판매량, 판매일
  
# 문제 : USER_INFO 테이블과 ONLINE_SALE 테이블에서 년, 월, 성별 별로 상품을 구매한 회원수를 집계하는 SQL문을 작성
# 결과는 년, 월, 성별을 기준으로 오름차순 정렬
# 성별 정보가 없는 경우에는 결과에서 제외

# 1. 처음에는 ONLINE_SALE 테이블을 기준으로 USER_INFO 테이블과 JOIN을 진행했습니다.
# 각 테이블의 USER_ID를 기준으로 하여 JOIN을 진행했습니다.
# 년도, 월 뿐만 아니라 GENDER 별로 구해야됐기 때문에 ONLINE_SALE에는 없는 GENDER 컬럼을 사용하기 위해 USER_INFO 테이블을 JOIN 하였습니다.

# 2. GENDER가 없는 값은 원하지 않았기 때문에, WHERE절을 활용하여 GENDER가 없는 값을 IS NOT NULL을 통해 제거

# 3. 년도, 월, 성별 별 상품 구매 회원 수를 구하기 위해 년도와 월, 성별을 기준으로 GROUP BY 를 진행했습니다. 년도와 월은 SALES_DATE 컬럼을 활용하여 YEAR()과 MONTH() 함수를 활용해 GROUP BY 를 진행했습니다.

# 4. GROUP BY를 진행하고, 년도, 월, 성별 별 상품 구매 회원 수를 COUNT()하는 과정에서, 각 월에 한 명의 사람이 여러 상품을 구매했을 수도 있기 때문에 COUNT() 집계 함수에서 DISTINCT를 통해 한 명의 사람이 여러 상품을 구매한 경우에는 중복을 제거하고, 한 건만 남기도록 진행했습니다.

# 5. 마지막으로는 년도, 월, 성별 순으로 ORDER BY 절에서 오름차순을 진행했습니다.

SELECT YEAR(OS.SALES_DATE) AS 'YEAR'
     , MONTH(OS.SALES_DATE) AS 'MONTH'
     , UI.GENDER
     , COUNT(DISTINCT OS.USER_ID) AS 'USERS'
FROM ONLINE_SALE AS OS
  LEFT JOIN USER_INFO AS UI ON OS.USER_ID = UI.USER_ID
WHERE UI.GENDER IS NOT NULL
GROUP BY YEAR(OS.SALES_DATE), MONTH(OS.SALES_DATE), UI.GENDER
ORDER BY YEAR(OS.SALES_DATE) ASC, MONTH(OS.SALES_DATE) ASC, UI.GENDER ASC;