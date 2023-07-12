DROP TABLE IF EXISTS RequestAccepted;

CREATE TABLE IF NOT EXISTS RequestAccepted (
  requester_id INT NOT NULL,
  accepter_id INT NULL,
  accept_date DATE NULL
);

TRUNCATE TABLE RequestAccepted;

INSERT INTO RequestAccepted (requester_id, accepter_id, accept_date)
VALUES (1, 2, '2016-06-03'),
       (1, 3, '2016-06-08'),
       (2, 3, '2016-06-08'),
       (3, 4, '2016-06-09');
