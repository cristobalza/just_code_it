CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT e1.salary
      FROM (SELECT DISTINCT salary FROM Employee) as e1
      WHERE (SELECT COUNT(*) 
             FROM (SELECT DISTINCT salary 
                   FROM Employee) as e2 
             WHERE e2.salary > e1.salary) = N - 1
      LIMIT 1

  );
END
