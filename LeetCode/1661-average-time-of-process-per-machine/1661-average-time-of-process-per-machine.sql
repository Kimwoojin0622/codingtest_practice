SELECT MACHINE_ID
     , ROUND(SUM(DIFF) / SUM(CNT), 3) AS 'PROCESSING_TIME'
FROM (SELECT MACHINE_ID
           , PROCESS_ID
           , MAX(TIMESTAMP) - MIN(TIMESTAMP) AS 'DIFF'
           , COUNT(*) / 2 AS 'CNT'
      FROM ACTIVITY
      GROUP BY MACHINE_ID, PROCESS_ID) AS DIFF_TABLE
GROUP BY MACHINE_ID;



-- SELECT MACHINE_ID
--      , PROCESS_ID
--      , MAX(TIMESTAMP) - MIN(TIMESTAMP) AS 'DIFF'
--      , COUNT(*) AS 'CNT'
-- FROM ACTIVITY
-- GROUP BY MACHINE_ID, PROCESS_ID

-- | machine_id | processing_time |
-- | ---------- | --------------- |
-- | 4          | 62.61           |
-- | 0          | 4.208           |
-- | 1          | 24.028          |
-- | 3          | 50.399          |
-- | 2          | 44.165          |
-- | 5          | 31.642          |