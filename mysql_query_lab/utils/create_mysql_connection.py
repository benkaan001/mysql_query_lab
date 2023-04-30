import mysql.connector
from mysql.connector import errorcode
from IPython.core.magic import register_line_magic
from IPython import get_ipython
from sqlalchemy import create_engine, exc
from mysql_query_lab.utils.config import MYSQL_CONFIG

db_name = None

@register_line_magic
def connect_to_mysql(db_name):
    """Establishes a connection to the specified MySQL database."""
    try:
        MYSQL_CONFIG['database'] = db_name
        with mysql.connector.connect(**MYSQL_CONFIG) as conn:
            print(f"Successfully connected to {db_name} database.")
            return conn
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password.")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(e)


def get_connection_string(db_name):
    """Returns a connection string for the specified database."""
    conn_string = f"mysql+mysqlconnector://{MYSQL_CONFIG['user']}:{MYSQL_CONFIG['password']}@{MYSQL_CONFIG['host']}/{db_name}"
    return conn_string


# Set the SQLalchemy engine
try:
    engine = create_engine(get_connection_string(db_name))
except exc.SQLAlchemyError as e:
    print(f"Error creating engine: {e}")

# Set up the %sql magic command
def load_ipython_extension(ipython):
    ipython.register_magic_function(connect_to_mysql, magic_kind='line')

# Automatically load the extension when the module is imported
load_ipython_extension(get_ipython())
