-- create_force_name_table.sql

USE `hbtn_0d_2`; -- Change this to your desired database name

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS `force_name` (
    `id` INT,
    `name` VARCHAR(256) NOT NULL
);

