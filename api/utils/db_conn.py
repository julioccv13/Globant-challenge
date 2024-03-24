import os
import logging
from sqlalchemy import create_engine, MetaData

# Configure logging
logs_dir = os.path.join('api', 'logs')
os.makedirs(logs_dir, exist_ok=True)
log_file = os.path.join(logs_dir, 'logs')
logging.basicConfig(filename=log_file, level=logging.INFO)

# Database connection parameters
dbname = 'postgres'
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5434'

# Function to connect to postgres
def connect_to_database():
    try:
        db_uri = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
        engine = create_engine(db_uri)
        metadata = MetaData()
        return engine, metadata
    except Exception as e:
        logging.error("Error connecting to database:", e)
        return None, None


