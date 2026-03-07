from dataclasses import dataclass
from .base_entity import BaseEntity
from enum import Enum


class CategoryType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


@dataclass
class Category(BaseEntity):
    name: str
    type: CategoryType
