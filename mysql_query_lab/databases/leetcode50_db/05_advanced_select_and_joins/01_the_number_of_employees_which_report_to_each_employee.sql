DROP TABLE IF EXISTS Employees;

CREATE TABLE IF NOT EXISTS Employees (
  employee_id INT NOT NULL,
  name VARCHAR(20) NOT NULL,
  reports_to INT,
  age INT NOT NULL,
  PRIMARY KEY (employee_id)
);

TRUNCATE TABLE Employees;

INSERT INTO Employees (employee_id, name, reports_to, age)
VALUES (9, 'Hercy', NULL, 43);

INSERT INTO Employees (employee_id, name, reports_to, age)
VALUES (6, 'Alice', 9, 41);

INSERT INTO Employees (employee_id, name, reports_to, age)
VALUES (4, 'Bob', 9, 36);

INSERT INTO Employees (employee_id, name, reports_to, age)
VALUES (2, 'Winston', NULL, 37);
