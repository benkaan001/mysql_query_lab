DROP TABLE IF EXISTS Logs;

CREATE TABLE IF NOT EXISTS Logs (
  id INT,
  num INT
);

TRUNCATE TABLE Logs;

INSERT INTO Logs (id, num) VALUES
  (1, 1),
  (2, 1),
  (3, 1),
  (4, 2),
  (5, 1),
  (6, 2),
  (7, 2);
