CREATE TABLE IF NOT EXISTS Sales2 (
  sale_id INT,
  product_id INT,
  year INT,
  quantity INT,
  price INT
);

CREATE TABLE IF NOT EXISTS Product2 (
  product_id INT,
  product_name VARCHAR(10)
);

TRUNCATE TABLE Sales2;

INSERT INTO Sales2 (sale_id, product_id, year, quantity, price) VALUES (1, 100, 2008, 10, 5000);
INSERT INTO Sales2 (sale_id, product_id, year, quantity, price) VALUES (2, 100, 2009, 12, 5000);
INSERT INTO Sales2 (sale_id, product_id, year, quantity, price) VALUES (7, 200, 2011, 15, 9000);

TRUNCATE TABLE Product2;

INSERT INTO Product2 (product_id, product_name) VALUES (100, 'Nokia');
INSERT INTO Product2 (product_id, product_name) VALUES (200, 'Apple');
INSERT INTO Product2 (product_id, product_name) VALUES (300, 'Samsung');
