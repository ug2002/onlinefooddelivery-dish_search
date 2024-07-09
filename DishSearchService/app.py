# DishSearchService app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# Load dishes from a text file
def load_dishes():
    dishes = []
    try:
        with open('dishes.txt', 'r') as f:
            for line in f:
                dishes.append(line.strip())
    except FileNotFoundError:
        pass
    return dishes

dishes = load_dishes()

@app.route('/search', methods=['GET'])
def search():
    dish_name = request.args.get('dish', '').lower()
    results = [dish for dish in dishes if dish.lower() == dish_name]
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
