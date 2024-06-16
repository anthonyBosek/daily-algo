-- Day 26
-- 596. Classes More Than 5 Students
SELECT class
FROM Courses
GROUP BY 1
HAVING COUNT(class) >= 5 

-- Day 27
-- 1729. Find Followers Count
SELECT user_id, COUNT(*) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id

-- Day 28
-- 619. Biggest Single Number
SELECT MAX(num) AS num 
FROM ( SELECT num
        FROM MyNumbers
        GROUP BY num
        HAVING COUNT(num) = 1) AS a;

-- Day 29
-- 1045. Customers Who Bought All Products
SELECT customer_id
FROM customer
GROUP BY customer_id
HAVING COUNT(DISTINCT(product_key)) = (SELECT COUNT(*) FROM product)

-- Day 30
-- 1731. The Number of Employees Which Report to Each Employee
SELECT 
  mgr.employee_id, 
  mgr.name, 
  COUNT(emp.employee_id) AS reports_count, 
  ROUND(
    AVG(emp.age)
  ) AS average_age 
FROM 
  employees emp 
  JOIN employees mgr ON emp.reports_to = mgr.employee_id 
GROUP BY 
  employee_id 
ORDER BY 
  employee_id

-- Day 31
-- 1789. Primary Department for Each Employee
-- *Approach 2: Window Function (COUNT)*
SELECT 
  employee_id, 
  department_id 
FROM 
  (
    SELECT 
      *, 
      COUNT(employee_id) OVER(PARTITION BY employee_id) AS EmployeeCount
    FROM 
      Employee
  ) EmployeePartition 
WHERE 
  EmployeeCount = 1 
  OR primary_flag = 'Y';
-- *Approach 1: UNION*
-- -- Retrieving employees with primary_flag set to 'Y'
-- SELECT 
--   employee_id, 
--   department_id 
-- FROM 
--   Employee 
-- WHERE 
--   primary_flag = 'Y' 
-- UNION 
-- -- Retrieving employees that appear exactly once in the Employee table
-- SELECT 
--   employee_id, 
--   department_id 
-- FROM 
--   Employee 
-- GROUP BY 
--   employee_id 
-- HAVING 
--   COUNT(employee_id) = 1;