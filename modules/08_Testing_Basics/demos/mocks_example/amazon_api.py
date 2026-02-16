import time
from data_classes import Order


def fetch_orders_from_amazon():
    # This function simulates fetching orders from Amazon's API
    time.sleep(10)  # Simulate network delay
    return [
        Order(id=1, price=19.99, item_name="Book"),
        Order(id=2, price=29.99, item_name="Headphones"),
        Order(id=3, price=9.99, item_name="Mouse"),
    ]