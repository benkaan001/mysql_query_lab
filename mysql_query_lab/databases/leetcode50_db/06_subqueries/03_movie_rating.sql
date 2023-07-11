DROP TABLE IF EXISTS  Movies;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS MovieRating;

CREATE TABLE IF NOT EXISTS Movies (
  movie_id INT NOT NULL,
  title VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS Users (
  user_id INT NOT NULL,
  name VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS MovieRating (
  movie_id INT NOT NULL,
  user_id INT NOT NULL,
  rating INT NOT NULL,
  created_at DATE NOT NULL
);

TRUNCATE TABLE Movies;

INSERT INTO Movies (movie_id, title) VALUES
  (1, 'Avengers'),
  (2, 'Frozen 2'),
  (3, 'Joker');

TRUNCATE TABLE Users;

INSERT INTO Users (user_id, name) VALUES
  (1, 'Daniel'),
  (2, 'Monica'),
  (3, 'Maria'),
  (4, 'James');

TRUNCATE TABLE MovieRating;

INSERT INTO MovieRating (movie_id, user_id, rating, created_at) VALUES
  (1, 1, 3, '2020-01-12'),
  (1, 2, 4, '2020-02-11'),
  (1, 3, 2, '2020-02-12'),
  (1, 4, 1, '2020-01-01'),
  (2, 1, 5, '2020-02-17'),
  (2, 2, 2, '2020-02-01'),
  (2, 3, 2, '2020-03-01'),
  (3, 1, 3, '2020-02-22'),
  (3, 2, 4, '2020-02-25');
