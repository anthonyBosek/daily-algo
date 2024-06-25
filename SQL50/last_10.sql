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

-- Day 45
-- 1527. Patients With a Condition
-- *Approach 1: RegEx*
SELECT * FROM patients WHERE conditions REGEXP '\\bDIAB1';
-- *Approach 2: LIKE*
SELECT patient_id,patient_name,conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';

-- Day 46
-- 196. Delete Duplicate Emails
DELETE FROM Person
WHERE id NOT IN (
    SELECT id
    FROM (
        SELECT MIN(id) AS id
        FROM Person
        GROUP BY email
    ) AS tmp
);

-- Day 47
-- 176. Second Highest Salary
SELECT
    (SELECT
        DISTINCT salary 
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 offset 1
    ) AS SecondHighestSalary;

-- Day 48
-- 1484. Group Sold Products By The Date
select 
    sell_date,
    count(distinct product) as num_sold,
    group_concat(distinct product order by product) as products
from
    Activities 
group by 
    sell_date
order by
    sell_date;
-- *another way
-- select sell_date, count(distinct product) as num_sold, Group_concat(distinct product separator ',') as products from Activities group by sell_date;

-- Day 49
-- 1327. List the Products Ordered in a Period
-- approach 1
select product_name, sum(unit) as unit from products
join orders using(product_id)
where year(order_date)=2020 and month(order_date)=2
group by 1
having sum(unit)>99;
-- approach 2
select product_name, unit
from (
select p.product_name, sum(o.unit) unit
from Products p
inner join orders o on o.product_id = p.product_id 
where o.order_date between '2020-02-01' and '2020-02-29'
group by 1
) t 
where unit >= 100;
-- approach 3 - - best
SELECT 
    p.product_name,
    SUM(o.unit) AS unit
FROM Products p
INNER JOIN Orders o ON p.product_id = o.product_id AND MONTH(o.order_date) = 2 AND YEAR(order_date) = 2020
GROUP BY o.product_id HAVING unit >= 100;

-- Day 50
-- 1517. Find Users With Valid E-Mails
SELECT *
FROM Users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\\?com)?\\.com$';

SELECT * 
FROM Users
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$';