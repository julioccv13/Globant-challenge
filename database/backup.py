from utils.db_backup import *
from utils.db_conn import *

# Directory for back up files
backup_directory = r'database\data\backup'

# Connect to PostgreSQL
engine, metadata = connect_to_database()

# Backup all tables
backup_tables(engine, backup_directory)
