SELECT X
     , Y
     , Z
     , IF(MIN + MIDDLE <= MAX, 'No', 'Yes') AS 'TRIANGLE'
FROM (
    SELECT *
         , CASE
                WHEN X < Y AND X < Z THEN X
                WHEN Y < X AND Y < Z THEN Y
                ELSE Z
           END AS 'MIN'
         , CASE
                WHEN (Y BETWEEN X AND Z) OR (Y BETWEEN Z AND X) THEN Y
                WHEN (X BETWEEN Y AND Z) OR (X BETWEEN Z AND Y) THEN X
                ELSE Z
           END AS 'MIDDLE'
         , CASE
                WHEN X > Y AND X > Z THEN X
                WHEN Y > X AND Y > Z THEN Y
                ELSE Z
           END AS 'MAX'
FROM TRIANGLE
) AS MMM;