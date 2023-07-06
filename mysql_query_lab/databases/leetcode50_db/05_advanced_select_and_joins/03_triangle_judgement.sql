DROP TABLE IF EXISTS Triangle;


CREATE TABLE IF NOT EXISTS Triangle (
  x INT NOT NULL,
  y INT NOT NULL,
  z INT NOT NULL,
  PRIMARY KEY (x, y, z)
);

TRUNCATE TABLE Triangle;

INSERT INTO Triangle (x, y, z)
VALUES (13, 15, 30);

INSERT INTO Triangle (x, y, z)
VALUES (10, 20, 15);
