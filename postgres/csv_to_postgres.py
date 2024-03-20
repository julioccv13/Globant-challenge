import csv
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='mysecretpassword',
    host='localhost'
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Define your CSV file path
csv_file_path = 'data.csv'

# Define your PostgreSQL table creation SQL
create_table_sql = """
CREATE TABLE IF NOT EXISTS my_table (
    id SERIAL PRIMARY KEY,
    column1 VARCHAR(255),
    column2 INTEGER,
    ...
);
"""

# Execute the table creation SQL
cur.execute(create_table_sql)

# Open and read CSV file
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row if present
    for row in reader:
        # Insert data into PostgreSQL
        cur.execute(
            "INSERT INTO my_table (column1, column2, ...) VALUES (%s, %s, ...)",
            row
        )

# Commit the transaction
conn.commit()

# Close cursor and connection
cur.close()
conn.close()
