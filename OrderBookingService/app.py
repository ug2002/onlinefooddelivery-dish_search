from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/book', methods=['POST'])
def book_order():
    data = request.json
    dish = data.get('dish')
    quantity = data.get('quantity')
    customer = data.get('customer')
    # Process the order
    # Here we would normally save the order to a database
    return jsonify({"status": "Order booked successfully", "order_id": "12345"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
