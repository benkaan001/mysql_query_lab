DROP TABLE IF EXISTS Activities;

CREATE TABLE IF NOT EXISTS Activities (
  sell_date DATE,
  product VARCHAR(20)
);

TRUNCATE TABLE Activities;

INSERT INTO Activities (sell_date, product)
VALUES ('2020-05-30', 'Headphone'),
       ('2020-06-01', 'Pencil'),
       ('2020-06-02', 'Mask'),
       ('2020-05-30', 'Basketball'),
       ('2020-06-01', 'Bible'),
       ('2020-06-02', 'Mask'),
       ('2020-05-30', 'T-Shirt');
