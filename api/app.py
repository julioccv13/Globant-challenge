from flask import Flask, request
from utils.request_handler import handle_data

app = Flask(__name__)

@app.route('/api/receive_data', methods=['POST'])
def handle_request():
    return handle_data()

if __name__ == "__main__":
    app.run(debug=True)
