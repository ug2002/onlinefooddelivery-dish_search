# order-cancellation-service/app.py
from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

ORDERS_FILE = 'orders.json'

# Initialize the orders file if it doesn't exist
if not os.path.exists(ORDERS_FILE):
    with open(ORDERS_FILE, 'w') as f:
        json.dump([], f)

@app.route('/cancel', methods=['POST'])
def cancel_order():
    cancel_request = request.json
    with open(ORDERS_FILE, 'r') as f:
        orders = json.load(f)
    updated_orders = [order for order in orders if order != cancel_request]
    with open(ORDERS_FILE, 'w') as f:
        json.dump(updated_orders, f)
    return jsonify({"message": "Order cancelled successfully", "order": cancel_request}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
