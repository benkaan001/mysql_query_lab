DROP TABLE IF EXISTS Queries;

CREATE TABLE IF NOT EXISTS Queries (
  query_name VARCHAR(30) NOT NULL,
  result VARCHAR(50) NOT NULL,
  position INT NOT NULL,
  rating INT NOT NULL
);

TRUNCATE TABLE Queries;

INSERT INTO Queries (query_name, result, position, rating) VALUES
  ('Dog', 'Golden Retriever', 1, 5),
  ('Dog', 'German Shepherd', 2, 5),
  ('Dog', 'Mule', 200, 1),
  ('Cat', 'Shirazi', 5, 2),
  ('Cat', 'Siamese', 3, 3),
  ('Cat', 'Sphynx', 7, 4);
