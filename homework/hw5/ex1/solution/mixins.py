DEFALT_DISCOUNT_PERCENT = 0
SHIPPING_RATE_PER_KG = 5


class DiscountMixin:
    discount_percent: float = DEFALT_DISCOUNT_PERCENT
    base_price: float

    def get_price(self) -> float:
        return self.base_price * (1 - self.discount_percent / 100)


class ShippingMixin:
    shipping_rate_per_kg: float = SHIPPING_RATE_PER_KG
    weight: float

    def get_shipping_cost(self) -> float:
        return self.weight * self.shipping_rate_per_kg
