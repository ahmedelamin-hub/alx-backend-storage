-- 0-uniq_users.sql
-- This script creates a table users with id, email, and name attributes
-- id: integer, never null, auto increment and primary key
-- email: string (255 characters), never null and unique
-- name: string (255 characters)
-- If the table already exists, the script will not fail

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,     -- Primary key, auto-incremented id
    email VARCHAR(255) NOT NULL UNIQUE,    -- Unique and non-null email
    name VARCHAR(255)                      -- Name field with max length of 255 characters
);

-- End of the script
