DROP TABLE IF EXISTS fact_sales;
DROP TABLE IF EXISTS dim_customer;
DROP TABLE IF EXISTS dim_product;
DROP TABLE IF EXISTS dim_date;

CREATE TABLE IF NOT EXISTS dim_date (
    date_id INT PRIMARY KEY,
    tmstp TIMESTAMP NOT NULL,
    date DATE NOT NULL,
    day_of_week VARCHAR(10) NOT NULL,
    month VARCHAR(10) NOT NULL,
    year INT NOT NULL
);


CREATE TABLE IF NOT EXISTS dim_product (
    product_id VARCHAR(20) PRIMARY KEY,
    product_category VARCHAR(50) NOT NULL,
    product_subcategory VARCHAR(50) NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    product_price DECIMAL(4,2) NOT NULL
);



CREATE TABLE IF NOT EXISTS dim_customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50) NOT NULL,
    customer_city VARCHAR(50) NOT NULL,
    customer_state VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_sales (
    sales_id INT PRIMARY KEY,
    sales_amount DECIMAL(10,2) NOT NULL,
    customer_id INT NOT NULL,
    date_id INT NOT NULL,
    product_id VARCHAR(20) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id)
);


COMMIT;