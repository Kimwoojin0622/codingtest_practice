SELECT EMP_NO
     , EMP_NAME
     , GRADE
     , CASE
           WHEN GRADE = 'S' THEN SAL * 0.2
           WHEN GRADE = 'A' THEN SAL * 0.15
           WHEN GRADE = 'B' THEN SAL * 0.1
           ELSE 0
       END AS 'BONUS'
FROM (SELECT HG.EMP_NO
           , HE.EMP_NAME
           , CASE
                 WHEN AVG(SCORE) >= 96 THEN 'S'
                 WHEN AVG(SCORE) >= 90 THEN 'A'
                 WHEN AVG(SCORE) >= 80 THEN 'B'
                 ELSE 'C'
             END AS 'GRADE'
           , HE.SAL
     FROM HR_GRADE AS HG
       INNER JOIN HR_EMPLOYEES AS HE ON HG.EMP_NO = HE.EMP_NO
     GROUP BY HG.EMP_NO) AS GRADE_TABLE
ORDER BY EMP_NO ASC;