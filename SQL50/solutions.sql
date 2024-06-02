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

-- Day3