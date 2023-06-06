DROP TABLE IF EXISTS Employee;

CREATE TABLE IF NOT EXISTS Employee (
  id INT,
  name VARCHAR(255),
  department VARCHAR(255),
  managerId INT
);

TRUNCATE TABLE Employee;

INSERT INTO Employee (id, name, department, managerId) VALUES (101, 'John', 'A', NULL);
INSERT INTO Employee (id, name, department, managerId) VALUES (102, 'Dan', 'A', 101);
INSERT INTO Employee (id, name, department, managerId) VALUES (103, 'James', 'A', 101);
INSERT INTO Employee (id, name, department, managerId) VALUES (104, 'Amy', 'A', 101);
INSERT INTO Employee (id, name, department, managerId) VALUES (105, 'Anne', 'A', 101);
INSERT INTO Employee (id, name, department, managerId) VALUES (106, 'Ron', 'B', 101);
