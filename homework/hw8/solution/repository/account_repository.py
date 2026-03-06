from .base_repository import BaseRepository
from ..models.account import Account
from .csv_accessor import CsvFileAccessor
from typing import List
from uuid import UUID, uuid4
from pathlib import Path
from decimal import Decimal

APPEND_MODE = "a"
WRITE_MODE = "w"
READ_MODE = "r"


class AccountRepository(BaseRepository[Account]):
    def __init__(self, accessor: CsvFileAccessor):
        if accessor is None:
            accessor = CsvFileAccessor(
                file_name="accounts.csv", headers=["id", "name", "opening_balance"]
            )

        super().__init__(accessor)

    def _row_to_entity(self, row: dict) -> Account:
        return Account(
            id=UUID(row["id"]),
            name=row["name"],
            opening_balance=Decimal(row["opening_balance"]),
        )

    def _entity_to_row(self, entity: Account) -> dict:
        return {
            "id": str(entity.id),
            "name": entity.name,
            "opening_balance": str(entity.opening_balance),
        }
