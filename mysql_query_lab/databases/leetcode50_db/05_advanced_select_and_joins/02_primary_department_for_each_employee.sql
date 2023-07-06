DROP TABLE IF EXISTS Employee;


CREATE TABLE IF NOT EXISTS Employee (
  employee_id INT NOT NULL,
  department_id INT NOT NULL,
  primary_flag ENUM('Y', 'N') NOT NULL,
  PRIMARY KEY (employee_id, department_id)
);

TRUNCATE TABLE Employee;

INSERT INTO Employee (employee_id, department_id, primary_flag)
VALUES (1, 1, 'N');

INSERT INTO Employee (employee_id, department_id, primary_flag)
VALUES (2, 1, 'Y');

INSERT INTO Employee (employee_id, department_id, primary_flag)
VALUES (2, 2, 'N');

INSERT INTO Employee (employee_id, department_id, primary_flag)
VALUES (3, 3, 'N');

INSERT INTO Employee (employee_id, department_id, primary_flag)
VALUES (4, 2, 'N');

INSERT INTO Employee (employee_id, department_id, primary_flag)
VALUES (4, 3, 'Y');

INSERT INTO Employee (employee_id, department_id, primary_flag)
VALUES (4, 4, 'N');
