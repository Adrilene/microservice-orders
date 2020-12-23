from orders.models.orders_model import Order

def get_orders():
    return Order.objects()


def get_order_by_id(_id):
    return Order.objects(id=_id).first()


def get_last_order():
    return Order.objects().order_by('-id').first()


def insert_order(body: dict):
    order = Order(**body)
    order.save()
    return str(order.id)
