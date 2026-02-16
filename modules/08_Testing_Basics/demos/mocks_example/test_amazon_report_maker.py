from unittest.mock import Mock


from amazon_api import fetch_orders_from_amazon
from amazon_report_maker import AmazonReportMaker
from data_classes import Order


# def test_without_mock():
#     report_maker = AmazonReportMaker()
#     average_price = report_maker.get_my_orders_average_price()
#     assert average_price == 19.99

def test_get_my_orders_average_price():
    # Create a mock for the fetch_orders_from_amazon function
    mock_fetch_orders = Mock(return_value=[
        Order(id=1, price=10.0, item_name="Item 1"),
        Order(id=2, price=20.0, item_name="Item 2"),
        Order(id=3, price=30.0, item_name="Item 3"),
    ])

    report_maker = AmazonReportMaker(mock_fetch_orders)
    average_price = report_maker.get_my_orders_average_price()
    assert average_price == 20.0
    mock_fetch_orders.assert_called_once()
