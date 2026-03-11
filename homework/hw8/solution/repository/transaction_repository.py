from .base_repository import BaseRepository
from ..models.transaction import Transaction
from .csv_accessor import CsvFileAccessor
from constants.headers import transaction_headers
from uuid import UUID
from decimal import Decimal
from datetime import date
from typing import Optional


class TransactionRepository(BaseRepository[Transaction]):
    def __init__(self, accessor: Optional[CsvFileAccessor] = None):
        super().__init__(
            accessor
            or CsvFileAccessor(
                file_name="transactions.csv", headers=transaction_headers
            )
        )

    def _row_to_entity(self, row: dict) -> Transaction:
        return Transaction(
            id=UUID(row["id"]),
            account_id=UUID(row["account_id"]),
            category_id=UUID(row["category_id"]),
            amount=Decimal(row["amount"]),
            date=date.fromisoformat(row["date"]),
            is_deleted=row["is_deleted"],
        )

    def _entity_to_row(self, entity: Transaction) -> dict:
        return {
            "id": str(entity.id),
            "account_id": str(entity.account_id),
            "category_id": str(entity.category_id),
            "amount": str(entity.amount),
            "date": entity.date.isoformat(),
            "is_deleted": entity.is_deleted,
        }
