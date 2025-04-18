# src/notebook_setup.py
# Helper script to set up the Jupyter notebook environment for the MySQL Query Lab.
# Run this script using '%run -i ../src/notebook_setup.py' in the first notebook cell.

import os
import sys

import sqlalchemy
from dotenv import load_dotenv
from IPython import get_ipython

# --- Import the custom magic class directly ---
# This requires src path to be set correctly first
try:
    from mysql_lab_magic import MySQLLabMagic

    magic_class_imported = True
except ImportError as e:
    print(
        "Error: Could not import MySQLLabMagic from mysql_lab_magic. "
        f"Ensure file exists and src is in sys.path. Details: {e}"
    )
    magic_class_imported = False
except Exception as e:
    print(f"An unexpected error occurred during import: {e}")
    magic_class_imported = False


print("Running notebook setup...")

# 1. Adjust sys.path to find the 'src' directory (handles ModuleNotFoundError)
try:
    # Assumes notebook is in 'notebooks/' subdir
    project_root = os.path.dirname(os.getcwd())
    src_path = os.path.join(project_root, "src")
    if src_path not in sys.path:
        sys.path.append(src_path)
        print(f"Added '{src_path}' to sys.path")
        # Re-attempt import if it failed initially and path was just added
        if not magic_class_imported:
            from mysql_lab_magic import MySQLLabMagic

            magic_class_imported = True

except Exception as e:
    print(
        "Warning: Could not automatically adjust sys.path. "
        f"Ensure 'src' is importable. Error: {e}"
    )

# 2. Load environment variables
try:
    # Assumes .env file is in the project root (parent of notebook dir)
    dotenv_path = os.path.join(project_root, ".env")
    load_dotenv(dotenv_path=dotenv_path)
    print("Loaded environment variables from .env file.")
except Exception as e:
    print(
        f"Warning: Could not load .env file from '{dotenv_path}'. "
        f"Ensure it exists. Error: {e}"
    )

# 3. Get database connection details
db_user = os.getenv("MYSQL_USER")
db_password = os.getenv("MYSQL_PASSWORD")
db_name = os.getenv("MYSQL_DATABASE")
db_host = os.getenv("DB_HOST", "127.0.0.1")
db_port = os.getenv("DB_PORT", "3307")  # Use the correct host port

db_engine = None  # Initialize db_engine to None

if not all([db_user, db_password, db_name]):
    print("Error: Database credentials or name missing in environment variables.")
    # raise ValueError("Missing DB credentials in .env") # Or handle more gracefully
else:
    # 4. Construct connection URL (using pymysql)
    db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    print(f"Database URL configured for: {db_host}:{db_port}/{db_name}")

    # 5. Create SQLAlchemy engine and make it available globally
    # The '%run -i' command executes this in the notebook's namespace.
    try:
        # Assign to a predictable variable name for the magic command
        db_engine = sqlalchemy.create_engine(db_url)

        # Test connection
        with db_engine.connect() as connection:
            print(
                "Successfully created SQLAlchemy engine ('db_engine') "
                "and connected to database."
            )

        # Make engine available in the global namespace where %run -i executes
        # This happens implicitly when run with -i, but we make it explicit for clarity
        ipython_shell = get_ipython()
        if ipython_shell:
            ipython_shell.user_ns["db_engine"] = db_engine

    except Exception as e:
        print(f"Error creating SQLAlchemy engine: {e}")
        # db_engine remains None

# 6. Register the custom magic class directly (bypassing load_ext)
if magic_class_imported:
    try:
        ipython_shell = get_ipython()
        if ipython_shell:
            print("Registering custom MySQLLabMagic class directly...")
            ipython_shell.register_magics(MySQLLabMagic)
            print("Custom '%%mysql_lab' magic registered successfully.")
        else:
            print("Warning: Could not get IPython shell instance to register magic.")
    except Exception as e:
        print(f"Error registering custom magic class: {e}")
else:
    print("Skipping magic registration because import failed.")


print("Notebook setup complete.")
