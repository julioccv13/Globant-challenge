import os
import logging
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from utils.models import *
from utils.db_conn import *

# Configure logging
logs_dir = os.path.join('api', 'logs')
os.makedirs(logs_dir, exist_ok=True)
log_file = os.path.join(logs_dir, 'logs')
logging.basicConfig(filename=log_file, level=logging.INFO)

# Configure database connection
engine = connect_to_database()
Session = sessionmaker(bind=engine)

# Function to insert data into the appropriate table
def insert_data(data):
    table_name = identify_table(data)
    if not table_name:
        return False, 'Unable to identify table for insertion'
    
    session = Session()
    try:
        # Insert data into the identified table
        table_class = globals()[table_name.capitalize()]
        entry = table_class(**data)
        session.add(entry)
        session.commit()
        return True, f'Data inserted into {table_name} successfully'
    except IntegrityError as e:
        session.rollback()
        logging.error(f'Error inserting data into {table_name}: {e}')
        return False, f'Error inserting data into {table_name}'
    finally:
        session.close()

# Function to identify the appropriate table based on the structure of the data
def identify_table(data):
    table_mapping = {
        'name': 'hired_employees',
        'department': 'departments',
        'job': 'jobs'
        # Add more mappings as needed based on the criteria to identify the table
    }
    for key, value in table_mapping.items():
        if key in data:
            return value
    return None