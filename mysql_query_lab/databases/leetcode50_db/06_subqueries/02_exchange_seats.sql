DROP TABLE IF EXISTS Seat;

CREATE TABLE IF NOT EXISTS Seat (
  id INT NOT NULL,
  student VARCHAR(255) NOT NULL
);

TRUNCATE TABLE Seat;

INSERT INTO Seat (id, student) VALUES
  (1, 'Abbot'),
  (2, 'Doris'),
  (3, 'Emerson'),
  (4, 'Green'),
  (5, 'Jeames');
