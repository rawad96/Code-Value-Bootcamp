from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum as SQLEnum


from .base_entity import BaseEntity
from enum import Enum

MAX_NAME_LENGTH = 100


class CategoryType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


class Category(BaseEntity):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(MAX_NAME_LENGTH), nullable=False)
    type: Mapped[CategoryType] = mapped_column(SQLEnum(CategoryType), nullable=False)
