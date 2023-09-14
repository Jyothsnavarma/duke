from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (replace with your own data source)
items = [
    {"num": 1, "name": "RAJA", "class": 5 },
    {"num": 2, "name": "RANI", "class": 2 },
    {"num": 3, "name": "RAMA", "class": 3 },
]

# Endpoint to get a list of all items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Endpoint to get a specific item by ID
@app.route('/api/items/<int:item_num>', methods=['GET'])
def get_item(item_num):
    item = next((item for item in items if item['num'] == item_num), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"message": "Item not found"}), 404

if __name__ == '__main__':
   app.run(debug=True)
