from .base_repository import BaseRepository
from ..models.category import Category, CategoryType
from .csv_accessor import CsvFileAccessor
from constants.headers import category_headers
from uuid import UUID
from typing import Optional


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, accessor: Optional[CsvFileAccessor] = None):
        super().__init__(
            accessor
            or CsvFileAccessor(file_name="categories.csv", headers=category_headers)
        )

    def _row_to_entity(self, row: dict) -> Category:
        return Category(
            id=UUID(row["id"]),
            name=row["name"],
            type=CategoryType(row["type"]),
            is_deleted=row["is_deleted"],
        )

    def _entity_to_row(self, entity: Category) -> dict:
        return {
            "id": str(entity.id),
            "name": entity.name,
            "type": str(entity.type.value),
            "is_deleted": entity.is_deleted,
        }
