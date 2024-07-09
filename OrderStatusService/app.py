# order-status-service/app.py
from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

ORDERS_FILE = 'orders.json'

# Initialize the orders file if it doesn't exist
if not os.path.exists(ORDERS_FILE):
    with open(ORDERS_FILE, 'w') as f:
        json.dump([], f)

@app.route('/status', methods=['GET'])
def order_status():
    with open(ORDERS_FILE, 'r') as f:
        orders = json.load(f)
    return jsonify(orders), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
