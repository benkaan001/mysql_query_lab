DROP TABLE IF EXISTS Project;
DROP TABLE IF EXISTS Employee;

-- Create the Project table
CREATE TABLE IF NOT EXISTS Project (
  project_id INT,
  employee_id INT
);

-- Create the Employee table
CREATE TABLE IF NOT EXISTS Employee (
  employee_id INT,
  name VARCHAR(10),
  experience_years INT
);

-- Truncate the Project table
TRUNCATE TABLE Project;

-- Insert data into the Project table
INSERT INTO Project (project_id, employee_id)
VALUES (1, 1), (1, 2), (1, 3), (2, 1), (2, 4);

-- Truncate the Employee table
TRUNCATE TABLE Employee;

-- Insert data into the Employee table
INSERT INTO Employee (employee_id, name, experience_years)
VALUES (1, 'Khaled', 3), (2, 'Ali', 2), (3, 'John', 1), (4, 'Doe', 2);
