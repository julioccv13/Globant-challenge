from flask import request
from utils.database_handler import connect_to_database

def receive_data(table_name):
    data = request.json

    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {table_name} (column1, column2) VALUES (%s, %s)", (data['value1'], data['value2']))
    conn.commit()
    cur.close()
    conn.close()

    return "Data received and inserted successfully!"

def handle_data():
    try:
        response = receive_data(table_name='example_table')
        return response, 200
    except Exception as e:
        return str(e), 500
