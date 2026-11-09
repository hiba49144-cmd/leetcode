-- Write your PostgreSQL query statement below.
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) 
RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    SELECT a.salary
    FROM (
      SELECT e.salary, 
             DENSE_RANK() OVER (ORDER BY e.salary DESC) AS ranked
      FROM Employee e
    ) a
    WHERE a.ranked = N
    LIMIT 1
  );
END;
$$ LANGUAGE plpgsql;