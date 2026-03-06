import pandas as pd
import random
from datetime import datetime, timedelta

products = ["Laptop", "Phone", "Keyboard", "Mouse", "Headphones"]
cities = ["Delhi", "Mumbai", "Bangalore", "Pune", "Jaipur"]

data = []

for i in range(1000):

    order = {
        "order_id": i,
        "customer_id": random.randint(100,500),
        "product": random.choice(products),
        "price": random.randint(500,50000),
        "quantity": random.randint(1,5),
        "city": random.choice(cities),
        "order_date": datetime.now() - timedelta(days=random.randint(1,100))
    }

    data.append(order)

df = pd.DataFrame(data)

df.to_csv("data/orders_raw.csv", index=False)

print("Raw dataset created")