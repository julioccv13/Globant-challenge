# API Service

This directory contains files and documentation related to the REST API for interacting with a PostgreSQL database using FastAPI 

## Features

1. **FastAPI Application**: Provides REST API endpoints for interacting with the database.
2. **Database Connection**: Establishes a connection to a PostgreSQL database using SQLAlchemy.

## API Endpoints

### `/process-data/`: 
- POST endpoint for inserting data into the database. Accepts JSON payloads with the data to be inserted.
- Be sure to include the name of the table you want to insert in and the data
- Example = {
     "table_name": "jobs",
     "data": [
         {"id": 200, "job": 'Test'},
         {"id": 300, "job": 'test'},
     ]
 }

## Models

### HiredEmployee
#### Fields:
- id (Integer, Primary Key)
- name (String)
- datetime (String)
- department_id (Integer)
- job_id (Integer)

### Departments
#### Fields:
- id (Integer, Primary Key)
- department (String)

### Jobs
#### Fields:
- id (Integer, Primary Key)
- job (String)

## Logging
Exceptions during database connection and data insertion are logged to a file named logs inside the api/logs folder.