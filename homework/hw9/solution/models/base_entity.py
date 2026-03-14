from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from solution.database import Base
from uuid import uuid4, UUID

MAX_ID_LENGTH = 36


class BaseEntity(Base):
    __abstract__ = True

    id: Mapped[UUID] = mapped_column(
        String(MAX_ID_LENGTH),
        primary_key=True,
        default=lambda: str(uuid4()),
        unique=True,
        nullable=False,
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
