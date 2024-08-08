-- 1-country_users.sql
-- This script creates a table users with id, email, name, and country attributes
-- id: integer, never null, auto increment and primary key
-- email: string (255 characters), never null and unique
-- name: string (255 characters)
-- country: enumeration of countries: US, CO, and TN, never null (default US)
-- If the table already exists, the script will not fail

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- Primary key, auto-incremented id
    email VARCHAR(255) NOT NULL UNIQUE,       -- Unique and non-null email
    name VARCHAR(255),                        -- Name field with max length of 255 characters
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'  -- Enumeration for country, default is 'US'
);

-- End of the script
