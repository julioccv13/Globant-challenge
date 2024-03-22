# Data Migrations

This directory contains scripts and documentation related to migrating data from CSV files to PostgreSQL and backing up data from PostgreSQL tables to AVRO format.

## csv_to_postgres.py

Python script for migrating data from CSV files to PostgreSQL tables.


## How to Use

1. Place your CSV files in the `data/` directory.
2. Run the `csv_to_postgres.py` script to migrate data to PostgreSQL.
3. Adjust the script according to your CSV file structure and PostgreSQL table schema.

## backup.py

Python script for backing up PostgreSQL tables to AVRO files.

## How to Use

1. Ensure that PostgreSQL is running and accessible.
2. Run the `backup.py` script to create backups of PostgreSQL tables.
3. AVRO files will be generated in the `backups/` directory.


