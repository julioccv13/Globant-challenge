from sqlalchemy import create_engine, MetaData

# Function to connect to postgres
def connect_to_database(dbname, user, password, host, port):
    try:
        db_uri = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
        engine = create_engine(db_uri)
        metadata = MetaData()
        return engine, metadata
    except Exception as e:
        print("Error connecting to database:", e)
        return None, None



