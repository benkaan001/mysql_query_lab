DROP TABLE IF EXISTS Products;

CREATE TABLE IF NOT EXISTS Products (
  product_id INT NOT NULL,
  new_price INT NOT NULL,
  change_date DATE NOT NULL
);

TRUNCATE TABLE Products;

INSERT INTO Products (product_id, new_price, change_date) VALUES
  (1, 20, '2019-08-14'),
  (2, 50, '2019-08-14'),
  (1, 30, '2019-08-15'),
  (1, 35, '2019-08-16'),
  (2, 65, '2019-08-17'),
  (3, 20, '2019-08-18');
