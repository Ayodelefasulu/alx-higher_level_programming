-- 2-create_read_user.sql

-- Create database hbtn_0d_2 if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user user_0d_2 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant USAGE privilege to user_0d_2 on all databases
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';

-- Grant SELECT privilege to user_0d_2 on database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Grant CREATE privilege to user_0d_2 on database hbtn_0d_2
GRANT CREATE ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

