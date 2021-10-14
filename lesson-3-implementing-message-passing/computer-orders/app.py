import json
from flask import Flask, jsonify, request

from .services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(retrieve_orders())


@app.route('/orders', methods=['POST'])
def post_orders():
    return jsonify(create_order(request.json))


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})


if __name__ == '__main__':
    app.run()
