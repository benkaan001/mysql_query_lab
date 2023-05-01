CREATE TABLE registrations (
  ID int PRIMARY KEY,
  FIRST_NAME varchar(255),
  LAST_NAME varchar(255),
  ADDRESS_STATE varchar(255),
  REGISTER_DATE datetime
);

INSERT INTO registrations (ID, FIRST_NAME, LAST_NAME, ADDRESS_STATE, REGISTER_DATE) VALUES
(1, 'Emma', 'Gonzales', 'Florida', '2022-01-01 06:06:00'),
(2, 'Avery', 'Jordan', 'West Virginia', '2021-09-23 05:04:00'),
(3, 'Liam', 'Murphy', 'California', '2020-11-16 22:34:00'),
(4, 'Olivia', 'Moore', 'Florida', '2020-04-15 15:26:00'),
(5, 'Noah', 'Bishop', 'New Jersey', '2023-04-04 15:22:00'),
(6, 'Sophia', 'White', 'Michigan', NULL),
(7, 'Jackson', 'Black', 'Ohio', '2020-07-02 06:34:00'),
(8, 'Isabella', 'Crawford', 'California', '2020-03-15 14:07:00'),
(9, 'Lucas', 'Simmons', 'Wisconsin', '2021-08-18 06:10:00'),
(10, 'Mia', 'Kelly', 'Georgia', '2020-01-21 03:54:00'),
(11, 'Ethan', 'Hunt', 'Arizona', '2022-05-16 03:57:00'),
(12, 'Alexander', 'Daniels', 'Texas', '2023-06-25 11:30:00'),
(13, 'Ava', 'Torres', 'Alabama', '2021-12-04 08:20:00'),
(14, 'Charlotte', 'Sims', 'Tennessee', '2020-05-04 07:16:00'),
(15, 'Luna', 'Stevens', 'Nevada', '2022-12-26 02:48:00'),
(16, 'Elijah', 'Freeman', 'Illinois', '2023-01-21 23:40:00'),
(17, 'Harper', 'Castillo', 'Georgia', '2021-08-14 13:36:00'),
(18, 'Henry', 'Rose', 'District of Columbia', '2020-10-20 14:11:00'),
(19, 'William', 'Scott', 'California', '2022-03-03 02:23:00'),
(20, 'Grace', 'Ferguson', 'California', '2023-05-23 05:24:00');

COMMIT;