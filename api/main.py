import uvicorn
from typing import Dict, Any
from fastapi import FastAPI
from utils.connection import *
from utils.insertion import *
from utils.queries import *


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

# Define endpoint to show the number of employees hired for each job and department in 2021 divided by quarter
@app.get("/hires_per_quarter/")
async def get_data():
    data_fetcher = HiresPerQuarter()  
    data = data_fetcher.hires_per_quarter()  
    return {"data": data}

# Define endpoint to show the list of ids, name and number of employees hired of each department that hired more employees than the mean of employees hired in 2021
@app.get("/above_avg_department_hires/")
async def get_data():
    data_fetcher = AboveAvgHires()  
    data = data_fetcher.above_avg_department_hires()  
    return {"data": data}

if __name__ == "__main__":    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)