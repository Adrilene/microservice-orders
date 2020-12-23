from orders.models.orders_model import Order

def get_orders():
    return Order.objects()


def get_order_by_id(_id):
    return Order.objects(id=_id).first()


def get_order_by_user_id(user_id):
    return Order.objects(user_id=user_id).first()


def get_last_order():
    return Order.objects().order_by('-id').first()


def get_order_by_user_agent(user_agent):
    return Order.objects(user_agent=user_agent)


def insert_order(body: dict):
    order = Order(**body)
    order.save()
    return str(order.id)
