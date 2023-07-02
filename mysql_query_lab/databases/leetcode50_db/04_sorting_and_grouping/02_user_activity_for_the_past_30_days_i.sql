DROP TABLE IF EXISTS Activity;

CREATE TABLE IF NOT EXISTS Activity (
  user_id INT NOT NULL,
  session_id INT NOT NULL,
  activity_date DATE NOT NULL,
  activity_type ENUM('open_session', 'end_session', 'scroll_down', 'send_message') NOT NULL
);

TRUNCATE TABLE Activity;

INSERT INTO Activity (user_id, session_id, activity_date, activity_type)
VALUES (1, 1, '2019-07-20', 'open_session');

INSERT INTO Activity (user_id, session_id, activity_date, activity_type)
VALUES (1, 1, '2019-07-20', 'scroll_down');

INSERT INTO Activity (user_id, session_id, activity_date, activity_type)
VALUES (1, 1, '2019-07-20', 'end_session');

INSERT INTO Activity (user_id, session_id, activity_date, activity_type)
VALUES (2, 4, '2019-07-20', 'open_session');

INSERT INTO Activity (user_id, session_id, activity_date, activity_type)
VALUES (2, 4, '2019-07-21', 'send_message');

INSERT INTO Activity (user_id, session_id, activity_date, activity_type)
VALUES (2, 4, '2019-07-21', 'end_session');

INSERT INTO Activity (user_id, session_id, activity_date, activity_type)
VALUES (3, 2, '2019-07-21', 'open_session');

INSERT INTO Activity (user_id, session_id, activity_date, activity_type)
VALUES (3, 2, '2019-07-21', 'send_message');

INSERT INTO Activity (user_id, session_id, activity_date, activity_type)
VALUES (3, 2, '2019-07-21', 'end_session');

INSERT INTO Activity (user_id, session_id, activity_date, activity_type)
VALUES (4, 3, '2019-06-25', 'open_session');

INSERT INTO Activity (user_id, session_id, activity_date, activity_type)
VALUES (4, 3, '2019-06-25', 'end_session');
