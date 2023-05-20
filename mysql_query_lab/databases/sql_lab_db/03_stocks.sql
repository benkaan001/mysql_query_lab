-- Create the stock_price table
CREATE TABLE stock_price(
    stock_name VARCHAR(20),
    price_date DATE,
    opening_price DECIMAL(10, 2),
    closing_price DECIMAL(10, 2)
);

-- Insert dummy data for Apple
INSERT INTO stock_price (stock_name, price_date, opening_price, closing_price)
VALUES ('Apple', '2023-01-01', 150.00, 155.00),
       ('Apple', '2023-01-02', 155.00, 160.00),
       ('Apple', '2023-01-03', 160.00, 165.00),
       ('Apple', '2023-01-04', 165.00, 170.00),
       ('Apple', '2023-01-05', 170.00, 165.00);

-- Insert dummy data for Microsoft
INSERT INTO stock_price (stock_name, price_date, opening_price, closing_price)
VALUES ('Microsoft', '2023-01-01', 210.00, 205.00),
       ('Microsoft', '2023-01-02', 205.00, 210.00),
       ('Microsoft', '2023-01-03', 210.00, 215.00),
       ('Microsoft', '2023-01-04', 215.00, 220.00),
       ('Microsoft', '2023-01-05', 220.00, 215.00);

