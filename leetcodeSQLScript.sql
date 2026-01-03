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
