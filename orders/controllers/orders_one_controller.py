from flask import request, jsonify, send_file
from orders.services.orders_service import (
    insert_order,
    get_order_by_id,
    get_image_by_id,
)
from orders.communication.receiver_order import ReceiverOrder
from orders.communication.sender_order import SenderOrder
from util.data_to_insert import calculate_amount
from flask_restful import Resource
from orders import app, api
import json
import io


class OrderController(Resource):
    def get(self, _id):
        order_image = get_image_by_id(_id)
        return send_file(order_image, mimetype="image/jpg")

    def post(self):
        data_json = {
            'products': request.form['products'],
            'client_id': request.form['client_id']
        }

        sender = SenderOrder()
        sender.send_request(data_json['client_id'])

        products, amount = calculate_amount(data_json['products'])
        data_to_insert = {
            'products': products,
            'amount': amount,
            'client_id': data_json['client_id'],
            'payment': '',
            'address': ''
        }


api.add_resource(OrderController, "/order")
