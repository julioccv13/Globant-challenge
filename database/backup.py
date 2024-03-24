from utils.db_backup import *
from utils.db_conn import *

# Database connection parameters
dbname = 'postgres'
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5434'

# Directory for back up files
backup_directory = r'database\data\backup'

# Connect to PostgreSQL
engine, metadata = connect_to_database(dbname, user, password, host, port)

# Backup all tables
backup_tables(engine, backup_directory)
