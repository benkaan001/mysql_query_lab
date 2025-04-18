# src/mysql_lab_magic.py
# Defines the custom %%mysql_lab cell magic for IPython/Jupyter.

import re
import pandas as pd
import sqlalchemy
from sqlalchemy import text # Import text construct for non-SELECT statements
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.display import display, Markdown


@magics_class
class MySQLLabMagic(Magics):
    """
    A custom IPython magic to execute SQL queries against a predefined
    SQLAlchemy engine object ('db_engine') in the user's namespace.

    Supports assigning results to variables (e.g., `df << %%mysql_lab`)
    and basic execution of non-SELECT statements.
    """

    @cell_magic
    def mysql_lab(self, line, cell):
        """
        Executes the SQL code in the cell.
        For SELECT queries, displays results as a DataFrame or assigns to a variable.
        For non-SELECT, executes and reports rows affected.

        Usage:
            %%mysql_lab
            SELECT * FROM your_table;

            my_var << %%mysql_lab
            SELECT * FROM another_table;

            %%mysql_lab
            INSERT INTO your_table (...) VALUES (...);
        """
        # Parse the line for variable assignment (e.g., "my_var <<")
        var_name = None
        # Regex to capture variable name before '<<'
        match = re.match(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*<<', line)
        if match:
            var_name = match.group(1).strip()
            # print(f"Assigning result to variable: {var_name}") # Debugging

        # Get the SQLAlchemy engine from the user's namespace
        user_ns = self.shell.user_ns
        engine_variable_name = 'db_engine' # Expect the engine in this variable

        if engine_variable_name not in user_ns:
            print(f"Error: SQLAlchemy engine object named '{engine_variable_name}' not found.")
            print("Please run the notebook setup cell first.")
            return

        engine = user_ns[engine_variable_name]

        if not isinstance(engine, sqlalchemy.engine.Engine):
             print(f"Error: Variable '{engine_variable_name}' is not a valid SQLAlchemy Engine object.")
             return

        # The SQL query is the content of the cell
        sql_query = cell.strip()

        if not sql_query:
            print("No SQL query provided in the cell.")
            return

        # Determine if it's likely a SELECT statement (basic check)
        is_select_statement = sql_query.lower().lstrip().startswith('select') or \
                              sql_query.lower().lstrip().startswith('with') or \
                              sql_query.lower().lstrip().startswith('show')

        try:
            if is_select_statement:
                # Execute SELECT using pandas
                # print(f"Executing SELECT query:\n{sql_query}") # Debugging
                df = pd.read_sql(sql_query, engine)
                if var_name:
                    # Assign to variable in user namespace
                    user_ns[var_name] = df
                    print(f"Query executed. Result assigned to variable '{var_name}'.")
                    # Optionally display a preview
                    # display(df.head())
                elif df is None:
                     # Should not happen with read_sql unless query returns nothing meaningful
                     display(Markdown("Query executed successfully, but returned no results."))
                elif df.empty:
                     display(Markdown("Query executed successfully. Result is empty."))
                     # Optionally display empty DataFrame with columns
                     # display(df)
                else:
                     display(df) # Display the resulting DataFrame
            else:
                # Execute non-SELECT statement (INSERT, UPDATE, DELETE, CREATE, etc.)
                # print(f"Executing non-SELECT statement:\n{sql_query}") # Debugging
                with engine.connect() as connection:
                    trans = connection.begin() # Start transaction
                    try:
                        result = connection.execute(text(sql_query))
                        trans.commit() # Commit transaction
                        # Report rows affected if available (not always applicable)
                        rowcount = result.rowcount if hasattr(result, 'rowcount') else -1
                        if rowcount == -1:
                             display(Markdown(f"Non-SELECT statement executed successfully."))
                        elif rowcount == 0:
                             display(Markdown(f"Statement executed successfully. 0 rows affected."))
                        else:
                             display(Markdown(f"Statement executed successfully. {rowcount} rows affected."))
                    except Exception as e_inner:
                         print(f"Error during non-SELECT execution, rolling back transaction.") # Info
                         trans.rollback() # Rollback on error
                         raise e_inner # Re-raise the exception

        except Exception as e:
            print(f"An error occurred during SQL execution:\n{e}")


def load_ipython_extension(ipython):
    """Register the %%mysql_lab magic."""
    print("--- Registering FULL MySQLLabMagic ---") # Add print statement here
    ipython.register_magics(MySQLLabMagic)

print("--- Finished defining FULL mysql_lab_magic.py ---") # Add print statement here
