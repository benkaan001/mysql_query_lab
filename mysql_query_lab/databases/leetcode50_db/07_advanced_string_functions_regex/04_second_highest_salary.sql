DROP TABLE IF EXISTS Employee;

CREATE TABLE IF NOT EXISTS Employee (
  id INT,
  salary INT
);

TRUNCATE TABLE Employee;

INSERT INTO Employee (id, salary)
VALUES (1, 100),
       (2, 200),
       (3, 300);
