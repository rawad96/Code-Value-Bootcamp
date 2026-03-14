import datetime
from decimal import Decimal

from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from solution.models.base_entity import BaseEntity

MAX_NAME_LENGTH = 100
DECIMAL_PRECISION = 12
DECIMAL_SCALE = 2


class Account(BaseEntity):
    __tablename__ = "accounts"
    name: Mapped[str] = mapped_column(String(MAX_NAME_LENGTH), nullable=False)
    opening_balance: Mapped[Decimal] = mapped_column(
        Numeric(DECIMAL_PRECISION, DECIMAL_SCALE), nullable=False
    )
