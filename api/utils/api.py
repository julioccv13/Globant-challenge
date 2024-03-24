from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from utils.database import *
from utils.models import *

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/insert-data/")
def insert_data_endpoint(data: dict, table_name: str, db: Session = Depends(get_db)):
    try:
        insert_data(db, table_name, data)
        return {"message": "Data inserted successfully"}
    except Exception as e:
        logging.error("Error inserting to database:", e)
        raise HTTPException(status_code=500, detail=str(e))
