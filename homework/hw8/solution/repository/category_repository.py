from .base_repository import BaseRepository
from ..models.category import Category, CategoryType
from .csv_accessor import CsvFileAccessor
from constants.headers import category_headers
from uuid import UUID


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, accessor: CsvFileAccessor):
        if accessor is None:
            accessor = CsvFileAccessor(
                file_name="categories.csv", headers=category_headers
            )

        super().__init__(accessor)

    def _row_to_entity(self, row: dict) -> Category:
        return Category(
            id=UUID(row["id"]),
            name=row["name"],
            type=CategoryType(row["type"]),
        )

    def _entity_to_row(self, entity: Category) -> dict:
        return {
            "id": str(entity.id),
            "name": entity.name,
            "type": str(entity.type.value),
        }
