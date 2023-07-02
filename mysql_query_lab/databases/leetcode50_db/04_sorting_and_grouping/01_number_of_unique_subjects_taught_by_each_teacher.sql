DROP TABLE IF EXISTS Teacher;

CREATE TABLE IF NOT EXISTS Teacher (
  teacher_id INT NOT NULL,
  subject_id INT NOT NULL,
  dept_id INT NOT NULL,
  PRIMARY KEY (teacher_id, subject_id, dept_id)
);

TRUNCATE TABLE Teacher;

INSERT INTO Teacher (teacher_id, subject_id, dept_id)
VALUES (1, 2, 3);

INSERT INTO Teacher (teacher_id, subject_id, dept_id)
VALUES (1, 2, 4);

INSERT INTO Teacher (teacher_id, subject_id, dept_id)
VALUES (1, 3, 3);

INSERT INTO Teacher (teacher_id, subject_id, dept_id)
VALUES (2, 1, 1);

INSERT INTO Teacher (teacher_id, subject_id, dept_id)
VALUES (2, 2, 1);

INSERT INTO Teacher (teacher_id, subject_id, dept_id)
VALUES (2, 3, 1);

INSERT INTO Teacher (teacher_id, subject_id, dept_id)
VALUES (2, 4, 1);
