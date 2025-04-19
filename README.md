# Modernized MySQL Query Lab

[![CI Pipeline](https://github.com/benkaan001/mysql_query_lab/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/benkaan001/mysql_query_lab/actions/workflows/ci.yml)


## Objective

This repository provides a containerized and tested environment for practicing and exploring SQL queries against various datasets using MySQL. It serves as a demonstration of modern data engineering and software development practices, including Docker, automated testing, custom tooling (IPython magic), and CI/CD.

This project is a modernized version of an earlier query lab. The original code is preserved in the `legacy/v1.0` branch.

## Features

* **Containerized Environment:** Uses Docker Compose for a reproducible MySQL 8.0 database setup.
* **Automated Data Loading:** Python script (`src/load_data.py`) using Pandas and SQLAlchemy (with PyMySQL driver) to load data from CSV files.
* **Interactive SQL Notebooks:** Jupyter Lab environment configured for running SQL queries.
* **Custom IPython Magic:** Includes a custom `%%mysql_lab` cell magic for a seamless "write only SQL" experience in notebooks, bypassing issues with standard libraries. Handles variable assignment (`df << %%mysql_lab`) and basic non-SELECT statements.
* **Automated Testing:** Integration tests (`pytest`) verify the data loading process against the live database container.
* **CI/CD Pipeline:** GitHub Actions workflow automatically runs linters (`ruff`, `black`) and tests (`pytest`) on pushes and pull requests to the `main` branch.
* **Code Quality:** Uses `black` for formatting and `ruff` for linting to ensure code consistency and catch potential issues.


## Tech Stack

* **Database:** MySQL 8.0
* **Containerization:** Docker, Docker Compose
* **Backend/Scripting:** Python 3.11+
* **Core Python Libraries:** Pandas, SQLAlchemy, PyMySQL, cryptography, python-dotenv
* **Testing:** Pytest
* **Notebook Environment:** Jupyter Lab
* **CI/CD:** GitHub Actions
* **Code Quality:** Ruff, Black

## Project Structure

```
.
├── .github/                # GitHub Actions workflows
│   └── workflows/
│       └── ci.yml
├── data/                   # Sample data files (e.g., .csv)
│   └── departments.csv
├── docs/                   # Supplementary documentation (optional)
│   └── notes/              # Personal notes (ignored)
├── notebooks/              # Jupyter notebooks for querying
│   └── 01_connect_and_query.ipynb
├── src/                    # Source code
│   ├── __init__.py
│   ├── load_data.py        # Data loading script
│   ├── mysql_lab_magic.py  # Custom IPython magic definition
│   └── notebook_setup.py   # Helper script for notebook environment setup
├── sql/                    # SQL files
│   ├── initdb/             # DB initialization scripts (schema)
│   │   └── 01_schema.sql
│   └── queries/            # Example SQL query files
│       └── 01_department_examples.sql
├── tests/                  # Automated tests
│   ├── __init__.py
│   └── integration/
│       ├── __init__.py
│       └── test_data_loading.py
├── .env_example            # Example environment variables template
├── .gitignore              # Files/directories ignored by Git
├── docker-compose.yml      # Docker Compose configuration
├── LICENSE                 # Project license file (e.g., MIT)
├── pyproject.toml          # Python project configuration (for linters/formatters)
├── README.md               # This file
└── requirements.txt        # Python dependencies
```

## Setup Instructions

1.  **Prerequisites:**
    * Git
    * Docker & Docker Compose
    * Python 3.11+ and pip
2.  **Clone Repository:**
    ```bash
    git clone [https://github.com/benkaan001/mysql_query_lab.git](https://github.com/benkaan001/mysql_query_lab.git)
    cd mysql_query_lab
    ```
3.  **Create Virtual Environment:**
    ```bash
    python -m venv .venv
    # Activate it:
    # macOS/Linux: source .venv/bin/activate
    # Windows: .venv\Scripts\activate
    ```
4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Configure Environment Variables:**
    * Copy the example `.env` file:
        ```bash
        cp .env_example .env
        ```
    * Edit the `.env` file and set **secure** values for:
        * `MYSQL_ROOT_PASSWORD`
        * `MYSQL_DATABASE` (e.g., `query_lab_db`)
        * `MYSQL_USER` (e.g., `query_lab_user`)
        * `MYSQL_PASSWORD`
    * **(For CI/CD):** Set up corresponding secrets in your GitHub repository settings.
    ##### **How to create GitHub Secrets**

    1. **Go to your repository on GitHub.**

    2. Click on **Settings** (top menu).

    3. In the left sidebar, click **Secrets and variables** > **Actions**.

    4. Click the **New repository secret** button.

    5. Enter a **name** (e.g., `MYSQL_ROOT_PASSWORD`) and the **value** (e.g., your password).

    6. Click **Add secret**.

    Repeat for each secret you need (e.g., `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_PASSWORD`).



6.  **Start Database Container:**
    ```bash
    docker-compose up -d
    ```
    Wait for the container to start and initialize (can check logs with `docker-compose logs -f db`).

## Usage

1.  **Load Data:**
    * Run the data loading script (make sure the virtual environment is active):
        ```bash
        python src/load_data.py data/departments.csv
        ```
2.  **Run Tests:**
    * Ensure the Docker container is running.
    * Run pytest from the project root:
        ```bash
        pytest
        ```
3.  **Run Linters/Formatters Locally:**
    * Check for linting issues:
        ```bash
        ruff check .
        ```
    * Automatically fix fixable issues (like import sorting):
        ```bash
        ruff check . --fix
        ```
    * Check formatting (without changing files):
        ```bash
        black --check .
        ```
    * Apply formatting:
        ```bash
        black .
        ```
4.  **Use Jupyter Notebooks:**
    * Ensure the Docker container is running.
    * Launch Jupyter Lab from the **project root directory**:
        ```bash
        jupyter lab
        ```
    * Open the notebook (e.g., `notebooks/01_connect_and_query.ipynb`).
    * Run the **first cell** (`%run -i ../src/notebook_setup.py`) to set up the connection and load the custom magic.
    * Execute subsequent cells containing `%%mysql_lab` followed by your SQL query. Results will be displayed as Pandas DataFrames. You can assign results using `my_df << %%mysql_lab`.
5.  **Connect with External SQL Client:**
    * You can connect any standard SQL client (DBeaver, TablePlus, MySQL Workbench, etc.) to the database using:
        * **Host:** `127.0.0.1`
        * **Port:** `3307` (or the host port mapped in `docker-compose.yml`)
        * **User:** Your `MYSQL_USER` from `.env`
        * **Password:** Your `MYSQL_PASSWORD` from `.env`
        * **Database:** Your `MYSQL_DATABASE` from `.env`


## Database Schema

The database schema is defined by scripts in the [sql/initdb/](sql/initdb/) directory. See [sql/initdb/01_schema.sql](sql/initdb/01_schema.sql) for current table definitions.

## Modernization Journey

This project was modernized from an earlier version (available on the `legacy/v1.0` branch) to incorporate current best practices like containerization, automated testing, CI/CD, dependency management, and custom tooling where needed.

## Future Enhancements (Next Steps)

* Integrate more complex datasets.
* Add corresponding data loading logic and tests for new datasets.
* Develop additional notebooks focused on specific SQL topics or data analysis tasks.


## License

MIT License.