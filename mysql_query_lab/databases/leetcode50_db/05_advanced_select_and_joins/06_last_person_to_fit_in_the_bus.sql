DROP TABLE IF EXISTS Queue;

CREATE TABLE IF NOT EXISTS Queue (
  person_id INT NOT NULL,
  person_name VARCHAR(30) NOT NULL,
  weight INT NOT NULL,
  turn INT NOT NULL
);

TRUNCATE TABLE Queue;

INSERT INTO Queue (person_id, person_name, weight, turn) VALUES
  (5, 'Alice', 250, 1),
  (4, 'Bob', 175, 5),
  (3, 'Alex', 350, 2),
  (6, 'John Cena', 400, 3),
  (1, 'Winston', 500, 6),
  (2, 'Marie', 200, 4);
