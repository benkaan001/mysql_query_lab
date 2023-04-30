# MySQL Query Lab

"MySQL Query Lab" is a data analysis and exploration project that uses notebooks to connect to a MySQL to create databases and run various queries at intermediate and advanced levels. With this project, users can explore and analyze their MySQL data with ease, thanks to the powerful querying capabilities of notebooks.

The project offers a user-friendly interface that allows users to interactively create, execute, and visualize queries, making it fun to create their own databases and practice their sql skills.



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

📌 ***Remember to activate the virtual environment every time you open a new terminal or command prompt window to work on your project. If you want to deactivate the virtual environment, simply run the command `deactivate` or run `source mysql_query_lab/env/bin/activate` to reactivate the virtual environment.***


## File Structure

```
mysql_query_lab/
├── venv/
├── setup.py
├── mysql_query_lab/
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
│   └── utils/
│       ├── config.py
│       ├── create_database.py
│       └── create_mysql_connection.py
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

