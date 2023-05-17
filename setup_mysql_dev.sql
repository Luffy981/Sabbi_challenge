-- Script that prepares a MySQL server

CREATE DATABASE IF NOT EXISTS sabbi_db;
CREATE USER IF NOT EXIST 'sabbi_dev'@'localhost' IDENTIFIED BY 'sabbi_pwd';
GRANT ALL PRIVILEGES ON sabbi_db.* TO 'sabbi_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'sabbi_dev'@'localhost';
FLUSH PRIVILEGES;
