from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column

from solution.database import Base


class BaseEntity(Base):
    __abstract__ = True

    id: Mapped[str] = mapped_column(primary_key=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
