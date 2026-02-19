from solution.product import Product
import pytest

BASE_PRICE = 1000.0
WEIGHT = 2.5

EXPECTED_PRICE_WITH_DISCOUNT = 900.0
EXPECTED_SHIPPING_COST = 12.5
EXPECTED_TOTAL_COST = 912.5


EXPECTED_PRICE_WITHOUT_DISCOUNT = 1000.0
EXPECTED_TOTAL_COST_WITHOUT_DISCOUNT = 1012.5


def test_product() -> None:
    laptop = Product("Laptop", BASE_PRICE, WEIGHT, discount_percent=10)
    assert laptop.get_price() == EXPECTED_PRICE_WITH_DISCOUNT
    assert laptop.get_shipping_cost() == EXPECTED_SHIPPING_COST
    assert laptop.get_total_cost() == EXPECTED_TOTAL_COST
    assert (
        laptop.get_info()
        == f"Item: Laptop\nBase Price: {BASE_PRICE}\nWeight: {WEIGHT}\nDiscount: 10\nShipping cost: {EXPECTED_SHIPPING_COST}"
    )


def test_product_no_discount() -> None:
    laptop = Product("Laptop", BASE_PRICE, WEIGHT, discount_percent=0)
    assert laptop.get_price() == EXPECTED_PRICE_WITHOUT_DISCOUNT
    assert laptop.get_shipping_cost() == EXPECTED_SHIPPING_COST
    assert laptop.get_total_cost() == EXPECTED_TOTAL_COST_WITHOUT_DISCOUNT
    assert (
        laptop.get_info()
        == f"Item: Laptop\nBase Price: {BASE_PRICE}\nWeight: {WEIGHT}\nDiscount: 0\nShipping cost: {EXPECTED_SHIPPING_COST}"
    )
