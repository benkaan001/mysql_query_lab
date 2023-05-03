# Triggers

Triggers are database objects that are automatically executed in response to certain events, such as changes to data in a table. A trigger can be used to enforce business rules, perform auditing or logging, or update related data in other tables.

## Types of Triggers

There are two types of triggers:

1. **Row-level triggers** - These triggers are executed once for each row affected by an SQL statement (e.g., INSERT, UPDATE, or DELETE).

2. **Statement-level triggers** - These triggers are executed once for each SQL statement that affects the trigger table, regardless of the number of rows affected.

## Syntax

The syntax for creating a trigger in MySQL is as follows:

```sql
CREATE TRIGGER trigger_name
    {BEFORE | AFTER} {INSERT | UPDATE | DELETE} ON table_name
    FOR EACH ROW
    trigger_body
```

## Usage

Triggers are useful in a variety of situations, such as:

- **Enforcing business rules** - A trigger can be used to enforce rules that are not easily enforced by constraints or other mechanisms. For example, a trigger can ensure that a discount is only applied to orders over a certain amount.

- **Performing auditing or logging** - A trigger can be used to log changes to data in a table. For example, a trigger can log all changes to a customer's account information.

- **Updating related data** - A trigger can be used to automatically update related data in other tables. For example, a trigger can update the balance of a customer's account in a separate table when a new order is placed.

## Example

Suppose we have two tables: `employees` and `employee_audit`. We want to create a trigger that logs changes to the `employees` table in the `employee_audit` table. Here's what the trigger would look like:

```sql
CREATE TRIGGER employee_audit_trigger
AFTER INSERT ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employee_audit (employee_id, action)
    VALUES (NEW.id, 'inserted');
END;
```

This trigger is executed after an `INSERT` statement is executed on the `employees` table. It logs the `id` of the newly inserted employee in the `employee_audit` table, along with the action that was taken (`inserted`). We can create similar triggers for `UPDATE` and `DELETE` statements to log changes to the `employees` table.

## Conclusion

Triggers are a powerful feature of MySQL that can be used to enforce business rules, perform auditing or logging, or update related data in other tables. They can be a valuable tool in maintaining the integrity of your database and automating certain tasks.