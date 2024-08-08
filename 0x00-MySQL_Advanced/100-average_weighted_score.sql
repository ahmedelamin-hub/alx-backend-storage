-- 100-average_weighted_score.sql
-- This script creates a stored procedure ComputeAverageWeightedScoreForUser to compute and store the average weighted score for a student

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight INT;

    -- Calculate the total weighted score and total weight
    SELECT SUM(score * weight), SUM(weight)
    INTO total_weighted_score, total_weight
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Calculate and update the average weighted score
    IF total_weight > 0 THEN
        UPDATE users
        SET average_score = total_weighted_score / total_weight
        WHERE id = user_id;
    END IF;
END //

DELIMITER ;
