DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Register;

CREATE TABLE IF NOT EXISTS Users (
  user_id INT NOT NULL AUTO_INCREMENT,
  user_name VARCHAR(20) NOT NULL,
  PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS Register (
  contest_id INT NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (contest_id, user_id)
);

TRUNCATE TABLE Users;

INSERT INTO Users (user_id, user_name) VALUES
  (6, 'Alice'),
  (2, 'Bob'),
  (7, 'Alex');

TRUNCATE TABLE Register;

INSERT INTO Register (contest_id, user_id) VALUES
  (215, 6),
  (209, 2),
  (208, 2),
  (210, 6),
  (208, 6),
  (209, 7),
  (209, 6),
  (215, 7),
  (208, 7),
  (210, 2),
  (207, 2),
  (210, 7);
