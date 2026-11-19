# 연간 평가점수에 해당하는 평가 등급 및 성과금 조회하기

# 테이블 1 - HR_DEPARTMENT (회사의 부서 정보를 담은 테이블)
  # 부서 ID, 국문 부서명, 영문 부서명, 부서 위치

# 테이블 2 - HR_EMPLOYEES (회사의 사원 정보를 담은 테이블)
  # 사번, 성명, 부서 ID, 직책, 이메일, 연봉 등
  
# 테이블 3 - HR_GRADE (2022년 사원의 평가 정보를 담은 테이블)
  # 사번, 연도, 반기, 평가 점수


# 문제 : 사원별 성과금 정보를 조회해야합니다.
# 평가 점수별 등급과 등급에 따른 성과금 정보가 같을 때, 사번, 성명, 평가 등급, 성과금을 조회하는 SQL문을 작성
# 결과는 사번 기준으로 오름차순 정렬

# 평가 등급
# 96 이상은 'S', 성과금은 연봉기준 20%
# 90 이상은 'A', 성과금은 연봉기준 15%
# 80 이상은 'B', 성과금은 연봉기준 10%
# 그 외는 'C', 성과금은 연봉기준 0%

# 1. 사원들의 2022년 성과 점수를 구하기 위해 HR_GRADE와 HR_EMPLOYEES 테이블을 JOIN 하였습니다. JOIN은 두 테이블의 공통 컬럼인 EMP_NO를 기준으로 JOIN을 진행하였습니다.

# 2. JOIN을 진행했을 시, 사원들의 2022년 1분기, 2분기의 점수를 알 수 있기 때문에, EMP_NO를 기준으로 GROUP BY를 진행하여 각 사원별 1분기와 2분기 평균 SCORE를 AVG() 집계 함수를 이용하여 구할 수 있습니다.

# 3. AVG() 집계 함수와 CASE WHEN을 사용해서 GRADE 컬럼을 만들었습니다. 점수가 96 이상이면 S, 90 이상이면 A, 80 이상이면 B, 이외는 C가 되도록 CASE WHEN 문을 작성했습니다.

# 4. 보너스에서도 AVG() 집계함수와 CASE WHEN을 통해, 평균이 96점 이상이면 현재 연봉 컬럼인 SAL 컬럼에서 0.2를 곱했고, 90점 이상이면 0.15, 80점 이상이면 0.1, 나머지는 0을 곱했습니다.

# 5. 마지막으로 사번 컬럼을 기준으로 오름차순 정렬을 하였습니다.

SELECT HG.EMP_NO
     , HE.EMP_NAME
     , CASE
           WHEN AVG(HG.SCORE) >= 96 THEN 'S'
           WHEN AVG(HG.SCORE) >= 90 THEN 'A'
           WHEN AVG(HG.SCORE) >= 80 THEN 'B'
           ELSE 'C'
       END AS 'GRADE'
     , CASE
           WHEN AVG(HG.SCORE) >= 96 THEN HE.SAL * 0.2
           WHEN AVG(HG.SCORE) >= 90 THEN HE.SAL * 0.15
           WHEN AVG(HG.SCORE) >= 80 THEN HE.SAL * 0.1
           ELSE HE.SAL * 0
       END AS 'BONUS'    
FROM HR_GRADE AS HG
  LEFT JOIN HR_EMPLOYEES AS HE ON HG.EMP_NO = HE.EMP_NO
GROUP BY HG.EMP_NO
ORDER BY HG.EMP_NO ASC;