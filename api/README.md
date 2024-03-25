# API Service

This directory contains files and documentation related to the REST API for interacting with a PostgreSQL database using FastAPI 

## Features

1. **FastAPI Application**: Provides REST API endpoints for interacting with the database.
2. **Database Connection**: Establishes a connection to a PostgreSQL database using SQLAlchemy.

## API Endpoints

### `/process-data/`: 
- GET endpoint to execute specific requirement query
- Be sure to include the name of the table you want to insert in and the data
- Example = {
     "table_name": "jobs",
     "data": [
         {"id": 200, "job": 'Test'},
         {"id": 300, "job": 'test'},
     ]
 }

### `/hires_per_quarter/`: 
- GET endpoint to execute specific requirement query
- Finds number of employees hired for each job and department in 2021 divided by quarter
- Response: CSV file containing the fetched data, stored in the api/data folder.

### `/above_avg_department_hires/`: 
- POST endpoint for inserting data into the database. Accepts JSON payloads with the data to be inserted.
- List of ids, name and number of employees hired of each department that hired more employees than the mean of employees hired in 2021 for all the departments
- Response: CSV file containing the fetched data, stored in the api/data folder.
