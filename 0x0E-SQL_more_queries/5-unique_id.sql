-- create_unique_id_table.sql

USE `hbtn_0d_2`; -- Change this to your desired database name

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id` INT DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);

