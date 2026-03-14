from .base_repository import BaseRepository
from ..models.transfer import Transfer
from .csv_accessor import CsvFileAccessor
from constants.headers import transfer_headers, CSVHeaders
from uuid import UUID
from decimal import Decimal
from datetime import date
from typing import Optional


class TransferRepository(BaseRepository[Transfer]):
    def __init__(self, accessor: Optional[CsvFileAccessor] = None):
        super().__init__(
            accessor
            or CsvFileAccessor(file_name="transfers.csv", headers=transfer_headers)
        )

    def _row_to_entity(self, row: dict) -> Transfer:
        """Returns Entity with row data"""
        return Transfer(
            id=UUID(row[CSVHeaders.ID.value]),
            from_account_id=UUID(row[CSVHeaders.FROM_ACCOUNT_ID.value]),
            to_account_id=UUID(row[CSVHeaders.TO_ACCOUNT_ID.value]),
            amount=Decimal(row[CSVHeaders.AMOUNT.value]),
            date=date.fromisoformat(row[CSVHeaders.DATE.value]),
            description=row[CSVHeaders.DESCRIPTION.value],
            is_deleted=row[CSVHeaders.IS_DELETED.value],
        )

    def _entity_to_row(self, entity: Transfer) -> dict:
        """Returns Entity data as a row"""
        return {
            CSVHeaders.ID.value: str(entity.id),
            CSVHeaders.FROM_ACCOUNT_ID.value: str(entity.from_account_id),
            CSVHeaders.TO_ACCOUNT_ID.value: str(entity.to_account_id),
            CSVHeaders.AMOUNT.value: str(entity.amount),
            CSVHeaders.DATE.value: entity.date.isoformat(),
            CSVHeaders.DESCRIPTION.value: entity.description,
            CSVHeaders.IS_DELETED.value: entity.is_deleted,
        }
