from utils.database_handler import connect_to_database, create_backup

if __name__ == "__main__":
    table_name = 'example_table'
    create_backup(table_name)
