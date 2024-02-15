-- create_id_not_null_table.sql

USE `hbtn_0d_2`; -- Change this to your desired database name

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id` INT DEFAULT 1,
    `name` VARCHAR(256)
);
