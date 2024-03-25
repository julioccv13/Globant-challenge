import os
import fastavro
import pandas as pd

# Function to restore tables from Avro format
def restore_tables_from_avro(engine, backup_dir):
    # Get all Avro files in the backup directory
    avro_files = [file for file in os.listdir(backup_dir) if file.endswith('.avro')]    
    # Restore tables from each Avro file
    for avro_file in avro_files:
    # Extract table name from file name   
        table_name = os.path.splitext(avro_file)[0]     
        avro_file_path = os.path.join(backup_dir, avro_file)        
        # Read Avro file and convert data to DataFrame
        with open(avro_file_path, 'rb') as f:
            avro_reader = fastavro.reader(f)
            data = [record for record in avro_reader]
            df = pd.DataFrame(data)        
        # Insert data into the respective table
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)        
        print(f"Table '{table_name}' restored successfully from '{avro_file_path}'")
