# API Service

This directory contains files and documentation related to the REST API for interacting with a PostgreSQL database using FastAPI 

## Features

1. **FastAPI Application**: Provides REST API endpoints for interacting with the database.
2. **Database Connection**: Establishes a connection to a PostgreSQL database using SQLAlchemy.
3. **Database Models**: Defines SQLAlchemy models representing database tables.

## API Endpoints

### `/insert-data/`: 
- POST endpoint for inserting data into the database. Accepts JSON payloads with the data to be inserted.
- Make sure to include the table name as a query parameter in the URL.
- Example = "http://localhost:8000/insert-data/?table_name=departments"

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