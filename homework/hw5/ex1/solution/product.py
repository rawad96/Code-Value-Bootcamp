from mixins import DiscountMixin, ShippingMixin
from item import Item


class Product(Item, DiscountMixin, ShippingMixin):

    def __init__(
        self, name: str, base_price: float, weight: float, discount_percent: float
    ):
        super().__init__(name, base_price, weight)
        self.discount_percent = discount_percent

    def get_info(self) -> str:
        return f"Item: {self.name}\nBase Price: {self.base_price}\nWeight: {self.weight}\nDiscount: {self.discount_percent}\nShipping cost: {self.get_shipping_cost()}"

    def get_total_cost(self) -> float:
        return self.get_price() + self.get_shipping_cost()
