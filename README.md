# Globant-challenge

This Python service provides functionality for ingesting historic data into a PostgreSQL database, exposing endpoints via FastAPI for data manipulation, and includes backup and recovery services for the database tables.

## Description

### 1. Database Connection

The database connection module establishes a connection with a PostgreSQL database to ingest historic data. It provides functions to interact with the database, such as inserting data and executing queries.

### 2. FastAPI Service

The FastAPI service module utilizes FastAPI to create a REST API for interacting with the PostgreSQL database. It exposes three endpoints:
- `/process_data`: This POST endpoint allows users to insert new data into the connected PostgreSQL database. Users can send data in JSON format to be stored in the database.
- `/hires_per_quarter`: This GET endpoint executes a specific query on the connected PostgreSQL database and returns the result.
- `/above_avg_department_hires`: This GET endpoint executes a second specific query requirement on the connected PostgreSQL database and returns the result. 

### 3. Backup and Recovery Service

- Backups are stored on the local file system in the `backups/` directory.
- Use the provided backup script (`backup.py`) to create backups of PostgreSQL tables in AVRO format.
- Use the provided recovery script (`recovery.py`) to restore PostgreSQL tables from backup files in AVRO format.


