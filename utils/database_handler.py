import psycopg2

def connect_to_database():
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='mysecretpassword',
        host='localhost'
    )
    return conn

def migrate_csv_to_postgres(data, table_name):
    conn = connect_to_database()
    cur = conn.cursor()

    for row in data:
        cur.execute(
            f"INSERT INTO {table_name} (column1, column2, column3) VALUES (%s, %s, %s)",
            (row['column1'], row['column2'], row['column3'])
        )

    conn.commit()
    cur.close()
    conn.close()

def create_backup(table_name):
    conn = connect_to_database()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()

    with open('backup.avro', 'w') as file:
        for row in rows:
            file.write(','.join(map(str, row)) + '\n')

    cur.close()
    conn.close()
