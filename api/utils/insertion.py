import logging
import pandas as pd
from utils.connection import *

# Connection to database
engine = connect_to_database()

# Function to read JSON file and insert data into database
def insert_data_from_json(json_data, engine):
    try:
        table_name = json_data.get('table_name')
        if not table_name:
            logging.error("Table name not found in JSON data.")
            return
        data = json_data.get('data')
        if not data:
            logging.error("No data found in JSON.")
            return
        df = pd.DataFrame(data)        
        # Insert data into the database
        df.to_sql(table_name, engine, if_exists='append', index=False)
        logging.info(f"Data inserted into table '{table_name}' from JSON.")        
    except Exception as e:
        logging.error("Error inserting data from JSON:", e)
        
