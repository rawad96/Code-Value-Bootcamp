from typing import Generic, TypeVar, List
from csv_accessor import CsvFileAccessor
from abc import ABC, abstractmethod

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):
    def __init__(self, accessor: CsvFileAccessor):
        self.accessor = accessor

    def create(self, item: T) -> T:
        row = self._entity_to_row(item)
        self.accessor.append_row(row)
        return item

    def get(self, item_id: str) -> T | None:
        for row in self.accessor.read_all():
            if row["id"] == str(item_id):
                return self._row_to_entity(row)
        return None

    def get_all(self) -> List[T]:
        return [self._row_to_entity(row) for row in self.accessor.read_all()]

    def update(self, item: T) -> T:
        rows = self.accessor.read_all()
        new_rows = []
        for row in rows:
            if row["id"] == str(item.id):
                new_rows.append(self._entity_to_row(item))
            else:
                new_rows.append(row)
        self.accessor.write_all(new_rows)
        return item

    def delete(self, item_id: str) -> None:
        rows = self.accessor.read_all()
        rows = [row for row in rows if row["id"] != str(item_id)]
        self.accessor.write_all(rows)

    @abstractmethod
    def _row_to_entity(self, row: dict) -> T:
        pass

    @abstractmethod
    def _entity_to_row(self, entity: T) -> dict:
        pass
