from digital_product import DigitalProduct
from product import Product

BASE_PRICE = 1000.0
WEIGHT = 2.5

if __name__ == "__main__":
    laptop = Product("Laptop", BASE_PRICE, WEIGHT, discount_percent=10)
    print(laptop.get_price())  # Output: 900.0
    print(laptop.get_shipping_cost())  # Output: 12.5
    print(laptop.get_total_cost())  # Output: 912.5
    print(laptop.get_info())

    # ebook = DigitalProduct("Python Guide", 29.99, discount_percent=20)
    # print(ebook.get_price())  # Output: 23.992
    # print(ebook.get_info())
