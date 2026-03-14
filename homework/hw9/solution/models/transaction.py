from .base_entity import BaseEntity
from decimal import Decimal
import datetime

from sqlalchemy import Numeric, func, ForeignKey, DateTime, String

from sqlalchemy.orm import Mapped, mapped_column

DECIMAL_PRECISION = 12
DECIMAL_SCALE = 2
MAX_ID_LENGTH = 36


class Transaction(BaseEntity):
    __tablename__ = "transactions"

    account_id: Mapped[str] = mapped_column(
        String(MAX_ID_LENGTH), ForeignKey("accounts.id"), nullable=False
    )

    category_id: Mapped[str] = mapped_column(
        String(MAX_ID_LENGTH), ForeignKey("categories.id"), nullable=False
    )
    amount: Mapped[Decimal] = mapped_column(
        Numeric(DECIMAL_PRECISION, DECIMAL_SCALE), nullable=False, default=0
    )
    date: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())
