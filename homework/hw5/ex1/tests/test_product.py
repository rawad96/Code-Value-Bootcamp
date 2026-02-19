from solution.product import Product
import pytest


def test_product():
    laptop = Product("Laptop", 1000.0, 2.5, discount_percent=10)
    assert laptop.get_price() == 900.0
    assert laptop.get_shipping_cost() == 12.5
    assert laptop.get_total_cost() == 912.5
    assert (
        laptop.get_info()
        == "Item: Laptop\nBase Price: 1000.0\nWeight: 2.5\nDiscount: 10\nShipping cost: 12.5"
    )


def test_product_no_discount():
    laptop = Product("Laptop", 1000.0, 2.5, discount_percent=0)
    assert laptop.get_price() == 1000.0
    assert laptop.get_shipping_cost() == 12.5
    assert laptop.get_total_cost() == 1012.5
    assert (
        laptop.get_info()
        == "Item: Laptop\nBase Price: 1000.0\nWeight: 2.5\nDiscount: 0\nShipping cost: 12.5"
    )
