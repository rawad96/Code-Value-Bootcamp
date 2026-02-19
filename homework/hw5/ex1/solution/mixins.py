class DiscountMixin:
    discount_percent: float = 0.0

    def get_price(self) -> float:
        return self.base_price * (1 - self.discount_percent / 100)


class ShippingMixin:
    shipping_rate_per_kg: float = 5.0

    def get_shipping_cost(self) -> float:
        return self.weight * self.shipping_rate_per_kg
