from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass
class Account:
    id: UUID
    name: str
    opening_balance: Decimal
