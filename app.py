product-api/
│── app.py  
│── README.md
│── presentation.pptx
from flask import Flask, jsonify, request
app = Flask(__name__)
products = [
    {"id": 1, "name": "Phone", "price": 500},
    {"id": 2, "name": "Laptop", "price": 1200}
]
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((p for p in products if p["id"] == id), None)
    return jsonify(product) if product else ("Not found", 404)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = next((p for p in products if p["id"] == id), None)
    if not product:
        return ("Not found", 404)
    
    data = request.json
    product["name"] = data.get("name", product["name"])
    product["price"] = data.get("price", product["price"])
    
    return jsonify(product)

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    global products
    products = [p for p in products if p["id"] != id]
    return ("Deleted", 204)

if __name__ == '__main__':
    app.run(debug=True) 
