-- 101-average_weighted_score.sql
-- This script creates a stored procedure ComputeAverageWeightedScoreForUsers
-- to compute and store the average weighted score for all students

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE finished INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;

    OPEN user_cursor;

    user_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF finished THEN 
            LEAVE user_loop;
        END IF;

        CALL ComputeAverageWeightedScoreForUser(user_id);
    END LOOP;

    CLOSE user_cursor;
END //

DELIMITER ;

