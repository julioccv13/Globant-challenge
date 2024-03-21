import sys
from utils.csv_handler import read_csv
from utils.database_handler import connect_to_database, migrate_csv_to_postgres

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python csv_to_postgres.py <table_name> <csv_file_path>")
        sys.exit(1)
    
    table_name = sys.argv[1]
    csv_file_path = sys.argv[2]
    
    try:
        data = read_csv(csv_file_path)
        migrate_csv_to_postgres(data, table_name)
        print("Data migrated successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")
