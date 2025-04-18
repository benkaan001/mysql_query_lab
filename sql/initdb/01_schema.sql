
USE query_lab_db;


CREATE TABLE IF NOT EXISTS departments (
    dept_no CHAR(4) NOT NULL COMMENT 'Unique department number (Primary Key)',
    dept_name VARCHAR(40) NOT NULL COMMENT 'Department name (must be unique)',
    PRIMARY KEY (dept_no),
    UNIQUE KEY uk_dept_name (dept_name) -- Renamed unique key for clarity
) COMMENT='Table containing department numbers and names.';


