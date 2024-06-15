-- Day 26
-- 596. Classes More Than 5 Students
SELECT class
FROM Courses
GROUP BY 1
HAVING COUNT(class) >= 5 

-- Day 27
-- 