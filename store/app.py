from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
        {
            'id': 1,
            'size': 7,
            'price': 99,
            'country': 'Brazil'
        },
        {
            'id': 2,
            'size': 4,
            'price': 77,
            'country': 'China'
        },
        {
            'id': 3,
            'size': 9,
            'price': 45,
            'country': 'EUA'
        }
]

@app.route('/')
@app.route('/api/v1/products')
def home():
    return jsonify(products)


@app.route('/api/v1/product/<int:product_id>')
def get_product_id(product_id):
    for product in products:
        if product['id'] == product_id:
            return jsonify(products[product_id - 1]), 200
    return jsonify({'Error':'Not Found'}), 404


@app.route('/api/v1/product/<int:product_id>', methods=['PUT'])
def change_country(product_id):
    for product in products:
        if product['id'] == product_id:
            product['country'] = request.get_json().get('country')

            return jsonify(product), 200
    return jsonify({'Error':'Product not found'})



@app.route('/api/v1/products', methods=['POST'])
def save_product():
    data = request.get_json()
    products.append(data)
    return jsonify(data), 201


@app.route('/api/v1/product/<int:product_id>', methods=['DELETE'])
def remove_item(product_id):
    for product in products:
        if product['id'] == product_id:
            del products[product['id'] - 1]
    return jsonify({'Message': 'Product was Deleted'})


#@app.route('/api/v1/product/<int:product_id>', methods=['DELETE'])
#def remove_item(product_id):
#   index = product_id - 1
#    del products[index] 
#    return jsonify({'Message': 'Product was Deleted'})


if __name__ == '__main__':
    app.run(debug=True)
