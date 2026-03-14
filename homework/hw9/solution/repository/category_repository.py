from .base_repository import BaseRepository
from ..models.category import Category, CategoryType
from .csv_accessor import CsvFileAccessor
from constants.headers import category_headers, CSVHeaders
from uuid import UUID
from typing import Optional


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, accessor: Optional[CsvFileAccessor] = None):
        super().__init__(
            accessor
            or CsvFileAccessor(file_name="categories.csv", headers=category_headers)
        )

    def _row_to_entity(self, row: dict) -> Category:
        """Returns Entity with row data"""
        return Category(
            id=UUID(row[CSVHeaders.ID.value]),
            name=row[CSVHeaders.NAME.value],
            type=CategoryType(row[CSVHeaders.TYPE.value]),
            is_deleted=row[CSVHeaders.IS_DELETED.value],
        )

    def _entity_to_row(self, entity: Category) -> dict:
        """Returns Entity data as a row"""
        return {
            CSVHeaders.ID.value: str(entity.id),
            CSVHeaders.NAME.value: entity.name,
            CSVHeaders.TYPE.value: str(entity.type.value),
            CSVHeaders.IS_DELETED.value: entity.is_deleted,
        }
