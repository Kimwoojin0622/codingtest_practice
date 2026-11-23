# Last Person to Fit in the Bus

# 테이블 1 - Queue (탑승자들의 정보를 담은 테이블)
  # PERSON_ID, PERSON_NAME, WEIGHT, TURN

# 문제 : 버스에 탑승을 하기 위해 기다리는 승객들이 있는데, 승객들을 순서대로 태워야한다. 단, WEIGHT의 리밋은 1000 킬로그램이다. 그러므로 못타는 탑승자가 생길 수 있다. 그 중에서 마지막으로 탑승을 한 손님의 이름을 가져오는 문제

# 1. 처음에는 QUEUE 테이블에서 각 손님들이 탑승할 때마다 총 몇 킬로그램인지 구하기 위해 SUM() 윈도우 함수를 통해 TURN 순서대로 WEIGHT의 누적합을 구함. 컬럼명은 WEIGHT_SUM으로 설정
  # 100KG, 200KG, 300KG 이면 100 -> 300 -> 600 순으로 누적 합을 구함

# 2. 누적합을 구한 하나의 테이블을 FROM 절의 인라인뷰로 불러오고 WS_TABLE이라는 테이블 명을 설정.
  # WEIGHT_SUM 을 줄여서 WS

# 3. 그 중에서 마지막 탄 사람을 구해야되기 때문에, WHERE절에서 누적합이 1000이하인 사람들을 필터링.

# 4. 그 중에서 WEIGHT_SUM인 누적합을 기준으로 ORDER BY를 사용해 내림차순 한 뒤, LIMIT 1을 걸어서 가장 마지막 사람의 이름을 구함

SELECT PERSON_NAME
FROM (
    SELECT *
         , SUM(WEIGHT) OVER(ORDER BY TURN ASC) AS 'WEIGHT_SUM'
    FROM QUEUE
) AS WS_TABLE
WHERE WEIGHT_SUM <= 1000
ORDER BY WEIGHT_SUM DESC
LIMIT 1;
