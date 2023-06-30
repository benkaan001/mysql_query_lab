DROP TABLE IF EXISTS Delivery;

CREATE TABLE IF NOT EXISTS Delivery (
  delivery_id INT NOT NULL AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date DATE NOT NULL,
  customer_pref_delivery_date DATE NOT NULL,
  PRIMARY KEY (delivery_id)
);

TRUNCATE TABLE Delivery;

INSERT INTO Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
VALUES (1, 1, '2019-08-01', '2019-08-02');

INSERT INTO Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
VALUES (2, 2, '2019-08-02', '2019-08-02');

INSERT INTO Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
VALUES (3, 1, '2019-08-11', '2019-08-12');

INSERT INTO Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
VALUES (4, 3, '2019-08-24', '2019-08-24');

INSERT INTO Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
VALUES (5, 3, '2019-08-21', '2019-08-22');

INSERT INTO Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
VALUES (6, 2, '2019-08-11', '2019-08-13');

INSERT INTO Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
VALUES (7, 4, '2019-08-09', '2019-08-09');
