# MySQL Query Lab

MySQL Query Lab is a project for data analysis and exploration. It uses notebooks to connect to MySQL, create databases, generate synthetic data, run queries, and create and test pandas DataFrames.

Key Features:

* ***Interactive querying:*** Create, execute, and visualize queries in notebooks.
* ***Powerful querying capabilities:*** Execute complex SQL queries with ease.
* ***Conversion to Pandas DataFrames:*** Convert query results into Pandas DataFrames for further analysis.
* ***Unit testing with pytest:*** Write unit tests using pytest to ensure the accuracy of SQL queries.
* ***Data generation with Faker:*** Generate synthetic data for test datasets or populating tables.
* ***CSV data loading:*** Load data into tables from external sources.
* ***User-friendly interface:*** Easy to navigate, create databases, and practice SQL skills.

MySQL Query Lab empowers users to explore and analyze MySQL data effectively, while also simplifying the process of query creation, testing, and data manipulation.


## Requirements

* Python 3.11 or higher
* pip

## Installation

1. Clone this repository to your local machine using `git clone https://github.com/benkaan001/mysql_query_lab.git`.
2. Navigate to the root directory of the project.
3. Create a virtual environment using `virtualenv venv`.
4. Activate the virtual environment using `source venv/bin/activate` (on Linux/Mac) or `venv\Scripts\activate` (on Windows).
5. Install the required packages using `pip install -r requirements.txt`.
6. Install the project locally in the virtual environment using `pip install -e .`.
7. Rename `.env.example` file to `.env` and fill your own database credentials.

📌 ***Remember to activate the virtual environment when you open a new terminal or command prompt window to work on your project. If you want to deactivate the virtual environment, simply run the command `deactivate` or run `source mysql_query_lab/env/bin/activate` to reactivate the virtual environment.***


## File Structure
```
mysql_query_lab/
├── venv/
├── setup.py
├── mysql_query_lab/
│   ├── assets/
│   │   ├── key_concepts/
│   │   │   ├── concept1.md
│   │   │   └── concept2.md
│   │   └── asset.png
│   ├── data/
│   │   ├── db1_dim_table/
│   │   │   └── dim_table.csv
│   │   └── db1_fact_table/
│   │       └── fact_table.csv
│   ├── databases/
│   │   ├── db1/
│   │   │   ├── create_tables.sql
│   │   │   └── seed_tables.sql
│   │   └── db2/
│   │       ├── create_tables.sql
│   │       └── seed_tables.sql
│   ├── notebooks/
│   │   ├── notebook1.ipynb
│   │   │   └── helper/
│   │   │       ├── create_database.ipynb
│   │   │       ├── create_tables.ipynb
│   │   │       └── seed_tables.ipynb
│   │   └── notebook2.ipynb
│   │       └── helper/
│   │           ├── create_database.ipynb
│   │           ├── create_tables.ipynb
│   │           └── seed_tables.ipynb
│   ├── utils/
│   │   ├── config.py
│   │   ├── create_database.py
│   │   └── create_mysql_connection.py
│   └── tests/
│       └── test_file1.py
│       └── test_file2.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch with a descriptive name (`git checkout -b my-new-feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push your changes to the new branch (`git push origin my-new-feature-branch`).
5. Create a pull request and describe your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

