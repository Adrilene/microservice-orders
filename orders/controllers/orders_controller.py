from flask import request, jsonify, send_file
from orders.services.orders_service import (
    insert_order,
    get_order_by_id
)
from orders.util.request_products import get_products_values, generate_nfe_id
from flask_restful import Resource
from orders import app, api
import json
import io
import ast

class OrderByIdController(Resource):
    def get(self, _id):
        order = get_order_by_id(_id)
        order = json.loads(order.to_json())
        return order

class OrderController(Resource):

    def post(self):
        delivery_fee = request.form['delivery_fee']
        data_json = {
            'products': ast.literal_eval(request.form['products']),
            'client_id': request.form['client_id'],
            'payment_method': request.form['payment_method']
        }
        data_json['nfe_id'] = generate_nfe_id()
        data_json['amount'] = get_products_values(data_json['products']) + float(delivery_fee)
        insert_order(data_json)
        return 'OK'


api.add_resource(OrderController, "/order")
api.add_resource(OrderByIdController, "/order/<_id>")
