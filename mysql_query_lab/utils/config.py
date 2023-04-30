import os

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

MYSQL_CONFIG = {
    'user': DB_USER,
    'password': DB_PASSWORD,
    'host': DB_HOST,
}