-- create_force_name_table.sql

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS `force_name` (
    `id` INT,
    `name` VARCHAR(256) NOT NULL
);

