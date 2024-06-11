-- Day 1
-- 1757. Recyclable and Low Fat Products
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y'

-- Day 2
-- 584. Find Customer Referee
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id is null

-- Day 3
-- 595. Big Countries
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >=  25000000

-- Day 4
-- 1148. Article Views I
-- ** Beats 100% of submissions!!! **
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC

-- Day 5
-- 1683. Invalid Tweets
-- ** Beats 100% of submissions!!! **
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15
-- WHERE CHAR_LENGTH(content) > 15 -- a tad bit slower! (99.96%)

-- Day 6
-- 1378. Replace Employee ID With The Unique Identifier
SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id

-- Day 7
-- 1068. Product Sales Analysis I
SELECT P.product_name, S.year, S.price
FROM Sales AS S
LEFT JOIN Product AS P
ON S.product_id = P.product_id
-- ** without alias (AS) **
-- SELECT Product.product_name, Sales.year, Sales.price
-- FROM Sales
-- LEFT JOIN Product
-- ON Sales.product_id = Product.product_id

-- Day 8
-- 1581. Customer Who Visited but Did Not Make Any Transactions
SELECT V.customer_id, COUNT(V.visit_id) AS count_no_trans
FROM Visits AS V
LEFT JOIN Transactions AS T
ON V.visit_id = T.visit_id
WHERE T.transaction_id IS NULL
GROUP BY V.customer_id

-- Day 9
-- 197. Rising Temperature
SELECT W1.id
FROM Weather AS W1
JOIN Weather AS W2
ON DATEDIFF(W1.recordDate, w2.recordDate) = 1
WHERE W1.temperature > W2.temperature
-- ** without JOIN **
-- SELECT W1.id
-- FROM Weather W1, Weather W2
-- WHERE W1.temperature > W2.temperature AND DATEDIFF(W1.recordDate, W2.recordDate) = 1

-- Day 10
-- 1661. Average Time of Process per Machine
SELECT A1.machine_id, ROUND(AVG(A2.timestamp - A1.timestamp), 3) AS processing_time
FROM Activity AS A1
JOIN ACTIVITY AS A2
ON A1.machine_id = A2.machine_id AND A1.process_id = A2.process_id
AND A1.activity_type = 'start' AND A2.activity_type = 'end'
GROUP BY A1.machine_id

-- Day 11
-- 577. Employee Bonus
SELECT E.name, B.bonus
FROM Employee AS E
LEFT JOIN Bonus AS B
    ON E.empId = B.empId
WHERE B.bonus < 1000 OR B.bonus IS NULL

-- Day 12
-- 1280. Students and Examinations
SELECT
    Students.student_id,
    Students.student_name,
    Subjects.subject_name,
    COUNT(Examinations.subject_name) AS attended_exams
FROM Students
JOIN Subjects
LEFT JOIN Examinations
ON Students.student_id = Examinations.student_id
AND Subjects.subject_name = Examinations.subject_name
GROUP BY Students.student_id, Subjects.subject_name
ORDER BY student_id ASC, subject_name ASC
-- *alternative solution*
-- SELECT s.student_id, s.student_name, su.subject_name, count(e.student_id) as attended_exams 
-- FROM Students s Join Subjects su
-- LEFT JOIN Examinations e
-- ON s.student_id = e.student_id and su.subject_name = e.subject_name
-- GROUP BY s.student_id, su.subject_name
-- ORDER BY s.student_id, su.subject_name;

-- Day 13
-- 570. Managers with at Least 5 Direct Reports
WITH A AS (
    SELECT MANAGERID, COUNT(*) CNT
    FROM Employee
    GROUP BY managerId 
)
SELECT E.NAME
FROM A, Employee E
WHERE CNT >= 5
    AND A.MANAGERID = E.id 
-- *alternative solution*
-- SELECT E1.name
-- FROM Employee AS E1
-- JOIN Employee AS E2
-- ON E2.managerID = E1.ID
-- GROUP BY E1.id, E1.name
-- HAVING count(E2.managerID) >= 5;
-- *alternative solution*
-- select name
-- from employee
-- where id
-- in ( select 
        --     managerid
        -- from 
        --     employee
        -- group by 
        --     managerid
        -- having count(*)>=5);

-- Day 14
-- 1934. Confirmation Rate
SELECT s.user_id, 
  ROUND(AVG(IF(c.action='confirmed',1,0)),2) as confirmation_rate 
FROM Signups s
LEFT JOIN Confirmations c using (user_id)
GROUP BY s.user_id

-- Day 15
-- 620. Not Boring Movies
SELECT *
FROM Cinema
WHERE MOD( id, 2) = 1
AND description != 'boring'
ORDER BY rating DESC
-- *alternative solution*
-- SELECT * FROM Cinema WHERE (id%2=1) AND description != "boring"
-- ORDER BY rating DESC

-- Day 16
-- 1251. Average Selling Price
SELECT p.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
FROM Prices p LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND
u.purchase_date BETWEEN start_date AND end_date
GROUP BY product_id

-- Day 17
-- 1075. Project Employees I
SELECT p.project_id, ROUND(AVG(e.experience_years),2) AS average_years
FROM Project p 
LEFT JOIN Employee e
ON p.employee_id = e.employee_id
GROUP BY p.project_id

-- Day 18
-- 1633. Percentage of Users Attended a Contest
SELECT r.contest_id,
ROUND(COUNT(r.user_id) * 100/ (SELECT COUNT(user_id) FROM Users),2) AS percentage
FROM Register r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;
-- *solution explanation*
-- SELECT 
--   contest_id, -- The ID of the contest
--   ROUND(
--     -- Calculate the percentage of users
--     COUNT(DISTINCT user_id) * 100 / (
--       SELECT 
--         COUNT(user_id) -- Total number of unique users
--       FROM 
--         Users
--     ), 
--     2
--   ) AS percentage -- The percentage of users registered for each contest, rounded to 2 decimal places
-- FROM 
--   Register -- The table containing registration information
-- GROUP BY 
--   contest_id -- Group the data by contest ID
-- ORDER BY 
--   percentage DESC, -- Order the results by percentage in descending order
--   contest_id; -- Then order by contest ID for ties

-- Day 19
-- 1211. Queries Quality and Percentage
SELECT 
    query_name,
    ROUND(AVG(rating/position), 2) AS quality,
    ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS poor_query_percentage
FROM 
    Queries
WHERE query_name is not null
GROUP BY
    query_name;

-- Day 20
-- 1193. Monthly Transactions I
SELECT
    SUBSTR(trans_date,1,7) AS month,
    country,
    count(id) AS trans_count,
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY month, country

-- Day 21
-- 