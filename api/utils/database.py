import os
import logging
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from utils.models import *

# Configure logging
log_dir = os.path.join('api', 'logs')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'logs.log')
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
    
engine, metadata = connect_to_database()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Insert
    
def insert_data(session, table_name, data):
    try:
        table = metadata.tables[table_name]
        session.execute(table.insert().values(**data))
        session.commit()
    except Exception as e:
        logging.error("Error inserting data into database:", e)
        session.rollback()