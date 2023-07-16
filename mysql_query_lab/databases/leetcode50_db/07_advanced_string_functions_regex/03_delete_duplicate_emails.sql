DROP TABLE IF EXISTS Person;

CREATE TABLE IF NOT EXISTS Person (
  Id INT,
  Email VARCHAR(255)
);

TRUNCATE TABLE Person;

INSERT INTO Person (Id, Email)
VALUES (1, 'john@example.com'),
       (2, 'bob@example.com'),
       (3, 'john@example.com');
