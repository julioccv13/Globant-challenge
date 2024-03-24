# API Service

This directory contains files and documentation related to the REST API service built with Flask and SQLAlchemy that the receives new data for the database. 

## Features

- Insert new employees, departments, and jobs into the database
- Dynamically route incoming data to the appropriate table based on specific criteria
- Log exceptions during data insertion to a file

## API Endpoints

- Insert Data
- URL: /api/insert
- Method: POST
- Request Body: JSON data representing an employee, department, or job
- Example: {
  "id": "12",
  "department": "IT",
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
Exceptions during data insertion are logged to a file named logs inside the api/logs folder.