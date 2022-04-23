import random
import json
import products 
import stores

prices = [0.99, 12.12, 14.00, 14.30, 200.12, 18.21, 0.55, 300, 400, 210] 
currencies = ["USD","GHS","CAD","GBP","AED","CFA","CNY","EUR"]
status = ["Available", "Out Of Stock", "3 left in stock", "Banned", "N/A"]

items = []
for x in range(10):
    content =  {
            "id": x + 1,
            "item":random.choice(products.products),
            "status":random.choice(status),
            "rating":random.randint(1, 5),
            "price":random.choice(prices),
            "currency":random.choice(currencies),
            "store": random.choice(stores.stores)
        }
    items.append(content)

with open("products.json","w") as file: 
    file.write(json.dumps({"products": items}))
    file.close()