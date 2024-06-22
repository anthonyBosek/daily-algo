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

-- Day 32
-- 610. Triangle Judgement
-- *Approach 3: IF (cleaner)*
SELECT x, y, z, 
IF(((x+y)>z AND (y+z)>x AND (x+z)>y), "Yes", "No") AS triangle 
FROM triangle
-- -- *Approach 2: CASE WHEN*
-- SELECT *,
-- CASE 
-- WHEN x+y>z AND z+y>x AND z+x>y THEN 'Yes'
-- ELSE 'No' END
-- AS triangle
-- FROM Triangle
-- -- *Approach 1: IF*
-- select
--     x,
--     y,
--     z,
--     if(x+y>z and y+z>x and z+x>y, 'Yes' , 'No') as triangle
-- from 
--     triangle;

-- Day 33
-- 180. Consecutive Numbers
SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;

-- Day 34
-- 1164. Product Price at a Given Date
-- *Approach 2: CTE*
WITH cte AS (
    SELECT *, RANK()OVER(PARTITION BY product_id ORDER BY change_date DESC)AS rk 
    FROM products 
    WHERE 
        change_date <= '2019-08-16'
)

SELECT DISTINCT p.product_id,IFNULL(c.new_price,10)AS price 
FROM products p  
LEFT JOIN cte c 
on c.product_id=p.product_id
where rk=1
or rk IS NULL
ORDER BY price desc
-- -- *Approach 1: UNION ALL*
-- SELECT
--   product_id,
--   10 AS price
-- FROM
--   Products
-- GROUP BY
--   product_id
-- HAVING
--   MIN(change_date) > '2019-08-16'
-- UNION ALL
-- SELECT
--   product_id,
--   new_price AS price
-- FROM
--   Products
-- WHERE
--   (product_id, change_date) IN (
--     SELECT
--       product_id,
--       MAX(change_date)
--     FROM
--       Products
--     WHERE
--       change_date <= '2019-08-16'
--     GROUP BY
--       product_id
--   );

-- Day 35
-- 1204. Last Person to Fit in the Bus
-- *Approach 1: Window Function*
SELECT person_name
FROM (
    SELECT *,
           SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM Queue
) subquery
WHERE cumulative_weight <= 1000
ORDER BY  turn DESC
LIMIT 1;
-- -- *Approach 2: CTE*
-- WITH RunningTotal AS (
--     SELECT
--         person_name,
--         weight,
--         turn,
--         SUM(weight) OVER (ORDER BY turn) AS total
--     FROM
--         Queue
-- )
-- SELECT
--     person_name
-- FROM
--     RunningTotal
-- WHERE
--     total <= 1000
-- ORDER BY
--     turn DESC
-- LIMIT 1;

-- Day 36
-- 1907. Count Salary Categories
-- *Approach 1: RIGHT JOIN*
SELECT category, 
       COALESCE(SUM(accounts_count), 0) AS accounts_count
FROM (
  SELECT CASE 
           WHEN income < 20000 THEN 'Low Salary'
           WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
           ELSE 'High Salary'
         END AS category,
         COUNT(*) AS accounts_count
  FROM Accounts
  GROUP BY category
) AS categorized_accounts
RIGHT JOIN (
  SELECT 'Low Salary' AS category
  UNION ALL 
  SELECT 'Average Salary'
  UNION ALL 
  SELECT 'High Salary'
) AS all_categories USING (category)
GROUP BY category;
-- -- *Approach 2: UNION*
-- SELECT 
--     'Low Salary' AS category,
--     SUM(income < 20000) AS accounts_count
-- FROM 
--     Accounts
-- UNION 
--     SELECT 
--         'Average Salary' AS category,
--         SUM(income BETWEEN 20000 AND 50000 ) AS accounts_count
--     FROM 
--         Accounts
-- UNION
--     SELECT 
--         'High Salary' AS category,
--         SUM(income > 50000) AS accounts_count
--     FROM 
--         Accounts;

-- Day 37
-- 1978. Employees Whose Manager Left the Company
SELECT employee_id
FROM employees
WHERE manager_id NOT IN (SELECT employee_id FROM employees)
AND salary < 30000
ORDER BY employee_id ASC

