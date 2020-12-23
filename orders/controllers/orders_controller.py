from flask import request, jsonify, send_file
from orders.services.orders_service import (
    insert_order,
    get_order_by_id,
    get_order_by_user_id,
    get_order_by_user_agent
)
from orders.util.request_products import get_products_values
from flask_restful import Resource
from orders import app, api
import json
import io
import ast
import random

class OrderByIdController(Resource):
    def get(self, _id):
        order = get_order_by_id(_id)
        if order:
            order = json.loads(order.to_json())
            return order

class OrderController(Resource):
    def post(self):
        data_json = {
            'products': request.json['products'],
            'user_id': request.json['user_id'],
            'payment_method': request.json['payment_method']
        }

        data_json['nfe_id'] = random.randint(1,10000)
        data_json['amount'] = get_products_values(data_json['products'])
        data_json['user_agent'] = request.headers.get('User-Agent')
        insert_order(data_json)
        
        return 'OK', 200

class OrderByUserIdController(Resource):
    def get(self, user_id):
        order = get_order_by_user_id(user_id)
        if order:
            order = json.loads(order.to_json())
            return [order], 200


class OrderByUserAgentController(Resource):
    def get(self):
        order = get_order_by_user_agent(request.headers.get('User-Agent'))
        if order:
            order = json.loads(order.to_json())
            return [order], 200
    
        return [], 200


api.add_resource(OrderController, "/order")
api.add_resource(OrderByIdController, "/order/<_id>")
api.add_resource(OrderByUserIdController, "/order_user/<user_id>")
api.add_resource(OrderByUserAgentController, "/order_user_agent")
