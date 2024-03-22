import psycopg2

def connect_to_database():
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='admin',
        host='localhost'
    )
    return conn

def migrate_csv_to_postgres(data, table_name):
    conn = connect_to_database()
    cur = conn.cursor()

    # Get the column names from the first row of the CSV data
    columns = list(data[0].keys())

    # Generate the SQL query dynamically based on column names
    placeholders = ', '.join(['%s'] * len(columns))
    columns_str = ', '.join(columns)
    insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"

    # Insert data into PostgreSQL table
    for row in data:
        values = [row[col] for col in columns]
        cur.execute(insert_query, values)

    conn.commit()
    cur.close()
    conn.close()

def create_backup(table_name):
    conn = connect_to_database()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()

    with open(f'backup_{table_name}.avro', 'w') as file:
        for row in rows:
            file.write(','.join(map(str, row)) + '\n')

    cur.close()
    conn.close()
