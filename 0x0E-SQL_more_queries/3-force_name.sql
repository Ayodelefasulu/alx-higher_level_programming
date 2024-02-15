-- create_force_name_table.sql

-- Use the database created
USE `hbtn_0d_2`;

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS `force_name` (
    `id` INT,
    `name` VARCHAR(256) NOT NULL
);

