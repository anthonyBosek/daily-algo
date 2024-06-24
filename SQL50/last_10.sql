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
-- 

-- Day 49
-- 

-- Day 50
-- 