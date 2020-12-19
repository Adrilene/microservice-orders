def calculate_amount(products_chosen):
    amount = 0
    products = []
    for item in products_chosen:
        products.append(item['product_id'])
        amount += item['value']

    return amount, products
