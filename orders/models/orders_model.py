from orders import db
from datetime import datetime


class Order(db.Document):
    meta = {"collection": "orders"}
    products = db.ListField(db.StringField(), required=True)
    amount = db.FloatField(required=True)
    client_id = db.StringField(required=True)
    payment_method = db.StringField(max_length=50, required=True)
    nfe_id = db.IntField(required=True)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
