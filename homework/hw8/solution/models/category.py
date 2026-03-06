from dataclasses import dataclass
from enum import Enum
from uuid import UUID


class CategoryType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


@dataclass
class Category:
    id: UUID
    name: str
    type: CategoryType
