from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (replace with your own data source)
items = [
    {"id": 1, "name": "RAJA"},
    {"id": 2, "name": "RANI"},
    {"id": 3, "name": "RAMA"},
]

# Endpoint to get a list of all items

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Endpoint to get a specific item by ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"message": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
