from utils.db_conn import *
from utils.db_recovery import *

# Define the date and the backup directory path using the provided date format
date = str(input("Select date to recover in format YYYY-MM-DD: "))
backup_dir = rf"database\data\backup\{date}"

# Connect to PostgreSQL
engine, metadata = connect_to_database()

# Restore data from avro files
restore_tables_from_avro(engine, backup_dir)
