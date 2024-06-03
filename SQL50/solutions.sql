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
-- 