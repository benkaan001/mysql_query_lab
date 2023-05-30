from setuptools import setup, find_packages

setup(
    name='mysql_query_lab',
    version='0.1',
    description='A project for querying MySQL databases',
    long_description="MySQL Query Lab is a data analysis project that connects to a MySQL database and enables users to run queries using notebooks. It offers a user-friendly interface for interactive query creation, execution, and visualization, making it fun to practice/write queries.",
    author='Ben Kaan',
    url='https://github.com/benkaan/mysql_query_lab',
    packages=find_packages(),
    install_requires=[
        'mysql-connector-python',
        'ipython',
        'ipython-sql',
        'nbimporter',
        'sqlalchemy',
        'ipykernel',
        'nbformat',
        'prettytable',
        'sqlparse',
        'jupyter_client',
        'jupyter_core',
        'matplotlib-inline',
        'mysqlclient',
        'ipython-genutils',
        'Faker',
        'pandas',
        'ipywidgets',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'mysql_query_lab = mysql_query_lab.__main__:main'
        ]
    },
    license='MIT',

)

print("Don't forget to run 'pip install -e .' to add the parent directory to your virtual environment!")