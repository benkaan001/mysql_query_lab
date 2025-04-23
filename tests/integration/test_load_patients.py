# tests/integration/test_load_patients.py
# Integration tests for loading the 'patients' table (LeetCode version).

import os
import subprocess
import sys

import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

PROBLEM_DB = "leetcode_01_db"
TABLE_NAME = "patients"
CSV_FILE_PATH = "data/leetcode/01_patients_diabetes_patients.csv"


@pytest.fixture(scope="module")
def db_engine_problem():
    """Creates a SQLAlchemy engine for the specific problem database."""
    load_dotenv()
    db_user = os.getenv("MYSQL_USER")
    db_password = os.getenv("MYSQL_PASSWORD")
    db_name = PROBLEM_DB
    db_host = os.getenv("DB_HOST", "127.0.0.1")
    db_port = os.getenv("DB_PORT", "3307")

    if os.getenv("CI"):
        db_host_ci = os.getenv("DB_HOST")
        db_port_ci = os.getenv("DB_PORT")
        db_user_ci = os.getenv("MYSQL_USER")
        db_password_ci = os.getenv("MYSQL_PASSWORD")
        db_name_ci = os.getenv("MYSQL_DATABASE")
        if all([db_host_ci, db_port_ci, db_user_ci, db_password_ci, db_name_ci]):
            print(
                "CI environment detected. Connecting to "
                f"{db_host_ci}:{db_port_ci}/{db_name_ci}"
            )
            db_url = (
                f"mysql+pymysql://{db_user_ci}:{db_password_ci}@"
                f"{db_host_ci}:{db_port_ci}/{db_name_ci}"
            )
        else:
            pytest.fail(
                "CI environment detected, but DB connection ENV VARS are missing."
            )
    else:
        if not all([db_user, db_password, db_name]):
            pytest.fail("Local DB credentials missing in .env")
        db_url = (
            f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        )

    try:
        engine = create_engine(db_url)
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print(f"\nCreated engine for {db_name} at {db_host}:{db_port}")
        return engine
    except Exception as e:
        pytest.fail(f"Failed to create database engine for {db_name}: {e}")


@pytest.fixture(scope="function")
def clean_patients_table(db_engine_problem):
    """Cleans the patients table in the problem-specific DB before each test."""
    engine = db_engine_problem
    with engine.connect() as connection:
        trans = connection.begin()
        try:
            connection.execute(text(f"TRUNCATE TABLE {TABLE_NAME}"))
            trans.commit()
            print(
                f"\nTruncated table {TABLE_NAME} in {engine.url.database} before test."
            )
        except Exception as e:
            trans.rollback()
            if "Unknown table" in str(e) or "doesn't exist" in str(e):
                pytest.skip(
                    f"""Table {TABLE_NAME} does not exist yet in
                    {engine.url.database}: {e}"""
                )
            else:
                pytest.fail(
                    f"""Failed to truncate table {TABLE_NAME} in
                    {engine.url.database}: {e}"""
                )
    yield


def test_load_patients_script(db_engine_problem, clean_patients_table):
    """Tests running load_data.py script for the patients table."""
    assert os.path.exists(CSV_FILE_PATH), f"Data file not found: {CSV_FILE_PATH}"

    python_executable = sys.executable
    cmd = [
        python_executable,
        "src/load_data.py",
        "--database",
        PROBLEM_DB,
        "--table",
        TABLE_NAME,
        "--file",
        CSV_FILE_PATH,
        "--if-exists",
        "replace",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)

    print("\n--- load_data.py stdout ---")
    print(result.stdout)
    print("--- load_data.py stderr ---")
    print(result.stderr)
    print("--- End script output ---")

    assert (
        result.returncode == 0
    ), f"load_data.py script failed with exit code {result.returncode}"

    engine = db_engine_problem
    with engine.connect() as connection:
        count_result = connection.execute(text(f"SELECT COUNT(*) FROM {TABLE_NAME}"))
        count = count_result.scalar_one()
        assert count == 5, f"Expected 5 rows in {TABLE_NAME}, found {count}"

        data_result = connection.execute(
            text(f"SELECT conditions FROM {TABLE_NAME} WHERE patient_id = :id"),
            {"id": 3},
        )
        conditions = data_result.scalar_one()
        assert conditions == "DIAB100 MYOP"

        data_result_2 = connection.execute(
            text(f"SELECT patient_name FROM {TABLE_NAME} WHERE patient_id = :id"),
            {"id": 2},
        )
        name = data_result_2.scalar_one()
        assert name == "Alice"
