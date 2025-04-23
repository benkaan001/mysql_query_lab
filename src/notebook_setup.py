import os
import sys

import sqlalchemy
from dotenv import load_dotenv
from IPython import get_ipython

magic_class_imported = False
try:
    project_root_setup = os.path.dirname(os.path.abspath(__file__))
    project_root_setup = os.path.dirname(project_root_setup)
    if project_root_setup not in sys.path:
        sys.path.insert(0, project_root_setup)
    from src.mysql_lab_magic import MySQLLabMagic
    magic_class_imported = True
except ImportError as e:
    print(
        "Error: Could not import MySQLLabMagic from src.mysql_lab_magic. "
        f"Ensure file exists and src is importable. Details: {e}"
    )
except Exception as e:
    print(f"An unexpected error occurred during import: {e}")

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
    try:
        current_project_root = project_root_setup
    except NameError:
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

    db_url = (
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{target_db_name}"
    )

    try:
        engine = sqlalchemy.create_engine(db_url)
        with engine.connect():
            print(f"Successfully created and connected engine for '{target_db_name}'.")
        _engine_cache[target_db_name] = engine
        return engine
    except Exception as e:
        print(f"Error creating SQLAlchemy engine for '{target_db_name}': {e}")
        return None

def register_magic_command():
    if magic_class_imported:
        try:
            ipython_shell = get_ipython()
            if ipython_shell:
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

print("Running notebook setup script...")
try:
    notebook_dir = os.getcwd()
    project_root = os.path.dirname(notebook_dir)
    project_root = os.path.dirname(project_root)
    project_root = os.path.dirname(project_root)
    src_path = os.path.join(project_root, "src")
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
        print(f"Added '{src_path}' to sys.path")
except NameError:
    print("Warning: Could not determine project root from current working directory.")
except Exception as e:
    print(f"Warning: Error adjusting sys.path: {e}")

register_magic_command()
print("Notebook setup script complete. Use 'get_db_engine(db_name)' to create engines.")
