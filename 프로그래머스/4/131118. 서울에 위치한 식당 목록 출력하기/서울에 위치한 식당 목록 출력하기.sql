# 테이블 1 - REST_INFO 테이블
  # 식당 ID, 식당 이름, 조회수, 즐겨 찾기 수 등
# 테이블 2 - REST_REVIEW 테이블
  # 리뷰 ID, 식당 ID, 회원 ID, 점수, 리뷰 텍스트, 리뷰 작성일

# 문제 : REST_INFO와 REST_REVIEW 테이블에서 서울에 위치한 식당들의 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수를 조회하는 SQL문을 작성
# 리뷰 평균 점수는 소수점 세 번째 자리에서 반올림 해주시고,
# 결과는 평균 점수를 기준으로 내림차순 정렬,
# 평균 점수가 같다면 즐겨찾기수를 기준으로 내림차순 정렬

# 1. REST_INFO 테이블에서 식당 주소가 서울을 포함한 값을 찾기 위해, WHERE 절에서 LIKE 연산자를 사용해 ADDRESS 컬럼에서 서울을 포함하는 행을 찾았습니다.

# 2. 식당 별 평균 점수를 구하기 위해 REST_

SELECT RI.REST_ID
     , RI.REST_NAME
     , RI.FOOD_TYPE
     , RI.FAVORITES
     , RI.ADDRESS
     , ROUND(AVG(RR.REVIEW_SCORE), 2) AS 'SCORE'
FROM REST_INFO AS RI
  LEFT JOIN REST_REVIEW AS RR ON RI.REST_ID = RR.REST_ID
WHERE RI.ADDRESS LIKE '서울%'
  AND RR.REVIEW_SCORE IS NOT NULL
GROUP BY RI.REST_ID, RI.REST_NAME
ORDER BY ROUND(AVG(RR.REVIEW_SCORE)) DESC, RI.FAVORITES DESC; 