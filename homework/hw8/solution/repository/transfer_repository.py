from .base_repository import BaseRepository
from ..models.transfer import Transfer
from .csv_accessor import CsvFileAccessor
from constants.headers import transfer_headers
from uuid import UUID
from decimal import Decimal
from datetime import date


class TransferRepository(BaseRepository[Transfer]):
    def __init__(self, accessor: CsvFileAccessor):
        if accessor is None:
            accessor = CsvFileAccessor(
                file_name="transfers.csv", headers=transfer_headers
            )

        super().__init__(accessor)

    def _row_to_entity(self, row: dict) -> Transfer:
        return Transfer(
            id=UUID(row["id"]),
            from_account_id=UUID(row["from_account_id"]),
            to_account_id=UUID(row["to_account_id"]),
            amount=Decimal(row["amount"]),
            date=date.fromisoformat(row["date"]),
            description=row["description"],
        )

    def _entity_to_row(self, entity: Transfer) -> dict:
        return {
            "id": str(entity.id),
            "from_account_id": entity.name,
            "to_account_id": str(entity.type.value),
            "amount": str(entity.amount),
            "date": entity.date.isoformat(),
            "description": entity.description,
        }
