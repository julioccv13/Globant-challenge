from utils.db_conn import *
from utils.db_recovery import *

# Database connection parameters
dbname = 'postgres'
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5434'

# Define the date and the backup directory path using the provided date format
date = '2024-03-23'
backup_dir = rf"database\data\backup\{date}"

# Connect to PostgreSQL
engine, metadata = connect_to_database(dbname, user, password, host, port)

# Restore data from avro files
date_str = date # input("Enter date in YYYY-MM-DD format: ")
restore_tables_from_avro(engine, backup_dir)
