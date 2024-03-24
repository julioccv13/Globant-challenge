import logging
import uvicorn
from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException
from utils.connection import *
from utils.insertion import *


# Initialize FastAPI app
app = FastAPI()

# Connect to the database
engine = connect_to_database()

# Define endpoint to receive data
@app.post("/process_data/")
async def process_data(json_data: Dict[str, Any]) -> Dict[str, Any]:
    table_name = json_data.get("table_name")
    data = json_data.get("data")    
    # Check if table_name and data are present
    if not table_name or not data:
        return {"error": "Invalid JSON data. 'table_name' and 'data' fields are required."}
    insert_data_from_json(json_data, engine)    
    return {"result": "Data processed and inserted into database successfully"}

if __name__ == "__main__":    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)