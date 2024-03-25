import os
import pandas as pd
from sqlalchemy import MetaData, Table, Column, inspect
import logging

# Function to create table with specified schema
def create_table(engine, table_name, schema):
    metadata = MetaData()
    table = Table(table_name, metadata,
                  *(Column(col_name, col_type) for col_name, col_type in schema.items()))
    metadata.create_all(engine)

# Function to read CSV or XLS file and insert data into database
def insert_data(file_path, engine, schema):
    file_name, file_ext = os.path.splitext(os.path.basename(file_path))
    table_name = file_name.lower()  
    if file_ext.lower() == '.csv':
        df = pd.read_csv(file_path, names=list(schema.keys()))
    elif file_ext.lower() in ('.xls', '.xlsx'):
        df = pd.read_excel(file_path, names=list(schema.keys()))
    else:
        logging.error(f"Unsupported file format: {file_ext}")
        return
    # Create table if not exists
    inspector = inspect(engine)
    if table_name not in inspector.get_table_names():
        create_table(engine, table_name, schema) 
    # Filter out and log null values
    null_rows = df[df.isnull().any(axis=1)]
    df_without_null = df.dropna()
    if not null_rows.empty:
        logging.info(f"Skipped {len(null_rows)} rows with null values in '{file_name}'.")    
    # Insert non-null data into the database
    df_without_null.to_sql(table_name, engine, if_exists='append', index=False)
