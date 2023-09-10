# Write your MySQL query statement below
WITH bearTbl AS (
SELECT
    *
    , SUM(CASE WHEN LOWER(content) LIKE '% bear %' THEN 1 ELSE 0 END) AS count
    , 'bear' AS word
FROM Files
)
, bullTbl AS (
SELECT
    *
    , SUM(CASE WHEN LOWER(content) LIKE '% bull %' THEN 1 ELSE 0 END) AS count
    , 'bull' AS word
FROM Files
)

SELECT
    word
    , count
FROM bearTbl
UNION ALL
SELECT
    word
    , count
FROM bullTbl
;