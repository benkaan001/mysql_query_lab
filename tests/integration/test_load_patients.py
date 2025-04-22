# tests/integration/test_load_patients.py
# Integration tests for loading the 'patients' table (LeetCode version).

import os
import subprocess # To run the script as a subprocess
import sys # To get python executable

import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Constants
PROBLEM_DB = "leetcode_01_db" # Database specific to this problem
TABLE_NAME = "patients"
# --- Updated Path ---
CSV_FILE_PATH = "data/leetcode/01_patients_diabetes_patients.csv" # Relative to project root


@pytest.fixture(scope="module")
def db_engine_problem():
    """ Creates a SQLAlchemy engine for the specific problem database. """
    load_dotenv()
    db_user = os.getenv("MYSQL_USER")
    db_password = os.getenv("MYSQL_PASSWORD")
    # Connect to the specific problem DB
    db_name = PROBLEM_DB
    db_host = os.getenv("DB_HOST", "127.0.0.1") # Host for connection (runner localhost)
    db_port = os.getenv("DB_PORT", "3307")      # Port for connection (runner host port)

    # --- CI Overrides ---
    # In GitHub Actions CI, connect to the service container directly
    if os.getenv("CI"): # Check if running in GitHub Actions CI environment
        db_host_ci = os.getenv("DB_HOST") # Should be 'mysql-db' or '127.0.0.1' depending on workflow
        db_port_ci = os.getenv("DB_PORT") # Should be '3306' or '3307' depending on workflow
        db_user_ci = os.getenv("MYSQL_USER") # Test user from workflow env
        db_password_ci = os.getenv("MYSQL_PASSWORD") # Test password from workflow env
        db_name_ci = os.getenv("MYSQL_DATABASE") # Test db name from workflow env

        if all([db_host_ci, db_port_ci, db_user_ci, db_password_ci, db_name_ci]):
             print(f"CI environment detected. Connecting to {db_host_ci}:{db_port_ci}/{db_name_ci}")
             # Note: Schema script creates PROBLEM_DB, but CI might use test_query_lab_db initially.
             # For simplicity here, we assume the test DB name passed via env matches PROBLEM_DB
             # or that the test setup ensures PROBLEM_DB exists.
             # A more robust setup might connect to the default CI DB first and create PROBLEM_DB.
             db_url = f"mysql+pymysql://{db_user_ci}:{db_password_ci}@{db_host_ci}:{db_port_ci}/{db_name_ci}"
        else:
             pytest.fail("CI environment detected, but DB connection ENV VARS are missing.")
    else:
        # --- Local Connection ---
        if not all([db_user, db_password, db_name]):
            pytest.fail("Local DB credentials missing in .env")
        db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


    try:
        engine = create_engine(db_url)
        # Test connection briefly
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print(f"\nCreated engine for {db_name} at {db_host}:{db_port}")
        return engine
    except Exception as e:
        pytest.fail(f"Failed to create database engine for {db_name}: {e}")


@pytest.fixture(scope="function")
def clean_patients_table(db_engine_problem):
    """Cleans the patients table in the problem-specific DB before each test."""
    # Ensure connection is to the correct database engine for this test
    engine = db_engine_problem
    with engine.connect() as connection:
        trans = connection.begin()
        try:
            connection.execute(text(f"TRUNCATE TABLE {TABLE_NAME}"))
            trans.commit()
            print(f"\nTruncated table {TABLE_NAME} in {engine.url.database} before test.")
        except Exception as e:
            trans.rollback()
            if "Unknown table" in str(e) or "doesn't exist" in str(e):
                 pytest.skip(f"Table {TABLE_NAME} does not exist yet in {engine.url.database}: {e}")
            else:
                 pytest.fail(f"Failed to truncate table {TABLE_NAME} in {engine.url.database}: {e}")
    yield


def test_load_patients_script(db_engine_problem, clean_patients_table):
    """Tests running load_data.py script for the patients table."""
    # Arrange: Ensure the CSV file exists
    assert os.path.exists(CSV_FILE_PATH), f"Data file not found: {CSV_FILE_PATH}"

    # Act: Run the load_data.py script targeting the specific database
    python_executable = sys.executable
    cmd = [
        python_executable,
        "src/load_data.py",
        "--database", PROBLEM_DB, # Target the specific DB
        "--table", TABLE_NAME,
        "--file", CSV_FILE_PATH,
        "--if-exists", "replace" # Use replace for testing
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)

    # Print script output for debugging if needed
    print("\n--- load_data.py stdout ---")
    print(result.stdout)
    print("--- load_data.py stderr ---")
    print(result.stderr)
    print("--- End script output ---")

    # Assert script ran successfully
    assert result.returncode == 0, f"load_data.py script failed with exit code {result.returncode}"

    # Assert data loaded correctly into the specific database
    engine = db_engine_problem # Use the correct engine
    with engine.connect() as connection:
        # Check row count
        count_result = connection.execute(text(f"SELECT COUNT(*) FROM {TABLE_NAME}"))
        count = count_result.scalar_one()
        assert count == 5, f"Expected 5 rows in {TABLE_NAME}, found {count}"

        # Check specific data
        data_result = connection.execute(
            text(f"SELECT conditions FROM {TABLE_NAME} WHERE patient_id = :id"),
            {"id": 3}
        )
        conditions = data_result.scalar_one()
        assert conditions == "DIAB100 MYOP"

        data_result_2 = connection.execute(
            text(f"SELECT patient_name FROM {TABLE_NAME} WHERE patient_id = :id"),
            {"id": 2}
        )
        name = data_result_2.scalar_one()
        assert name == "Alice"
