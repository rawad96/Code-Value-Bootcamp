from dataclasses import dataclass
from .base_entity import BaseEntity
from uuid import UUID
from decimal import Decimal
from datetime import date


@dataclass
class Transfer(BaseEntity):
    from_account_id: UUID
    to_account_id: UUID
    amount: Decimal
    date: date
    description: str
