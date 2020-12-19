from orders import db
from datetime import datetime


class Product(db.Document):
    meta = {"collection": "orders"}
    products = db.ListField(db.StringField(), required=True)
    amount = db.FloatField(required=True)
    client_id = db.StringField(required=True)
    payment = db.StringField(max_length=50, srequired=True)
    address = db.StringField(max_length=200, required=True)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
