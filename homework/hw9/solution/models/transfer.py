from .base_entity import BaseEntity
from decimal import Decimal
from datetime import date

from sqlalchemy import Numeric, Date, String, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

MAX_DESCRIPTION_LENGTH = 100
DECIMAL_PRECISION = 12
DECIMAL_SCALE = 2


class Transfer(BaseEntity):
    __tablename__ = "transfers"

    from_account_id: Mapped[str] = mapped_column(
        ForeignKey("accounts.id"), nullable=False
    )
    to_account_id: Mapped[str] = mapped_column(
        ForeignKey("accounts.id"), nullable=False
    )
    amount: Mapped[Decimal] = mapped_column(
        Numeric(DECIMAL_PRECISION, DECIMAL_SCALE), nullable=False, default=0
    )
    date: Mapped[date] = mapped_column(
        Date, server_default=func.current_date(), nullable=False
    )
    description: Mapped[str] = mapped_column(
        String(MAX_DESCRIPTION_LENGTH), nullable=True
    )
