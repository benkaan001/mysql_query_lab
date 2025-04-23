# src/notebook_setup.py
# Helper script to set up the Jupyter notebook environment for the MySQL Query Lab.
# Defines a function to get DB engines and registers custom magic.
# Run '%run -i ...' then 'db_engine = get_db_engine("db_name")' in notebook cells.

import os
import sys

import sqlalchemy
from dotenv import load_dotenv
from IPython import get_ipython

# --- Import the custom magic class directly ---
# This requires src path to be set correctly first
magic_class_imported = False  # Flag to track import status
try:
    # Determine project root relative to this script file
    project_root_setup = os.path.dirname(os.path.abspath(__file__))  # Path to src
    project_root_setup = os.path.dirname(project_root_setup)  # Path to project root
    if project_root_setup not in sys.path:
        sys.path.insert(0, project_root_setup)  # Add project root to path

    from src.mysql_lab_magic import MySQLLabMagic

    magic_class_imported = True
except ImportError as e:
    print(
        "Error: Could not import MySQLLabMagic from src.mysql_lab_magic. "
        f"Ensure file exists and src is importable. Details: {e}"
    )
except Exception as e:
    print(f"An unexpected error occurred during import: {e}")


# --- Global Cache for Engines ---
# Avoid recreating engines repeatedly if the same DB is requested
_engine_cache = {}


def get_db_engine(target_db_name: str):
    """
    Creates and returns a SQLAlchemy engine for the specified target database.
    Reads base credentials from .env file. Caches engines.
    """
    global _engine_cache
    if target_db_name in _engine_cache:
        print(f"Using cached engine for database '{target_db_name}'.")
        return _engine_cache[target_db_name]

    print(f"Creating new engine for database '{target_db_name}'...")
    # Load environment variables for base connection
    # Assumes .env is in the project root (parent of src)
    # Determine project root relative to this script file if not already done
    try:
        current_project_root = project_root_setup
    except NameError:  # Fallback if run outside expected structure
        current_project_root = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

    load_dotenv(dotenv_path=os.path.join(current_project_root, ".env"))
    db_user = os.getenv("MYSQL_USER")
    db_password = os.getenv("MYSQL_PASSWORD")
    db_host = os.getenv("DB_HOST", "127.0.0.1")
    db_port = os.getenv("DB_PORT", "3307")

    if not all([db_user, db_password, target_db_name]):
        print(
            "Error: Database credentials or target database name missing."
            " Check .env file and function argument."
        )
        return None

    # Construct connection URL targeting the specific database
    db_url = (
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{target_db_name}"
    )

    try:
        # Create engine for the specific target database
        engine = sqlalchemy.create_engine(db_url)
        # Test connection
        with engine.connect():
            print(f"Successfully created and connected engine for '{target_db_name}'.")
        _engine_cache[target_db_name] = engine  # Cache the engine
        return engine
    except Exception as e:
        print(f"Error creating SQLAlchemy engine for '{target_db_name}': {e}")
        return None


# --- Register Magic Command ---
def register_magic_command():
    """Registers the custom magic command with IPython."""
    if magic_class_imported:
        try:
            ipython_shell = get_ipython()
            if ipython_shell:
                # Check if magic is already registered before attempting to register
                if not ipython_shell.find_magic("mysql_lab"):
                    print("Registering custom MySQLLabMagic class...")
                    ipython_shell.register_magics(MySQLLabMagic)
                    print("Custom '%%mysql_lab' magic registered successfully.")
                else:
                    print("Custom '%%mysql_lab' magic already registered.")
            else:
                print(
                    "Warning: Could not get IPython shell instance to register magic."
                )
        except Exception as e:
            print(f"Error registering custom magic class: {e}")
    else:
        print("Skipping magic registration because import failed.")


# --- Run setup steps when script is executed by %run -i ---
print("Running notebook setup script (v2: with get_db_engine)...")
# Adjust path (redundant if import worked, but safe)
try:
    # Try to determine project root based on typical notebook location
    notebook_dir = os.getcwd()  # Where the notebook is running
    project_root = os.path.dirname(notebook_dir)  # Up one level (e.g., leetcode/)
    project_root = os.path.dirname(project_root)  # Up another level (e.g., notebooks/)
    project_root = os.path.dirname(project_root)  # Up another level (project root)

    src_path = os.path.join(project_root, "src")
    if src_path not in sys.path:
        sys.path.insert(0, src_path)  # Use insert(0,...) for higher priority
        print(f"Added '{src_path}' to sys.path")
except NameError:  # Handle case where getcwd() might fail
    print("Warning: Could not determine project root from current working directory.")
except Exception as e:
    print(f"Warning: Error adjusting sys.path: {e}")

# Register the magic
register_magic_command()

print("Notebook setup script complete. Use 'get_db_engine(db_name)' to create engines.")
