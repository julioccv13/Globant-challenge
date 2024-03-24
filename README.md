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

### 4. Backup and Recovery

- Backups are stored on the local file system in the `backups/` directory.
- Use the provided backup script (`backup.py`) to create backups of PostgreSQL tables in AVRO format.
- Use the provided recovery script (`recovery.py`) to restore PostgreSQL tables from backup files in AVRO format.
