import os
import pandas as pd
import numpy as np
from sqlalchemy import Table, MetaData
from fastavro.schema import load_schema
from datetime import datetime
import fastavro
   
# Function to retrieve names of all tables in the database  
      
def read_tables(engine):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table_names = metadata.tables.keys()
    return table_names

# Function to map pandas data types to Avro types

def type_mapping(pandas_type):
    if np.issubdtype(pandas_type, np.integer):
        return ['null', 'int']
    elif np.issubdtype(pandas_type, np.floating):
        return ['null', 'double']
    elif np.issubdtype(pandas_type, np.bool_):
        return ['null', 'boolean']
    else:
        return ['null', 'string']
    
# Function to backup a table to Avro format

def table_to_avro(engine, table_name, avro_file_path):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = Table(table_name, metadata, autoload=True, autoload_with=engine)
    query = table.select()
    df = pd.read_sql(query, engine)
    # Convert DataFrame to list of dictionaries
    records = df.to_dict(orient='records')
    # Generate Avro schema dynamically based on DataFrame columns
    avro_fields = []
    for column, dtype in df.dtypes.items():
        avro_type = type_mapping(dtype)
        avro_field = {'name': column, 'type': avro_type}
        avro_fields.append(avro_field)
    avro_schema = {
        'type': 'record',
        'name': 'Record',
        'fields': avro_fields
    }
    # Write data to Avro file
    with open(avro_file_path, 'wb') as f:
        fastavro.writer(f, avro_schema, records)

# Function to backup all tables in the database to Avro format
        
def backup_tables(engine, backup_dir):
    # Create directory with current date inside backup directory
    current_date = datetime.now().strftime("%Y-%m-%d")  
    backup_date_dir = os.path.join(backup_dir, current_date)
    os.makedirs(backup_date_dir, exist_ok=True)    
    backup_dir = backup_date_dir    
    # Get all table names
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table_names = metadata.tables.keys()
    # Backup each table to Avro format to that date
    for table_name in table_names:
        avro_file_name = f"{table_name}.avro"
        avro_file_path = os.path.join(backup_dir, avro_file_name)
        table_to_avro(engine, table_name, avro_file_path)
        print(f"Table '{table_name}' backed up successfully to '{avro_file_path}'")