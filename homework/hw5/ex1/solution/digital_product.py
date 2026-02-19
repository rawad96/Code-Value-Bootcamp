from item import Item
from mixins import DiscountMixin

DEFALT_DISCOUNT_PERCENT = 0


class DigitalProduct(Item, DiscountMixin):
    def __init__(
        self,
        name: str,
        base_price: float,
        discount_percent: float,
        weight: float = DEFALT_DISCOUNT_PERCENT,
    ):
        super().__init__(name, base_price, weight)
        self.discount_percent = discount_percent

    def get_info(self) -> str:
        return f"""No shipping cost for a digital product!\nItem: {self.name}
Base Price: {self.base_price}\nWeight: {self.weight}\nDiscount: {self.discount_percent}\nFinal Price: {self.get_price()}"""
