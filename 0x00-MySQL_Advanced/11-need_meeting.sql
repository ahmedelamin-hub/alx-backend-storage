-- 11-need_meeting.sql
-- This script creates a view need_meeting that lists all students
-- who have a score under 80 and no last_meeting or a last_meeting date more than a month ago

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < CURDATE() - INTERVAL 1 MONTH);
