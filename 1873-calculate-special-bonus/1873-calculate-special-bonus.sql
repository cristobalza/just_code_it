# Write your MySQL query statement below
SELECT
    employee_id
    , bonus
FROM (SELECT
    employee_id
    , CASE 
        WHEN name NOT LIKE 'M%' AND MOD(employee_id, 2) != 0 THEN salary
        ELSE 0
        END AS bonus
FROM Employees) AS tbl
ORDER BY 
    employee_id ASC
;