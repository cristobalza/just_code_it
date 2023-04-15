# Write your MySQL query statement below
WITH data2 AS (
    SELECT DISTINCT 
        author_id AS id
    FROM Views
    WHERE author_id = viewer_id 
    
)

SELECT 
    id
FROM data2
ORDER BY id ASC
;