DROP TABLE IF EXISTS Courses;

CREATE TABLE IF NOT EXISTS Courses (
  student VARCHAR(255) NOT NULL,
  class VARCHAR(255) NOT NULL,
  PRIMARY KEY (student, class)
);

TRUNCATE TABLE Courses;

INSERT INTO Courses (student, class)
VALUES ('A', 'Math');

INSERT INTO Courses (student, class)
VALUES ('B', 'English');

INSERT INTO Courses (student, class)
VALUES ('C', 'Math');

INSERT INTO Courses (student, class)
VALUES ('D', 'Biology');

INSERT INTO Courses (student, class)
VALUES ('E', 'Math');

INSERT INTO Courses (student, class)
VALUES ('F', 'Computer');

INSERT INTO Courses (student, class)
VALUES ('G', 'Math');

INSERT INTO Courses (student, class)
VALUES ('H', 'Math');

INSERT INTO Courses (student, class)
VALUES ('I', 'Math');
