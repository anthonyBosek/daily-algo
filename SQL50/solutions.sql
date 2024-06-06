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
-- 