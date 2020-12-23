import json
import requests
from orders.services.orders_service import get_last_order
import random

def get_products_values(products): 
    values = []
    for product in products: 
        response = requests.get(f'http://localhost:5000/product/{product}')
        values.append(response.json()['price'])
    
    return sum(values)


# ef generate_nfe_id(): 
#     nfe_id = 1
#     last = get_last_order()
#     last = json.loads(last.to_json())
#     if 'nfe_id' in last: 
#         nfe_id = last['nfe_id'] + 1

#     return nfe_id
# d
