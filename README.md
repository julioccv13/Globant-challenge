# globant-challenge

This project involves migrating historic data from CSV files to a PostgreSQL database, creating a REST API service to receive new data, and implementing backup and restore features.

## Setup

### 1. PostgreSQL Database

- Install PostgreSQL locally on your machine. You can download it from [PostgreSQL Downloads](https://www.postgresql.org/download/).
- Create a PostgreSQL database and define tables as needed for your project.

### 2. Docker Container (Optional)

- If you prefer, you can use Docker for local deployment.
- Ensure Docker is installed and running on your local machine.
- Modify the Dockerfile to use the locally installed PostgreSQL database.

### 3. Flask Application

- Install Python dependencies using `pip install -r requirements.txt`.
- Update the Flask application (`app.py`) to connect to your PostgreSQL database.
- Run the Flask application locally using `python app.py`.

### 4. Backup and Restore

- Backups are stored on the local file system in the `backups/` directory.
- Use the provided backup script (`backup_script.py`) to create backups of PostgreSQL tables in AVRO format.

## Components

### 1. Data Migration

- **migrations/** directory contains scripts for migrating data from CSV files to PostgreSQL.
- Use `csv_to_postgres.py` to migrate data from CSV files to PostgreSQL tables.
- Adjust the script according to your CSV file structure and PostgreSQL table schema.

### 2. REST API Service

- **api/** directory contains files related to the REST API service.
- Use `app.py` to run the Flask application for the REST API service.
- Endpoints are defined for receiving new data and batch transactions.
- Ensure data validation and insertion logic are implemented as needed.

### 3. Backups

- **backups/** directory contains scripts and documentation related to backup features.
- Use `backup_script.py` to create backups of PostgreSQL tables in AVRO format.
- Adjust the script to save backups locally in the `backups/` directory.

## Usage

1. **Data Migration**:
   - Place CSV files in the `data/` directory.
   - Run `csv_to_postgres.py` to migrate data to PostgreSQL.

2. **REST API Service**:
   - Run `app.py` to start the Flask application for the REST API service.
   - Use appropriate endpoints for receiving new data and batch transactions.

3. **Backups**:
   - Run `backup_script.py` to create backups of PostgreSQL tables.
   - Adjust the script to customize backup configurations as needed.

