from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search_dish():
    dish_name = request.args.get('dish')
    # Dummy data for demonstration
    dishes = {
        'Margherita Pizza': '10.99 USD',
        'Pepperoni Pizza': '12.99 USD',
        'Veggie Pizza': '11.99 USD'
    }
    price = dishes.get(dish_name, 'Dish not found')
    return jsonify({'dish': dish_name, 'price': price})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
