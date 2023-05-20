-- Recreate table
DROP TABLE IF EXISTS stock_price;

-- Create the stock_price table
CREATE TABLE stock_price(
    stock_name VARCHAR(20),
    price_date DATE,
    closing_price DECIMAL(10, 2)
);

-- Insert dummy data for Apple
INSERT INTO stock_price (stock_name, price_date, closing_price)
VALUES ('Apple', '2023-01-01', 155.00),
       ('Apple', '2023-01-02', 160.00),
       ('Apple', '2023-01-03', 143.00),
       ('Apple', '2023-01-04', 169.00),
       ('Apple', '2023-01-05', 162.00);

-- Insert dummy data for Microsoft
INSERT INTO stock_price (stock_name, price_date, closing_price)
VALUES ('Microsoft', '2023-01-01', 205.00),
       ('Microsoft', '2023-01-02', 211.00),
       ('Microsoft', '2023-01-03', 202.00),
       ('Microsoft', '2023-01-04', 226.00),
       ('Microsoft', '2023-01-05', 214.00);

