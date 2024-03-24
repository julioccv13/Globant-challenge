# Database management

This directory contains scripts and documentation related to migrating data from CSV files to PostgreSQL and backing up data from PostgreSQL tables to AVRO format.

## migration.py

This service provides functionality for interacting with a PostgreSQL database. It includes functions for establishing a connection to the database, creating tables, and inserting data.

## Features
- Connect to a PostgreSQL database using SQLAlchemy.
- Create tables with specified schemas.
- Read data from CSV or XLS files and insert it into the database.

## backup.py

This service connects to a PostgreSQL database, reads all tables, and creates backups of each table in Avro format.

## Features

- Connects to a PostgreSQL database using SQLAlchemy.
- Dynamically generates Avro schema based on the database table schema.
- Backs up each table to Avro format.

## recovery.py

This service allows you to restore tables from Avro files into a PostgreSQL database.

## Features

- Connects to a PostgreSQL database using SQLAlchemy.
- Read data from Avro backup files organized by date.
- Insert the data into the appropriate tables in the database.