-- Day 38
-- 626. Exchange Seats
SELECT 
    CASE
        WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM seat) THEN id
        WHEN id % 2 = 0 THEN id - 1
        ELSE id + 1
    END AS id,
    student
FROM
    seat
ORDER BY id;

-- Day 39
-- 1341. Movie Rating
-- *Approach 1: UNION ALL*
(SELECT name AS results
FROM MovieRating JOIN Users USING(user_id)
GROUP BY name
ORDER BY COUNT(*) DESC, name
LIMIT 1)
UNION ALL
(SELECT title AS results
FROM MovieRating JOIN Movies USING(movie_id)
WHERE EXTRACT(YEAR_MONTH FROM created_at) = 202002
GROUP BY title
ORDER BY AVG(rating) DESC, title
LIMIT 1);
-- -- *Approach 2: CTE*
WITH 
TheMostActiveUser AS (
    SELECT name
    FROM 
        Users
        NATURAL JOIN MovieRating
    GROUP BY user_id
    ORDER BY COUNT(*) DESC, name
    LIMIT 1
),
TheBestMovieFebruary AS (
    SELECT title
    FROM
        Movies
        NATURAL JOIN MovieRating
    WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY movie_id
    ORDER BY AVG(rating) DESC, title
    LIMIT 1
)

SELECT name AS results
FROM TheMostActiveUser
UNION ALL
SELECT title
FROM TheBestMovieFebruary

-- Day 40
-- 1321. Restaurant Growth
-- *Approach 1: CTE*
WITH A AS(SELECT visited_on, SUM(amount) as amount
FROM Customer
GROUP BY visited_on)


SELECT B.visited_on, B.amount, B.average_amount FROM (SELECT A.visited_on, 
SUM(A.amount) OVER(ORDER BY A.visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
ROUND(AVG(A.amount) OVER(ORDER BY A.visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) AS average_amount
FROM A
WHERE A.visited_on
GROUP BY A.visited_on) B
WHERE B.visited_on >= (SELECT MIN(A.visited_on)+ 6 FROM A)
-- -- *Approach 2: Subquery*
SELECT
    visited_on,
    (
        SELECT SUM(amount)
        FROM customer
        WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
    ) AS amount,
    ROUND(
        (
            SELECT SUM(amount) / 7
            FROM customer
            WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
        ),
        2
    ) AS average_amount
FROM customer c
WHERE visited_on >= (
        SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY)
        FROM customer
    )
GROUP BY visited_on;

-- Day 41
-- 585. Investments in 2016
SELECT ROUND(SUM(tiv_2016),2) AS "tiv_2016"
FROM Insurance
WHERE tiv_2015 IN(
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(pid)>=2
)
AND
(lat, lon) IN(
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(pid)=1
);

-- Day 42
-- 602. Friend Requests II: Who Has the Most Friends
WITH all_ids AS (
   SELECT requester_id AS id 
   FROM RequestAccepted
   UNION ALL
   SELECT accepter_id AS id
   FROM RequestAccepted)
SELECT id, 
   COUNT(id) AS num
FROM all_ids
GROUP BY id
ORDER BY COUNT(id) DESC
LIMIT 1;

-- Day 43
-- 185. Department Top Three Salaries
-- *Approach 1: Window Function*
SELECT d.name AS 'Department', 
       e1.name AS 'Employee', 
       e1.salary AS 'Salary' 
FROM Employee e1
JOIN Department d
ON e1.departmentId = d.id 
WHERE
    3 > (SELECT COUNT(DISTINCT e2.salary)
        FROM Employee e2
        WHERE e2.salary > e1.salary AND e1.departmentId = e2.departmentId);
-- *Approach 2: CTE*
WITH employee_department AS
    (
    SELECT d.id, 
        d.name AS Department, 
        salary AS Salary, 
        e.name AS Employee, 
        DENSE_RANK()OVER(PARTITION BY d.id ORDER BY salary DESC) AS rnk
    FROM Department d
    JOIN Employee e
    ON d.id = e.departmentId
    )
SELECT Department, Employee, Salary
FROM employee_department
WHERE rnk <= 3;

-- Day 44
-- 1667. Fix Names in a Table
SELECT
  user_id,
  CONCAT(
    UPPER(LEFT(name, 1)),
    LCASE(SUBSTRING(name, 2))
  ) AS name
FROM Users
ORDER BY user_id;