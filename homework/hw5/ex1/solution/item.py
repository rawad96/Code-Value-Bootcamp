class Item:
    def __init__(self, name: str, base_price: float, weight: float):
        self.name = name
        self.base_price = base_price
        self.weight = weight

    def get_info(self) -> str:
        return (
            f"Item: {self.name}, Base Price: {self.base_price}, Weight: {self.weight}"
        )
