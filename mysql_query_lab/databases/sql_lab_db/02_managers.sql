CREATE TABLE employee (
  emp_id INT,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  dept_id INT,
  manager_id INT,
  office_id INT
);

CREATE TABLE department (
  dept_id INT,
  dept_name VARCHAR(50)
);

INSERT INTO employee (emp_id, first_name, last_name, dept_id, manager_id, office_id) VALUES
(1, 'Sally', 'Jones', 3, 2, 5),
(2, 'Mark', 'Smith', 2, 4, 3),
(3, 'John', 'Andrews', 1, 4, 3),
(4, 'Michelle', 'Johnson', 2, NULL, 5),
(5, 'Brian', 'Grand', 2, 2, 3);

INSERT INTO department (dept_id, dept_name) VALUES
(1, 'Sales'),
(2, 'IT'),
(3, 'Support');

COMMIT;