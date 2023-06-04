DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Bonus;

CREATE TABLE IF NOT EXISTS Employee (
  empId INT,
  name VARCHAR(255),
  supervisor INT,
  salary INT
);

CREATE TABLE IF NOT EXISTS Bonus (
  empId INT,
  bonus INT
);

TRUNCATE TABLE Employee;

INSERT INTO Employee (empId, name, supervisor, salary) VALUES
(3, 'Brad', NULL, 4000),
(1, 'John', 3, 1000),
(2, 'Dan', 3, 2000),
(4, 'Thomas', 3, 4000);

TRUNCATE TABLE Bonus;

INSERT INTO Bonus (empId, bonus) VALUES
(2, 500),
(4, 2000);
