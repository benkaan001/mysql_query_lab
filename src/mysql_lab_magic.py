import re

import pandas as pd
import sqlalchemy
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.display import Markdown, display
from sqlalchemy import text


def _clean_sql_query(cell_content: str) -> str:
    """Removes leading/trailing whitespace and full-line comments."""
    lines = []
    for line in cell_content.strip().splitlines():
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith("--"):
            lines.append(line)
    return "\n".join(lines).strip()


@magics_class
class MySQLLabMagic(Magics):
    """
    Custom IPython magic to execute SQL queries against a SQLAlchemy engine
    ('db_engine'). Supports variable assignment and non-SELECT statements.
    """

    @cell_magic
    def mysql_lab(self, line, cell):
        var_name = None
        match = re.match(r"^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*<<", line)
        if match:
            var_name = match.group(1).strip()

        user_ns = self.shell.user_ns
        engine_variable_name = "db_engine"

        if engine_variable_name not in user_ns or user_ns[engine_variable_name] is None:
            print(
                "Error: SQLAlchemy engine object named "
                f"'{engine_variable_name}' not found or not initialized."
            )
            print("Please run the notebook setup cell successfully first.")
            return

        engine = user_ns[engine_variable_name]

        if not isinstance(engine, sqlalchemy.engine.Engine):
            print(
                f""""Error: Variable '{engine_variable_name}' is not a valid
                SQLAlchemy Engine object."""
            )
            return

        sql_query = _clean_sql_query(cell)
        if not sql_query:
            print("No executable SQL query found in the cell (ignoring comments).")
            return

        is_select_statement = (
            sql_query.lower().lstrip().startswith("select")
            or sql_query.lower().lstrip().startswith("with")
            or sql_query.lower().lstrip().startswith("show")
        )

        try:
            if is_select_statement:
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
                    display(df)
            else:
                with engine.connect() as connection:
                    trans = connection.begin()
                    try:
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
                                    "Statement executed successfully. "
                                    f"{rowcount} rows affected."
                                )
                            )
                    except Exception as e_inner:
                        print(
                            "Error during non-SELECT execution, "
                            "rolling back transaction."
                        )
                        trans.rollback()
                        raise e_inner

        except Exception as e:
            print(f"An error occurred during SQL execution:\n{e}")
            print("\n--- Query Executed ---")
            print(sql_query)
            print("----------------------")


def load_ipython_extension(ipython):
    ipython.register_magics(MySQLLabMagic)
