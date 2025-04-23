# src/mysql_lab_magic.py
# Defines the custom %%mysql_lab cell magic for IPython/Jupyter.
# --- v2: With comment handling fix ---

import re

import pandas as pd
import sqlalchemy
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.display import Markdown, display
from sqlalchemy import text  # Import text construct for non-SELECT statements

print("--- Importing FULL mysql_lab_magic.py (v2: comment handling fix) ---")


def _clean_sql_query(cell_content: str) -> str:
    """Removes leading/trailing whitespace and full-line comments."""
    lines = []
    for line in cell_content.strip().splitlines():
        stripped_line = line.strip()
        # Also ignore inline comments starting with -- if they take the whole logical part
        # This is a basic check; complex inline comments might still pass
        if stripped_line and not stripped_line.startswith("--"):
            lines.append(
                line
            )  # Keep original line spacing if needed, just filter comments
    return "\n".join(lines).strip()


@magics_class
class MySQLLabMagic(Magics):
    """
    A custom IPython magic to execute SQL queries against a predefined
    SQLAlchemy engine object ('db_engine') in the user's namespace.

    Supports assigning results to variables (e.g., `df << %%mysql_lab`)
    and basic execution of non-SELECT statements. Handles comments.
    NOTE: Requires manual escaping of '%' to '%%' in LIKE clauses.
    """

    @cell_magic
    def mysql_lab(self, line, cell):
        """
        Executes the SQL code in the cell (ignoring comment lines).
        For SELECT queries, displays results as a DataFrame or assigns to a variable.
        For non-SELECT, executes and reports rows affected.
        Requires manual '%%' for literal percent signs in LIKE clauses.
        """
        # Parse the line for variable assignment (e.g., "my_var <<")
        var_name = None
        match = re.match(r"^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*<<", line)
        if match:
            var_name = match.group(1).strip()

        # Get the SQLAlchemy engine from the user's namespace
        user_ns = self.shell.user_ns
        engine_variable_name = "db_engine"

        if engine_variable_name not in user_ns or user_ns[engine_variable_name] is None:
            print(
                f"Error: SQLAlchemy engine object named '{engine_variable_name}' not found or not initialized."
            )
            print("Please run the notebook setup cell successfully first.")
            return

        engine = user_ns[engine_variable_name]

        if not isinstance(engine, sqlalchemy.engine.Engine):
            print(
                f"Error: Variable '{engine_variable_name}' is not a valid SQLAlchemy Engine object."
            )
            return

        # --- Clean the SQL query from the cell ---
        sql_query = _clean_sql_query(cell)  # Use the cleaned query

        if not sql_query:
            print("No executable SQL query found in the cell (ignoring comments).")
            return

        # Determine if it's likely a SELECT statement (basic check on cleaned query)
        is_select_statement = (
            sql_query.lower().lstrip().startswith("select")
            or sql_query.lower().lstrip().startswith("with")
            or sql_query.lower().lstrip().startswith("show")
        )

        try:
            if is_select_statement:
                # Execute SELECT using pandas on the cleaned query
                # print(f"Executing SELECT query:\n{sql_query}") # Debugging
                df = pd.read_sql(sql_query, engine)
                if var_name:
                    user_ns[var_name] = df
                    print(f"Query executed. Result assigned to variable '{var_name}'.")
                elif df is None:
                    display(
                        Markdown(
                            "Query executed successfully, but returned no results."
                        )
                    )
                elif df.empty:
                    display(Markdown("Query executed successfully. Result is empty."))
                else:
                    display(df)  # Display the DataFrame
            else:
                # Execute non-SELECT statement on the cleaned query
                # print(f"Executing non-SELECT statement:\n{sql_query}") # Debugging
                with engine.connect() as connection:
                    trans = connection.begin()
                    try:
                        # Use text() construct for non-SELECT
                        result = connection.execute(text(sql_query))
                        trans.commit()
                        rowcount = (
                            result.rowcount if hasattr(result, "rowcount") else -1
                        )
                        if rowcount == -1:
                            display(
                                Markdown("Non-SELECT statement executed successfully.")
                            )
                        elif rowcount == 0:
                            display(
                                Markdown(
                                    "Statement executed successfully. 0 rows affected."
                                )
                            )
                        else:
                            display(
                                Markdown(
                                    f"Statement executed successfully. {rowcount} rows affected."
                                )
                            )
                    except Exception as e_inner:
                        print(
                            "Error during non-SELECT execution, rolling back transaction."
                        )
                        trans.rollback()
                        raise e_inner

        except Exception as e:
            # Show the query that caused the error
            print(f"An error occurred during SQL execution:\n{e}")
            print("\n--- Query Executed ---")
            print(sql_query)  # Show the cleaned query
            print("----------------------")


def load_ipython_extension(ipython):
    """Register the %%mysql_lab magic."""
    print("--- Registering FULL MySQLLabMagic (v2: comment handling fix) ---")
    ipython.register_magics(MySQLLabMagic)


print("--- Finished defining FULL mysql_lab_magic.py (v2: comment handling fix) ---")
