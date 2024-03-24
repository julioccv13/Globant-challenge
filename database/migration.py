import os
from utils.db_conn import *
from utils.db_migration import *
from sqlalchemy import Column, String, Integer

# Directory containing CSV and Excel files
data_directory = 'database\data'

# Define schemas for different tables based on file names
table_schemas = {
    "hired_employees": {"id": Integer, "name": String, "datetime": String, "department_id": Integer, "job_id": Integer},
    "departments": {"id": Integer, "department": String},
    "jobs": {"id": Integer, "job": String}
}

# Connect to database
engine, metadata = connect_to_database()

# Read data from files in the folder and insert into database
for file_name in os.listdir(data_directory):
    file_path = os.path.join(data_directory, file_name)
    if os.path.isfile(file_path):
        # Determine schema based on file name
        table_name = os.path.splitext(file_name)[0].lower()
        schema = table_schemas.get(table_name, {})  # Get schema for the table
        # Check if table exists
        metadata = MetaData()
        metadata.reflect(bind=engine)
        if table_name not in metadata.tables:
            # Create table if not exists
            metadata = MetaData()
            table = Table(table_name, metadata,
                          *(Column(col_name, col_type) for col_name, col_type in schema.items()))
            metadata.create_all(engine)        
        # Read and insert data
        insert_data(file_path, engine, schema)
print("Data insertion completed.")
