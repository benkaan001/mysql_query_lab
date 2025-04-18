# src/load_data.py
# Script to load data from a CSV file into the MySQL database.

import argparse
import logging
import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_data(csv_file_path):
    """
    Loads data from a specified CSV file into the 'departments' table
    in the MySQL database.
    """
    # Load environment variables from .env file
    load_dotenv()
    db_user = os.getenv("MYSQL_USER")
    db_password = os.getenv("MYSQL_PASSWORD")
    db_name = os.getenv("MYSQL_DATABASE")
    db_host = os.getenv("DB_HOST", "127.0.0.1")  # Connect to localhost/127.0.0.1
    # --- IMPORTANT: Use the HOST port mapped in docker-compose.yml ---
    db_port = os.getenv("DB_PORT", "3307")  # Use the correct host port

    # Validate that environment variables are loaded
    if not all([db_user, db_password, db_name]):
        logging.error(
            "Database credentials or name not found in environment variables. "
            "Ensure .env file is set and loaded correctly."
        )
        return

    # Construct database connection URL for SQLAlchemy using pymysql
    # Format: mysql+pymysql://user:password@host:port/database
    db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    logging.info(
        f"Attempting connection using pymysql to: {db_host}:{db_port} as user {db_user}"
    )

    try:
        # Create SQLAlchemy engine
        engine = create_engine(db_url)
        logging.info(f"Successfully created database engine for {db_name}")

        # Read data from CSV file using pandas
        logging.info(f"Reading data from {csv_file_path}...")
        df = pd.read_csv(csv_file_path)
        logging.info(f"Read {len(df)} rows from CSV.")

        # Define the target table name
        table_name = "departments"  # Matches the table created in 01_schema.sql

        # --- Use engine directly with pandas.to_sql ---
        # This is generally the recommended approach as Pandas can manage
        # the connection context for the to_sql operation.
        logging.info(f"Loading data into table '{table_name}' using engine...")
        df.to_sql(name=table_name, con=engine, if_exists="append", index=False)

        logging.info(f"Successfully loaded {len(df)} rows into '{table_name}'.")

    except FileNotFoundError:
        logging.error(f"Error: CSV file not found at {csv_file_path}")
    except pd.errors.EmptyDataError:
        logging.error(f"Error: CSV file {csv_file_path} is empty.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")  # Log the specific exception


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Load data from a CSV file into the MySQL database."
    )
    parser.add_argument("csv_file", help="Path to the CSV file to load.")

    # Parse arguments
    args = parser.parse_args()

    # Call the main function
    load_data(args.csv_file)
