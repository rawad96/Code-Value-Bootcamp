from .base_repository import BaseRepository
from ..models.account import Account
from .csv_accessor import CsvFileAccessor
from uuid import UUID
from decimal import Decimal
from constants.headers import account_headers


class AccountRepository(BaseRepository[Account]):
    def __init__(self, accessor: CsvFileAccessor):
        if accessor is None:
            accessor = CsvFileAccessor(
                file_name="accounts.csv", headers=account_headers
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
