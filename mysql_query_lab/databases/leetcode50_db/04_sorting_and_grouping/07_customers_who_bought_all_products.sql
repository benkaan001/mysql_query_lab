DROP TABLE IF EXISTS Customer;

DROP TABLE IF EXISTS Product;

CREATE TABLE IF NOT EXISTS Customer (
  customer_id INT NOT NULL,
  product_key INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Product (
  product_key INT NOT NULL,
  PRIMARY KEY (product_key)
);

TRUNCATE TABLE Customer;

INSERT INTO Customer (customer_id, product_key)
VALUES (1, 5);

INSERT INTO Customer (customer_id, product_key)
VALUES (2, 6);

INSERT INTO Customer (customer_id, product_key)
VALUES (3, 5);

INSERT INTO Customer (customer_id, product_key)
VALUES (3, 6);

INSERT INTO Customer (customer_id, product_key)
VALUES (1, 6);

TRUNCATE TABLE Product;

INSERT INTO Product (product_key)
VALUES (5);

INSERT INTO Product (product_key)
VALUES (6);
