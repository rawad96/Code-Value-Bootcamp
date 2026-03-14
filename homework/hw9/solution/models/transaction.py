from .base_entity import BaseEntity
from decimal import Decimal
import datetime

from sqlalchemy import Numeric, Date, func, ForeignKey

from sqlalchemy.orm import Mapped, mapped_column

DECIMAL_PRECISION = 12
DECIMAL_SCALE = 2


class Transaction(BaseEntity):
    __tablename__ = "transactions"

    account_id: Mapped[str] = mapped_column(ForeignKey("accounts.id"), nullable=False)
    category_id: Mapped[str] = mapped_column(
        ForeignKey("categories.id"), nullable=False
    )
    amount: Mapped[Decimal] = mapped_column(
        Numeric(DECIMAL_PRECISION, DECIMAL_SCALE), nullable=False, default=0
    )
    date: Mapped[datetime.date] = mapped_column(
        Date, server_default=func.current_date, nullable=False
    )
