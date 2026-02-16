from amazon_api import fetch_orders_from_amazon
from data_classes import Order


class AmazonReportMaker:

    def __init__(self, fetch_orders_func=fetch_orders_from_amazon):
        self._fetch_orders_func = fetch_orders_func

    def get_my_orders_average_price(self):
        # Imagine this method makes an API call to Amazon and returns a list of orders
        orders = self._fetch_orders_func()
        if not orders:
            return 0
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)
