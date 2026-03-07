from dataclasses import dataclass
from .base_entity import BaseEntity
from decimal import Decimal
from uuid import UUID


@dataclass
class Account(BaseEntity):
    name: str
    opening_balance: Decimal
