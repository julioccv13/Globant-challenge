import os
import pandas as pd
from utils.csv_handler import read_csv
from utils.database_handler import migrate_csv_to_postgres

if __name__ == "__main__":
    # Specify the directory containing CSV and XLS files
    data_dir = 'data'

    # Iterate over files in the data directory
    for file_name in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file_name)
        
        # Check if the file is a CSV or XLS file
        if file_name.endswith('.csv'):
            data = read_csv(file_path)
        elif file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            data = pd.read_excel(file_path).to_dict(orient='records')
        else:
            print(f"Ignoring file {file_name} - Unsupported file format")
            continue
        
        # Extract table name from file name
        table_name = os.path.splitext(file_name)[0]
        
        try:
            migrate_csv_to_postgres(data, table_name)
            print(f"Data from {file_path} migrated to {table_name} successfully!")
        except Exception as e:
            print(f"Error occurred while migrating data from {file_path}: {e}")
