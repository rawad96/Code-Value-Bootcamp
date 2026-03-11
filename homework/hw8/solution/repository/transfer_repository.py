from .base_repository import BaseRepository
from ..models.transfer import Transfer
from .csv_accessor import CsvFileAccessor
from constants.headers import transfer_headers
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
        return Transfer(
            id=UUID(row["id"]),
            from_account_id=UUID(row["from_account_id"]),
            to_account_id=UUID(row["to_account_id"]),
            amount=Decimal(row["amount"]),
            date=date.fromisoformat(row["date"]),
            description=row["description"],
            is_deleted=row["is_deleted"],
        )

    def _entity_to_row(self, entity: Transfer) -> dict:
        return {
            "id": str(entity.id),
            "from_account_id": str(entity.from_account_id),
            "to_account_id": str(entity.to_account_id),
            "amount": str(entity.amount),
            "date": entity.date.isoformat(),
            "description": entity.description,
            "is_deleted": entity.is_deleted,
        }
