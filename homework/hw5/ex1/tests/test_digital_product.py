from solution.digital_product import DigitalProduct
import pytest


def test_digital_product():
    ebook = DigitalProduct("Python Guide", 29.99, discount_percent=20)
    assert ebook.get_price() == 23.992
    assert (
        ebook.get_info()
        == "No shipping cost for a digital product!\nItem: Python Guide\nBase Price: 29.99\nWeight: 0.0\nDiscount: 20\nFinal Price: 23.992"
    )


def test_digital_product_no_discount():
    ebook = DigitalProduct("Python Guide", 29.99, discount_percent=0)
    assert ebook.get_price() == 29.99
    assert (
        ebook.get_info()
        == "No shipping cost for a digital product!\nItem: Python Guide\nBase Price: 29.99\nWeight: 0.0\nDiscount: 0\nFinal Price: 29.99"
    )
