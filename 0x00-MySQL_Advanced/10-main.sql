-- 10-main.sql
-- Show and test SafeDiv function
SELECT (a / b) AS normal_division FROM numbers;
SELECT SafeDiv(a, b) AS safe_division FROM numbers;
