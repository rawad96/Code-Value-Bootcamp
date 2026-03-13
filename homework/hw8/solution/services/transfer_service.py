from ..repository.transfer_repository import TransferRepository
from ..services.transaction_service import TransactionService
from ..services.category_service import CategoryService
from ..models.transaction import Transaction
from ..models.transfer import Transfer
from uuid import uuid4, UUID
from typing import Optional, Any
from datetime import datetime

ID = "id"
NAME = "name"
AMOUNT = "amount"
IS_DELETED = "is_deleted"
OPENING_BALANCE = "opening_balance"
ACCOUNT_ID = "account_id"
TYPE = "type"
FROM_ACCOUNT_ID = "from_account_id"
TO_ACCOUNT_ID = "to_account_id"
DATE = "date"
DESCRIPTION = "description"
CATEGORY_ID = "category_id"


def transfer_to_dict(transfer: Transfer) -> dict[str, Any]:
    return {
        ID: str(transfer.id),
        FROM_ACCOUNT_ID: str(transfer.from_account_id),
        TO_ACCOUNT_ID: str(transfer.to_account_id),
        AMOUNT: str(transfer.amount),
        DATE: transfer.date.isoformat(),
        DESCRIPTION: transfer.description,
    }


class TransferService:
    def __init__(
        self,
        repo: Optional[TransferRepository] = None,
        transaction_service: Optional[TransactionService] = None,
        category_service: Optional[CategoryService] = None,
    ):
        self.repo = repo or TransferRepository()
        self.transaction_service = transaction_service or TransactionService()
        self.category_service = category_service or CategoryService()

    def creat_transfer(self, transfer: dict[str, Any]) -> dict[str, str]:
        new_transfer = Transfer(
            id=uuid4(),
            from_account_id=transfer[FROM_ACCOUNT_ID],
            to_account_id=transfer[TO_ACCOUNT_ID],
            amount=transfer[AMOUNT],
            date=datetime.now().date(),
            description=transfer[DESCRIPTION],
            is_deleted="false",
        )
        self.repo.create(new_transfer)

        transfer_out = self.category_service.get_by_name("Transfer Out")
        transfer_in = self.category_service.get_by_name("Transfer In")

        withdraw = {
            ACCOUNT_ID: transfer[FROM_ACCOUNT_ID],
            CATEGORY_ID: transfer_out[ID],
            AMOUNT: transfer[AMOUNT],
        }

        deposit = {
            ACCOUNT_ID: transfer[TO_ACCOUNT_ID],
            CATEGORY_ID: transfer_in[ID],
            AMOUNT: transfer[AMOUNT],
        }

        self.transaction_service.creat_trnsaction(withdraw)
        self.transaction_service.creat_trnsaction(deposit)

        return {"Message": "Transfer created"}

    def get_all_transfers(self) -> list[dict[str, Any]]:
        transfers = self.repo.get_all()

        return [transfer_to_dict(transfer) for transfer in transfers]

    def get_all_by_account(self, account_id: UUID) -> list[dict[str, Any]]:
        all_transfers = self.repo.get_all()
        return [
            transfer_to_dict(transfer)
            for transfer in all_transfers
            if transfer.from_account_id == account_id
            or transfer.to_account_id == account_id
        ]

    def get_by_id(self, transfer_id: UUID) -> dict[str, Any]:
        transfer = self.repo.get(transfer_id)

        return transfer_to_dict(transfer)

    def delete_transfer(self, transfer_id: UUID) -> dict[str, str]:
        self.repo.delete(transfer_id)

        return {"Message": "Transfer deleted"}
