# 입양 시각 구하기(2)

# 테이블 1 - ANIMAL_OUTS (동물 보호소에서 입양 보낸 동물의 정보)
  # 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부

# 문제 : 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성
# 결과는 시간대 순으로 정렬

# 1. ANIMAL_OUTS 테이블의 DATETIME을 활용. 몇 시에 가장 입양이 활발하게 일어나는지 보기위해, DATETIME의 HOUR() 함수를 이용하여 GROUP BY를 진행

# 2. 시간대별 몇 건의 입양이 있었는지 COUNT() 집계 함수를 통해 출력

# 3. 0시부터 23시까지 없는 시간대가 존재. 11시, 19시는 존재하지만 0시, 2시는 존재하지 않음
# 그래서, 재귀 함수를 통해 0시부터 23시까지 존재하는 HOUR_TABLE을 생성

# 4. 0시부터 23시까지의 HOUR 컬럼을 가지고 있는 HOUR_TABLE을 기준으로 #1번에서 만들었던 시간별 입양 건수를 LEFT JOIN을 진행. JOIN 할 때는 HOUR 컬럼을 기준으로 JOIN을 진행

# 5. 이 때, 0시와 2시 같은 경우에는 COUNT 컬럼의 값이 NULL 이니, 이럴 경우에는 COUNT 컬럼에 0을 집어넣기 위해 CASE WHEN 문을 사용해서, IS NULL이면 0을 아니면 기본 COUNT 값을 출력

# 6. 마지막으로는 HOUR을 기준으로 오름차순 정렬

WITH RECURSIVE HOUR_TABLE AS (
    SELECT 0 AS 'HOUR'
    
    UNION ALL
    
    SELECT HOUR + 1
    FROM HOUR_TABLE
    WHERE HOUR < 23
)

SELECT HT.HOUR
     , CASE
           WHEN CNT IS NULL THEN 0
           ELSE CNT
       END AS 'CNT'
FROM HOUR_TABLE AS HT
  LEFT JOIN (SELECT HOUR(DATETIME) AS 'HOUR'
                  , COUNT(ANIMAL_ID) AS 'CNT'
             FROM ANIMAL_OUTS
             GROUP BY HOUR(DATETIME)) AS RAW_TABLE ON HT.HOUR = RAW_TABLE.HOUR
ORDER BY HT.HOUR ASC;

