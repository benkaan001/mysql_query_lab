
import os
import pytest
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv


from src.load_data import load_data

# Define the path to the sample data relative to the project root
SAMPLE_CSV_PATH = "data/departments.csv"
TABLE_NAME = "departments"

@pytest.fixture(scope="module")
def db_engine():
    """
    Pytest fixture to create a SQLAlchemy engine.
    Loads database configuration from the .env file.
    Scope='module' means this fixture runs once per test module.
    """
    load_dotenv()
    db_user = os.getenv("MYSQL_USER")
    db_password = os.getenv("MYSQL_PASSWORD")
    db_name = os.getenv("MYSQL_DATABASE")
    db_host = os.getenv("DB_HOST", "127.0.0.1") # Use DB_HOST from env if set, else default
    db_port = os.getenv("DB_PORT", "3307")      # Use DB_PORT from env if set, else use the known working port

    if not all([db_user, db_password, db_name]):
        pytest.fail("Database credentials or name not found in environment variables.")

    db_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    try:
        engine = create_engine(db_url)
        # Test connection briefly
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return engine
    except Exception as e:
        pytest.fail(f"Failed to create database engine: {e}")

@pytest.fixture(scope="function")
def clean_table(db_engine):
    """
    Pytest fixture to clean the target table before each test function.
    Scope='function' means this runs before each test function using it.
    """
    with db_engine.connect() as connection:
        # Use TRUNCATE TABLE for efficiency, requires appropriate permissions
        # Alternatively, use DELETE FROM TABLE_NAME
        try:
            connection.execute(text(f"TRUNCATE TABLE {TABLE_NAME}"))
            # Commit is often needed after DDL or data-modifying statements outside transactions
            # For SQLAlchemy 1.4+ engine connections, commit might happen automatically
            # If using older SQLAlchemy or specific transaction modes, uncomment below:
            # connection.commit()
        except Exception as e:
            # Handle cases where table might not exist yet on first run etc.
            # Or fail if cleaning is essential
             pytest.skip(f"Could not truncate table {TABLE_NAME}, perhaps it doesn't exist yet? Error: {e}")
             pass # Allow test to proceed if truncate fails (e.g., table not created)

    yield # Test runs here

    # Optional: Add cleanup after test if needed
    # with db_engine.connect() as connection:
    #     connection.execute(text(f"TRUNCATE TABLE {TABLE_NAME}"))
    #     # connection.commit()


def test_load_departments_data(db_engine, clean_table):
    """
    Tests loading data from departments.csv into the departments table.
    Uses the db_engine and clean_table fixtures.
    """
    # Arrange: Ensure the sample CSV exists
    assert os.path.exists(SAMPLE_CSV_PATH), f"Sample data file not found at {SAMPLE_CSV_PATH}"

    # Act: Run the data loading function
    # We directly call the imported function instead of running the script as a subprocess
    try:
        load_data(SAMPLE_CSV_PATH)
    except Exception as e:
        pytest.fail(f"load_data function raised an unexpected exception: {e}")

    # Assert: Check if data was loaded correctly
    with db_engine.connect() as connection:
        # 1. Check row count
        result = connection.execute(text(f"SELECT COUNT(*) FROM {TABLE_NAME}"))
        count = result.scalar_one() # Gets the single value from the first row
        assert count == 9, f"Expected 9 rows in {TABLE_NAME}, but found {count}"

        # 2. Check for a specific known value
        result = connection.execute(
            text(f"SELECT dept_name FROM {TABLE_NAME} WHERE dept_no = :dept_no"),
            {"dept_no": "d005"} # Parameter binding
        )
        dept_name = result.scalar_one_or_none() # Use scalar_one_or_none for safety
        assert dept_name is not None, "Department d005 not found."
        assert dept_name == "Development", f"Expected dept_name 'Development' for d005, but found '{dept_name}'"

        # 3. Check another specific value
        result = connection.execute(
            text(f"SELECT dept_no FROM {TABLE_NAME} WHERE dept_name = :dept_name"),
            {"dept_name": "Finance"}
        )
        dept_no = result.scalar_one_or_none()
        assert dept_no is not None, "Department Finance not found."
        assert dept_no == "d002", f"Expected dept_no 'd002' for Finance, but found '{dept_no}'"

