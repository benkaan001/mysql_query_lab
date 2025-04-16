-- sql/initdb/01_schema.sql
-- Initial database schema setup.
-- This script will be executed automatically by the MySQL container on its first run.

-- Create the database specified in the .env file if it doesn't already exist.
-- The container usually creates this automatically based on MYSQL_DATABASE,
-- but explicitly stating it can be good practice for clarity.
-- CREATE DATABASE IF NOT EXISTS ${MYSQL_DATABASE}; -- Often redundant, uncomment if needed

-- Switch to the target database context.
-- Use the value provided in the .env file for MYSQL_DATABASE.
-- Note: Docker Compose doesn't substitute variables inside these SQL files.
-- The database name here must match the one used by your application logic later.
USE query_lab_db; -- Make sure this matches MYSQL_DATABASE in your .env

-- Example Table: Create a simple 'departments' table to start.
CREATE TABLE IF NOT EXISTS departments (
    dept_no CHAR(4) NOT NULL,
    dept_name VARCHAR(40) NOT NULL,
    PRIMARY KEY (dept_no),
    UNIQUE KEY (dept_name)
);


