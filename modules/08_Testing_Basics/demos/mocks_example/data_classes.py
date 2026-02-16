from dataclasses import dataclass


@dataclass
class Order:
    id: int
    price: float
    item_name: str