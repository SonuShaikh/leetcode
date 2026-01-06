-- 183. Customers Who Never Order
-- https://leetcode.com/problems/customers-who-never-order/description/
-- Write your MySQL query statement below
-- Not exist is much optimized way than Not in and left join
SELECT
    cust.name AS Customers
FROM
    Customers cust
WHERE
    NOT EXISTS(
        SELECT 1 FROM Orders ord
        WHERE cust.id = ord.customerid
    )


-- https://leetcode.com/problems/department-highest-salary/
-- Write your MySQL query statement below
SELECT 
        tmp.Department
    ,   tmp.Employee
    ,   tmp.salary
FROM (
    SELECT
            dept.name AS Department
        ,   emp.name  AS Employee
        ,   emp.salary 
        ,   RANK() OVER (PARTITION BY emp.departmentid ORDER BY emp.salary DESC) AS RN
    FROM
        employee emp
        INNER JOIN department dept
            ON dept.id = emp.departmentid
) AS tmp
WHERE
    tmp.RN = 1


-- https://leetcode.com/problems/department-top-three-salaries/
SELECT 
        tmp.Department
    ,   tmp.Employee
    ,   tmp.salary
FROM (
    SELECT
            dept.name AS Department
        ,   emp.name  AS Employee
        ,   emp.salary 
        ,   DENSE_RANK() OVER (PARTITION BY emp.departmentid ORDER BY emp.salary DESC) AS RN
    FROM
        employee emp
        INNER JOIN department dept
            ON dept.id = emp.departmentid
) AS tmp
WHERE
    tmp.RN <= 3
ORDER BY tmp.salary DESC

-- https://leetcode.com/problems/nth-highest-salary/

CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
    -- Guard clause for invalid N
    IF N <= 0 THEN
        RETURN;
    END IF;

  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT 
        emp.salary
    FROM
        employee emp
    GROUP BY emp.salary
    ORDER BY emp.salary DESC
    OFFSET N - 1 
    LIMIT 1
    
  );
END;
$$ LANGUAGE plpgsql;


--https://leetcode.com/problems/rank-scores/submissions/1876304944/
-- Write your PostgreSQL query statement below
SELECT
        s.Score
    ,   DENSE_RANK() OVER(ORDER BY s.score DESC) AS rank
FROM
    Scores s
ORDER BY rank