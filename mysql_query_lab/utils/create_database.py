import mysql.connector
from mysql.connector import errorcode
from utils.config import MYSQL_CONFIG

def create_mysql_database(db_name):
    """
    Create a MySQL database with the provided name using the credentials specified in MYSQL_CONFIG.

    Args:
        db_name (str): The name of the database to create.

    Returns:
        None

    Raises:
        mysql.connector.Error: If there is an error creating the database.
    """
    try:
        # Connect to MySQL server
        with mysql.connector.connect(
            host=MYSQL_CONFIG["host"],
            user=MYSQL_CONFIG["user"],
            password=MYSQL_CONFIG["password"]) as conn:

            # Create cursor object
            with conn.cursor() as cursor:

                # Drop the database if it already exists
                cursor.execute(f"DROP DATABASE IF EXISTS {db_name};")

                # Create the new database
                cursor.execute(f"CREATE DATABASE {db_name};")

            # Commit the transaction
            conn.commit()

            # Print success message
            print(f"Database {db_name} created successfully")

    except mysql.connector.Error as err:
        # Handle any MySQL errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print("MySQL Error:", err)
