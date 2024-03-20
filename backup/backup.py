import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter
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

# Define your PostgreSQL table names
tables = ['table1', 'table2']  # Add more tables as needed

# Define AVRO schema
schema = {
    "type": "record",
    "name": "my_data",
    "fields": [
        # Define your AVRO schema fields based on your PostgreSQL table columns
        {"name": "column1", "type": "string"},
        {"name": "column2", "type": "int"},
        # Add more fields as needed
    ]
}

# Iterate over tables and backup data to AVRO files
for table in tables:
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    
    avro_file_path = f'backups/{table}_backup.avro'
    
    with open(avro_file_path, 'wb') as avro_file:
        writer = DataFileWriter(avro_file, DatumWriter(), avro.schema.Parse(json.dumps(schema)))
        
        for row in rows:
            writer.append(row)
        
        writer.close()

# Close cursor and connection
cur.close()
conn.close()
