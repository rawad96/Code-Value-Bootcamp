from .base_repository import BaseRepository
from ..models.account import Account
from .csv_accessor import CsvFileAccessor
from uuid import UUID
from decimal import Decimal
from constants.headers import account_headers, CSVHeaders
from typing import Optional


class AccountRepository(BaseRepository[Account]):
    def __init__(self, accessor: Optional[CsvFileAccessor] = None):
        super().__init__(
            accessor
            or CsvFileAccessor(file_name="accounts.csv", headers=account_headers)
        )

    def _row_to_entity(self, row: dict) -> Account:
        """Returns Entity with row data"""
        return Account(
            id=UUID(row[CSVHeaders.ID.value]),
            name=row[CSVHeaders.NAME.value],
            opening_balance=Decimal(row[CSVHeaders.OPENING_BALANCE.value]),
            is_deleted=row[CSVHeaders.IS_DELETED.value],
        )

    def _entity_to_row(self, entity: Account) -> dict:
        """Returns Entity data as a row"""
        return {
            CSVHeaders.ID.value: str(entity.id),
            CSVHeaders.NAME.value: entity.name,
            CSVHeaders.OPENING_BALANCE.value: str(entity.opening_balance),
            CSVHeaders.IS_DELETED.value: entity.is_deleted,
        }
