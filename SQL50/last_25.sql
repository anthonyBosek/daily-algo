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