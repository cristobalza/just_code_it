# Write your MySQL query statement below
SELECT 
    author_id as id
FROM (
    SELECT
        *
FROM Views
WHERE author_id = viewer_id
) AS tbl
GROUP BY author_id
HAVING COUNT(*) > 0
ORDER BY 
    author_id ASC
;