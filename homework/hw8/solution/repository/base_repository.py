from typing import Generic, TypeVar
from .csv_accessor import CsvFileAccessor
from ..models.base_entity import BaseEntity
from abc import ABC, abstractmethod
from uuid import UUID
from constants.headers import CSVHeaders

T_ENTITY = TypeVar("T_ENTITY", bound=BaseEntity)


class BaseRepository(ABC, Generic[T_ENTITY]):
    def __init__(self, accessor: CsvFileAccessor):
        self.accessor = accessor

    def create(self, item: T_ENTITY) -> T_ENTITY:
        """Adds item and returns it."""
        row = self._entity_to_row(item)
        self.accessor.append_row(row)
        return item

    def get(self, item_id: UUID) -> T_ENTITY | None:
        rows = self.accessor.read_all()
        for row in rows:
            if (
                row[CSVHeaders.ID.value] == str(item_id)
                and row[CSVHeaders.IS_DELETED.value] != "true"
            ):
                return self._row_to_entity(row)
        return None

    def get_all(self) -> list[T_ENTITY]:
        """Returns all items."""
        rows = self.accessor.read_all()
        return [
            self._row_to_entity(row)
            for row in rows
            if row[CSVHeaders.IS_DELETED.value] != "true"
        ]

    def update(self, item: T_ENTITY) -> T_ENTITY:
        rows = self.accessor.read_all()
        new_rows = []
        for row in rows:
            if row[CSVHeaders.ID.value] == str(item.id):
                new_rows.append(self._entity_to_row(item))
            else:
                new_rows.append(row)
        self.accessor.write_all(new_rows)
        return item

    def delete(self, item_id: str | UUID) -> None:
        """Marks item as deleted."""
        rows = self.accessor.read_all()
        for row in rows:
            if row[CSVHeaders.ID.value] == str(item_id):
                row[CSVHeaders.IS_DELETED.value] = "true"
        self.accessor.write_all(rows)

    @abstractmethod
    def _row_to_entity(self, row: dict) -> T_ENTITY:
        """Returns Entity with row data"""
        raise NotImplementedError

    @abstractmethod
    def _entity_to_row(self, entity: T_ENTITY) -> dict:
        """Returns Entity data as a row"""
        raise NotImplementedError
