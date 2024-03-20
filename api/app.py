from flask import Flask, request, jsonify
import psycopg2
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='validation_errors.log', level=logging.ERROR, format='%(asctime)s - %(message)s')

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='mysecretpassword',
    host='localhost'
)

# Define a route to receive new data
@app.route('/api/new_data', methods=['POST'])
def receive_new_data():
    data = request.json
    
    # Add your validation logic here
    if not validate_data(data):
        # Log validation errors
        logging.error(f"Validation error for data: {data}")
        return jsonify({'error': 'Validation failed. Transaction not inserted.'}), 400
    
    # Insert data into PostgreSQL if validation passes
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO my_table (column1, column2, ...) VALUES (%s, %s, ...)",
                (data['column1'], data['column2'], ...)  # Replace with actual data
            )
            conn.commit()
    except Exception as e:
        # Log insertion errors
        logging.error(f"Error inserting data: {e}")
        return jsonify({'error': 'Failed to insert transaction.'}), 500
    
    return jsonify({'message': 'Data received and inserted successfully'}), 200

def validate_data(data):
    # Implement your validation logic here
    # Check if data conforms to data dictionary rules
    # Return True if validation passes, False otherwise
    # For simplicity, let's assume data validation fails if 'column1' is missing
    if 'column1' not in data:
        return False
    return True

if __name__ == '__main__':
    app.run(debug=True)
