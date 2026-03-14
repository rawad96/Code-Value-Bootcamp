from .base_entity import BaseEntity
from decimal import Decimal
import datetime

from sqlalchemy import Numeric, DateTime, String, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

MAX_DESCRIPTION_LENGTH = 100
DECIMAL_PRECISION = 12
DECIMAL_SCALE = 2
MAX_ID_LENGTH = 36


class Transfer(BaseEntity):
    __tablename__ = "transfers"

    from_account_id: Mapped[str] = mapped_column(
        String(MAX_ID_LENGTH), ForeignKey("accounts.id"), nullable=False
    )
    to_account_id: Mapped[str] = mapped_column(
        String(MAX_ID_LENGTH), ForeignKey("accounts.id"), nullable=False
    )
    amount: Mapped[Decimal] = mapped_column(
        Numeric(DECIMAL_PRECISION, DECIMAL_SCALE), nullable=False, default=0
    )
    date: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())
    description: Mapped[str] = mapped_column(
        String(MAX_DESCRIPTION_LENGTH), nullable=True
    )
