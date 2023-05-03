# Partitioning in MySQL

Partitioning is a technique used in MySQL to divide large tables into smaller, more manageable parts. It is a way to horizontally partition a table, which means that a table is divided into smaller sub-tables based on some criteria. Each sub-table is called a partition and can be stored in different physical locations. Partitioning can improve query performance, reduce query execution time, and improve the manageability of large tables.

## Types of Partitioning in MySQL

MySQL supports several types of partitioning:

- **Range partitioning**: In this type of partitioning, data is divided based on a specified range of values. For example, a table can be partitioned based on dates, where each partition contains data for a specific range of dates.
- **List partitioning**: In this type of partitioning, data is divided based on a specific set of values. For example, a table can be partitioned based on regions, where each partition contains data for a specific region.
- **Hash partitioning**: In this type of partitioning, data is divided based on a hashing algorithm applied to a specific column. This ensures that data is uniformly distributed across all partitions.
- **Key partitioning**: In this type of partitioning, data is divided based on the values of the primary key or unique key columns.

## Creating a Partitioned Table in MySQL

To create a partitioned table in MySQL, you can use the `CREATE TABLE` statement with the `PARTITION BY` clause. Here's an example:

```sql
CREATE TABLE sales (
    id INT,
    date DATE,
    amount DECIMAL(10,2)
)
PARTITION BY RANGE( YEAR(date) ) (
    PARTITION p0 VALUES LESS THAN (2010),
    PARTITION p1 VALUES LESS THAN (2011),
    PARTITION p2 VALUES LESS THAN (2012),
    PARTITION p3 VALUES LESS THAN (2013),
    PARTITION p4 VALUES LESS THAN (2014)
);
```

In this example, the `sales` table is partitioned by range on the `date` column. The `PARTITION BY` clause specifies the partitioning type and the partitioning key. The `RANGE` keyword specifies that the partitioning is based on a range of values. The `YEAR(date)` function is used to extract the year from the `date` column, which is used as the partitioning key.

The `PARTITION` clause specifies the individual partitions, each with a name (`p0`, `p1`, `p2`, `p3`, and `p4`) and a value range. In this example, the table is partitioned into 5 partitions based on the year: `p0` contains data for years before 2010, `p1` contains data for 2010, `p2` contains data for 2011, and so on.

## Querying a Partitioned Table in MySQL

Once you have created a partitioned table, you can query it using the same SQL statements you would use on a non-partitioned table. However, MySQL will automatically prune the partitions that do not contain the data you are querying, which can significantly improve query performance.

Here's an example query on the `sales` table:

```sql
SELECT YEAR(date) AS year, SUM(amount) AS total
FROM sales
WHERE date BETWEEN '2010-01-01' AND '2013-12-31'
GROUP BY YEAR(date);
```

This query returns the total sales amount for each year between 2010 and 2013. Since the `sales` table is partitioned by year, MySQL will only scan the partitions that contain data for the specified years. This