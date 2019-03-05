from flask import Flask, jsonify, request

app = Flask(__name__)

PRODUCTS = [
        {
            'id': 1,
            'price': 99,
            'name': 'rice',
        },
        {
            'id': 2,
            'price': 77,
            'name': 'bean'

        },
        {
            'id': 3,
            'price': 45,
            'name': 'bread'

        }
]

@app.route('/')
@app.route('/api/v1/products', methods=['GET'])
def products():
    return jsonify(PRODUCTS)


@app.route('/api/v1/product/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    for product in PRODUCTS:
        if product['id'] == product_id:
            return jsonify(product), 200
    return jsonify({'Error':'Not Found'}), 404


@app.route('/api/v1/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    for product in PRODUCTS:
        if product['id'] == product_id:
            product['name'] = request.get_json().get('name')

            return jsonify(product), 200
    return jsonify({'Error':'Product not found'})



@app.route('/api/v1/products', methods=['POST'])
def add_product():
    data = request.get_json()
    PRODUCTS.append(data)
    return jsonify(data), 201


@app.route('/api/v1/product/<int:product_id>', methods=['DELETE'])
def remove_product(product_id):
    for counter, product in enumerate(PRODUCTS):
        if product['id'] == product_id:
            del PRODUCTS[counter]
            return jsonify({'Message': 'Product was Deleted'})
    return jsonify({'Message': 'Page not found'}), 404



if __name__ == '__main__':
    app.run(debug=True)
