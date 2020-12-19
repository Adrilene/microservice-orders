import json
import requests
from orders.services.orders_service import get_last_order

def get_products_values(products): 
    values = []
    for product in products: 
        response = requests.get(f'http://localhost:5000/product/{product}')
        values.append(response.json()['price'])
    
    return sum(values)


def generate_nfe_id(): 
    nfe_id = 1
    last = get_last_order()
    if last: 
        last = json.loads(last.to_json())
        nfe_id = last['nfe_id'] + 1

    return nfe_id

