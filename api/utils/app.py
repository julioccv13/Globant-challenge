from flask import Flask, request, jsonify
from utils.shared import insert_data

app = Flask(__name__)

# Endpoint to receive data and insert it into the appropriate table
@app.route('/api/insert', methods=['POST'])
def insert():
    data = request.json
    success, message = insert_data(data)
    if success:
        return jsonify({'message': message}), 201
    else:
        return jsonify({'error': message}), 400

if __name__ == '__main__':
    app.run(debug=True)


