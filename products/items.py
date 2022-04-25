import random
import json
from .products import products
from .stores import stores

prices = [0.99, 12.12, 14.00, 14.30, 200.12, 18.21, 0.55, 300, 400, 210] 
currencies = ["USD","GHS","CAD","GBP","AED","CFA","CNY","EUR"]
status = ["Available", "Out Of Stock", "3 left in stock", "Banned", "N/A"]

def generateProducts(number):
    items = []
    for x in range(number):
        content =  {
                "id": x + 1,
                "item":random.choice(products),
                "status":random.choice(status),
                "rating":random.randint(1, 5),
                "price":random.choice(prices),
                "currency":random.choice(currencies),
                "store": random.choice(stores)
            }
        items.append(content)
    return json.dumps({"products":items})