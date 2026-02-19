from solution.digital_product import DigitalProduct
import pytest

BASE_PRICE = 29.99

EXPECTED_PRICE_WITH_DISCOUNT = 23.992
EXPECTED_PRICE_WITHOUT_DISCOUNT = 29.99


def test_digital_product() -> None:
    ebook = DigitalProduct("Python Guide", BASE_PRICE, discount_percent=20)
    assert ebook.get_price() == EXPECTED_PRICE_WITH_DISCOUNT
    assert (
        ebook.get_info()
        == f"No shipping cost for a digital product!\nItem: Python Guide\nBase Price: {BASE_PRICE}\nWeight: 0.0\nDiscount: 20\nFinal Price: {EXPECTED_PRICE_WITH_DISCOUNT}"
    )


def test_digital_product_no_discount() -> None:
    ebook = DigitalProduct("Python Guide", BASE_PRICE, discount_percent=0)
    assert ebook.get_price() == EXPECTED_PRICE_WITHOUT_DISCOUNT
    assert (
        ebook.get_info()
        == "No shipping cost for a digital product!\nItem: Python Guide\nBase Price: 29.99\nWeight: 0.0\nDiscount: 0\nFinal Price: 29.99"
    )
