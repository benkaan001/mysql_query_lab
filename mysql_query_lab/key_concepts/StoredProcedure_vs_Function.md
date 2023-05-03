## Stored Procedures and Functions

Stored procedures and functions are database objects that contain a collection of SQL statements that can be executed as a single unit. They are used to encapsulate complex logic and operations that are frequently performed in an application or database.

### Stored Procedures

A stored procedure is a collection of SQL statements that are stored in the database and can be executed as a single unit. It can accept input parameters and can return multiple output parameters. Stored procedures can be used to encapsulate complex business logic, reduce network traffic, and improve performance by reducing the number of round trips to the database.

To create a stored procedure, you can use the `CREATE PROCEDURE` statement followed by the SQL statements that make up the procedure. Here is an example of a stored procedure that accepts an input parameter and returns a result set:

```sql
CREATE PROCEDURE get_orders_by_customer_id (IN customer_id INT)
BEGIN
    SELECT * FROM orders WHERE customer_id = customer_id;
END
```

To execute the stored procedure, you can use the `CALL` statement followed by the name of the procedure and the input parameter values:

```sql
CALL get_orders_by_customer_id(1234);
```

### Functions

A function is a database object that returns a single value based on the input parameters. Unlike stored procedures, functions cannot modify the database or perform any operations that have side effects. They are used to encapsulate frequently used calculations or transformations that can be reused across multiple queries or procedures.

To create a function, you can use the `CREATE FUNCTION` statement followed by the SQL statements that make up the function. Here is an example of a function that accepts an input parameter and returns a single value:

```sql
CREATE FUNCTION get_total_order_amount (customer_id INT)
RETURNS DECIMAL(10,2)
BEGIN
    DECLARE total_amount DECIMAL(10,2);
    SELECT SUM(order_total) INTO total_amount FROM orders WHERE customer_id = customer_id;
    RETURN total_amount;
END
```

To use the function in a query, you can simply call it like any other function:

```sql
SELECT customer_id, get_total_order_amount(customer_id) as total_amount FROM orders;
```

### Conclusion

Stored procedures and functions are powerful tools for encapsulating and reusing complex logic in databases. They can improve performance, reduce network traffic, and make it easier to maintain and modify database code. By using stored procedures and functions in your database applications, you can improve scalability and reduce maintenance costs over time.