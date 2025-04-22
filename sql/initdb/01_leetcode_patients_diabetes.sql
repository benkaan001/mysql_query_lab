-- sql/initdb/01_leetcode_patients_diabetes.sql
-- Schema definition for LeetCode Problem: Patients With a Condition

-- Create the database specific to this problem
CREATE DATABASE IF NOT EXISTS leetcode_01_db;

-- Grant privileges for the application user on this new database
-- NOTE: Replace 'dockeruser' with the actual MYSQL_USER defined in your .env file if different.
-- The '%' means the user can connect from any host (common for Docker setups).
GRANT ALL PRIVILEGES ON leetcode_01_db.* TO 'dockeruser'@'%';

-- Apply the privilege changes
FLUSH PRIVILEGES;

-- Switch to the problem-specific database context
USE leetcode_01_db;

-- Table: patients (From LeetCode Diabetes Problem)
-- Stores patient information including conditions.
DROP TABLE IF EXISTS patients; -- Drop if exists for clean setup during init

CREATE TABLE patients (
    patient_id INT,
    patient_name VARCHAR(30),
    conditions VARCHAR(100),
    -- Consider adding a primary key if appropriate for other problems
    -- PRIMARY KEY (patient_id)
    INDEX idx_patient_name (patient_name) -- Example index
) COMMENT='Patient data for LeetCode diabetes problem';

