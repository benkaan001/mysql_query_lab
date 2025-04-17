# src/load_data.py
# Script to load data from a CSV file into the MySQL database.

import os
import logging
import argparse
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(csv_file_path):
    """
    Loads data from a specified CSV file into the 'departments' table in the MySQL database.
    """
    # Load environment variables from .env file
    load_dotenv()
    db_user = os.getenv("MYSQL_USER")
    db_password = os.getenv("MYSQL_PASSWORD")
    db_name = os.getenv("MYSQL_DATABASE")
    # db_host = "127.0.0.1" # Standard host for mapped port
    db_host = "localhost" # Alternative host to try
    db_port = "3307"

    # --- TEMPORARY DEBUGGING ---
    # Print the credentials the script is actually using.
    # REMOVE THIS BLOCK AFTER DEBUGGING!
    print("-" * 20 + " DEBUGGING " + "-" * 20)
    print(f"Attempting connection with:")
    print(f"  Host: {db_host}")
    print(f"  Port: {db_port}")
    print(f"  User: {db_user}")
    # Avoid printing password directly if possible, check if it's loaded:
    print(f"  Password Loaded: {'YES' if db_password else 'NO'}")
    print(f"  Database: {db_name}")
    print("-" * 50)
    # --- END TEMPORARY DEBUGGING ---


    # Validate that environment variables are loaded
    if not all([db_user, db_password, db_name]):
        logging.error("Database credentials or name not found in environment variables. Ensure .env file is set and loaded correctly.")
        return

    # Construct database connection URL for SQLAlchemy
    # Format: mysql+mysqlconnector://user:password@host:port/database
    db_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    try:
        # Create SQLAlchemy engine
        engine = create_engine(db_url)
        logging.info(f"Successfully created database engine for {db_name}")

        # Read data from CSV file using pandas
        logging.info(f"Reading data from {csv_file_path}...")
        df = pd.read_csv(csv_file_path)
        logging.info(f"Read {len(df)} rows from CSV.")

        # Define the target table name
        table_name = "departments" # Matches the table created in 01_schema.sql

        # Load data into the MySQL table
        # 'if_exists'='append': Adds data. If run again, it will add duplicates unless constraints prevent it.
        # Consider 'replace' if you want to drop and recreate the table each time (careful!).
        # For true idempotency, more complex logic (checking existence) might be needed.
        logging.info(f"Loading data into table '{table_name}'...")
        with engine.connect() as connection:
             # Optional: Clear the table before loading if you want a fresh load each time
             # logging.warning(f"Clearing existing data from table '{table_name}'...")
             # connection.execute(text(f"TRUNCATE TABLE {table_name}")) # Use with caution!

             df.to_sql(name=table_name, con=connection, if_exists='append', index=False)

        logging.info(f"Successfully loaded {len(df)} rows into '{table_name}'.")

    except FileNotFoundError:
        logging.error(f"Error: CSV file not found at {csv_file_path}")
    except pd.errors.EmptyDataError:
        logging.error(f"Error: CSV file {csv_file_path} is empty.")
    except Exception as e:
        logging.error(f"An error occurred during data loading: {e}")
        # Consider more specific error handling for database errors (e.g., sqlalchemy.exc.IntegrityError)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Load data from a CSV file into the MySQL database.")
    parser.add_argument("csv_file", help="Path to the CSV file to load.")

    # Parse arguments
    args = parser.parse_args()

    # Call the main function
    load_data(args.csv_file)
