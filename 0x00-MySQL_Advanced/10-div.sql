-- 10-div.sql
-- This script creates a function SafeDiv to divide the first number by the second
-- and return 0 if the second number is 0

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END //

DELIMITER ;
