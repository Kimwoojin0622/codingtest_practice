# Rising Temperature

# 테이블 1 - WEATHER 테이블
# ID, RECORDDATE, TEMPERATURE 컬럼 존재

# 문제 : 전 날의 기온보다 더 높은 기온을 가진 ID를 출력
# 만약 ID3의 날짜가 2015-01-03이고 기온이 20도, ID4의 날짜가 2015-01-04이고 기온이 30도면 전날의 기온인 20도보다 높으니, ID 4를 출력

# 1. 각 행 별, 이전 날씨를 구하기 위해 LAG를 통해서 그 전 행에 있는 TEMPERATURE 값을 가져온 뒤, 해당 컬럼명을 YESTERDAY_TEMPERATURE이라고 설정

# 2. 테스트 케이스 중, 날씨가 하루 건너 뛰는 형태가 존재. 2015-04-13 다음 데이터가 2015-04-15이므로, 2015-04-14가 존재하지 않음. 그래서 LAG()를 통해 그 전 행에 있는 RECORDATE 값을 가져온 뒤, 해당 컬럼명을 YESTERDAY라고 설정

# 3. WHERE절에 현재 날짜가 가지고 있는 TEMPERATURE가 YESTERDAY_TEMPERATURE보다 크고, DATEDIFF() 를 통해 구한 날짜간 차이가 1인 행만 불러오도록 조건절 작성
  # 왜냐하면 2015-04-13과 2015-04-15의 차이는 2임. 그 전날의 TEMPERATURE를 모르기 때문에 제거

# 4. 마지막으로 ID 컬럼만 출력되도록 원했기 때문에, ID 컬럼을 출력

SELECT ID
FROM (
    SELECT *
         , LAG(TEMPERATURE) OVER(ORDER BY RECORDDATE) AS 'YESTERDAY_TEMPERATURE'
         , LAG(RECORDDATE) OVER(ORDER BY RECORDDATE) AS 'YESTERDAY'
    FROM WEATHER
) AS YESTER_TOMMOROW_TABLE
WHERE TEMPERATURE > YESTERDAY_TEMPERATURE
  AND DATEDIFF(RECORDDATE, YESTERDAY) = 1;
