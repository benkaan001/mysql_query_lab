import argparse
import logging
import os
import sys

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_table_data(
    engine, table_name: str, csv_file_path: str, if_exists_action: str = "append"
):
    """Loads data from a CSV into a specific table using the provided engine."""
    if not os.path.exists(csv_file_path):
        logging.error(f"Error: CSV file not found at {csv_file_path}")
        return False

    try:
        logging.info(f"Reading data from {csv_file_path}...")
        df = pd.read_csv(csv_file_path)
        logging.info(f"Read {len(df)} rows from CSV for table '{table_name}'.")
        msg = (
            f"Loading data into table '{table_name}' "
            f"(if_exists='{if_exists_action}')..."
        )
        logging.info(msg)
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists=if_exists_action,
            index=False,
        )
        logging.info(f"Successfully loaded {len(df)} rows into '{table_name}'.")
        return True

    except FileNotFoundError:
        logging.error(f"Error: CSV file not found at {csv_file_path}")
        return False
    except pd.errors.EmptyDataError:
        logging.error(f"Error: CSV file {csv_file_path} is empty.")
        return False
    except Exception as e:
        logging.error(f"An error occurred loading data for table '{table_name}': {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Load data from a CSV file into a specified MySQL table."
    )
    parser.add_argument(
        "--database", required=True, help="Name of the target database (schema)."
    )
    parser.add_argument(
        "--table", required=True, help="Name of the database table to load into."
    )
    parser.add_argument("--file", required=True, help="Path to the source CSV file.")
    parser.add_argument(
        "--if-exists",
        default="append",
        choices=["fail", "replace", "append"],
        help="How to behave if the table already exists (default: append).",
    )

    args = parser.parse_args()

    load_dotenv()
    db_user = os.getenv("MYSQL_USER")
    db_password = os.getenv("MYSQL_PASSWORD")
    db_host = os.getenv("DB_HOST", "127.0.0.1")
    db_port = os.getenv("DB_PORT", "3307")
    target_db_name = args.database

    if not all([db_user, db_password, target_db_name]):
        logging.error(
            "Database credentials or target database name missing."
            " Check .env file and --database argument."
        )
        sys.exit(1)

    db_url = (
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{target_db_name}"
    )
    msg = (
        f"Connecting using pymysql to: {db_host}:{db_port}/"
        f"{target_db_name} as user {db_user}"
    )
    logging.info(msg)

    try:
        engine = create_engine(db_url)
        logging.info(f"Successfully created database engine for {target_db_name}")
        success = load_table_data(engine, args.table, args.file, args.if_exists)
        if not success:
            sys.exit(1)
    except Exception as e:
        logging.error(f"Failed to create database engine or load data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
