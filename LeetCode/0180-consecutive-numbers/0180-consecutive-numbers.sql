# Consecutive Numbers

# 테이블 1 - LOGS
  # ID, NUM

# 문제 : LOGS 테이블에서 3번 연속으로 나타나는 NUM을 출력

# 1. 먼저 세번 나타나는 NUM을 찾기 위해 각 행의 이전, 이후 NUM 값을 들고오는 LAG와 LEAD 윈도우 함수를 사용

# 2. 만약 1이 3번 연속 나온다면 현재 NUM과 LAG를 통해 얻은 NUM과 LEAD를 통해 얻은 NUM이 한 줄에 동일하게 있을 것임
  # EX)
  # 1 NULL 1
  # 1 1    1
  # 1 1    다음값
  # 이면 LAG는 NULL 1 1 이고 LEAD는 1 1 다음값일 것임
  # 그러므로 1의 값이 3개 일치하는 부분이 있으므로 1은 3개 연속으로 나온 숫자임

# 3. 단, 테스트 케이스에서 1이 4번 나올 경우 1의 값이 두 번 나오기 때문에, 이를 방지하기 위해 SELECT 문에 DISTINCT를 사용하여 중복을 제거

SELECT DISTINCT NUM AS 'CONSECUTIVENUMS'
FROM (
    SELECT *
         , LAG(NUM) OVER(ORDER BY ID ASC) AS 'BE'
         , LEAD(NUM) OVER(ORDER BY ID ASC) AS 'AF'
    FROM LOGS
) AS LAG_LEAD_TABLE
WHERE NUM = BE
  AND BE = AF;