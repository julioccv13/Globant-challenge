import logging
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from utils.database import SessionLocal, insert_data
from utils.models import metadata

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/insert-data/")
def insert_data_endpoint(data: dict, db: Session = Depends(get_db)):
    try:
        # Determine the table name from the request data
        table_name = data.table_name
        if table_name is None:
            raise HTTPException(status_code=400, detail="Table name not provided in request data")

        # Insert data into the specified table
        insert_data(db, table_name, data)
        return {"message": f"Data inserted successfully into {table_name}"}
    except Exception as e:
        error_msg = f"Error inserting to table '{table_name}'"
        logging.error(error_msg, exc_info=True)
        raise HTTPException(status_code=500, detail=error_msg)
