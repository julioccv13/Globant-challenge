import os
from utils.csv_handler import read_csv
from utils.database_handler import migrate_csv_to_postgres

import os
from utils.csv_handler import read_csv
from utils.database_handler import migrate_csv_to_postgres

if __name__ == "__main__":
    # Specify the directory containing CSV files
    data_dir = 'data'

    # Iterate over files in the data directory
    for file_name in os.listdir(data_dir):
        if file_name.endswith('.csv'):
            # Construct full file path
            csv_file_path = os.path.join(data_dir, file_name)
            
            # Extract table name from file name (assumes file name without extension is table name)
            table_name = os.path.splitext(file_name)[0]
            
            try:
                data = read_csv(csv_file_path)
                migrate_csv_to_postgres(data, table_name)
                print(f"Data from {csv_file_path} migrated to {table_name} successfully!")
            except Exception as e:
                print(f"Error occurred while migrating data from {csv_file_path}: {e}")
