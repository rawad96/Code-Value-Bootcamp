from dataclasses import dataclass
from .base_entity import BaseEntity
from uuid import UUID
from decimal import Decimal
from datetime import date


@dataclass
class Transaction(BaseEntity):
    account_id: UUID
    category_id: UUID
    amount: Decimal
    date: date
