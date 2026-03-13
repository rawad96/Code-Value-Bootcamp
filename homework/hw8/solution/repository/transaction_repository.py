from .base_repository import BaseRepository
from ..models.transaction import Transaction
from .csv_accessor import CsvFileAccessor
from constants.headers import CSVHeaders, transaction_headers
from uuid import UUID
from decimal import Decimal
from datetime import date, datetime
from typing import Optional


class TransactionRepository(BaseRepository[Transaction]):
    def __init__(self, accessor: Optional[CsvFileAccessor] = None):
        super().__init__(
            accessor
            or CsvFileAccessor(
                file_name="transactions.csv", headers=transaction_headers
            )
        )

    def _parse_date(self, date_str: str) -> date:
        """Parses date string from CSV."""
        if "/" in date_str:
            return datetime.strptime(date_str, "%m/%d/%Y").date()
        try:
            return date.fromisoformat(date_str)
        except ValueError as error:
            print(error)
        for fmt in ("%d-%m-%Y", "%m-%d-%Y"):
            try:
                return datetime.strptime(date_str, fmt).date()
            except ValueError as error:
                print(error)
        raise ValueError(f"Invalid date format: {date_str!r}")

    def _row_to_entity(self, row: dict) -> Transaction:
        """Returns Entity with row data"""
        date_value = self._parse_date(row[CSVHeaders.DATE.value])
        return Transaction(
            id=UUID(row[CSVHeaders.ID.value]),
            account_id=UUID(row[CSVHeaders.ACCOUNT_ID.value]),
            category_id=UUID(row[CSVHeaders.CATEGORY_ID.value]),
            amount=Decimal(row[CSVHeaders.AMOUNT.value]),
            date=date_value,
            is_deleted=row[CSVHeaders.IS_DELETED.value],
        )

    def _entity_to_row(self, entity: Transaction) -> dict:
        """Returns Entity data as a row"""
        return {
            CSVHeaders.ID.value: str(entity.id),
            CSVHeaders.ACCOUNT_ID.value: str(entity.account_id),
            CSVHeaders.CATEGORY_ID.value: str(entity.category_id),
            CSVHeaders.AMOUNT.value: str(entity.amount),
            CSVHeaders.DATE.value: entity.date.isoformat(),
            CSVHeaders.IS_DELETED.value: entity.is_deleted,
        }
