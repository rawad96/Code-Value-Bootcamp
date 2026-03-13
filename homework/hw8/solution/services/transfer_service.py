from ..repository.transfer_repository import TransferRepository
from ..services.transaction_service import TransactionService
from ..services.category_service import CategoryService
from ..models.transaction import Transaction
from ..models.transfer import Transfer
from uuid import uuid4, UUID
from typing import Optional, Any
from datetime import datetime
from constants.headers import CSVHeaders


def transfer_to_dict(transfer: Transfer) -> dict[str, Any]:
    """Returns transfer as dict."""
    return {
        CSVHeaders.ID.value: str(transfer.id),
        CSVHeaders.FROM_ACCOUNT_ID.value: str(transfer.from_account_id),
        CSVHeaders.TO_ACCOUNT_ID.value: str(transfer.to_account_id),
        CSVHeaders.AMOUNT.value: str(transfer.amount),
        CSVHeaders.DATE.value: transfer.date.isoformat(),
        CSVHeaders.DESCRIPTION.value: transfer.description,
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
            from_account_id=transfer[CSVHeaders.FROM_ACCOUNT_ID.value],
            to_account_id=transfer[CSVHeaders.TO_ACCOUNT_ID.value],
            amount=transfer[CSVHeaders.AMOUNT.value],
            date=datetime.now().date(),
            description=transfer[CSVHeaders.DESCRIPTION.value],
            is_deleted="false",
        )
        self.repo.create(new_transfer)

        transfer_out = self.category_service.get_by_name("Transfer Out")
        transfer_in = self.category_service.get_by_name("Transfer In")

        if transfer_in is None or transfer_out is None:
            raise ValueError(
                "Transfer categories not found: transfer_in or transfer_out is None"
            )

        withdraw = {
            CSVHeaders.ACCOUNT_ID.value: transfer[CSVHeaders.FROM_ACCOUNT_ID.value],
            CSVHeaders.CATEGORY_ID.value: transfer_out[CSVHeaders.ID.value],
            CSVHeaders.AMOUNT.value: transfer[CSVHeaders.AMOUNT.value],
        }

        deposit = {
            CSVHeaders.ACCOUNT_ID.value: transfer[CSVHeaders.TO_ACCOUNT_ID.value],
            CSVHeaders.CATEGORY_ID.value: transfer_in[CSVHeaders.ID.value],
            CSVHeaders.AMOUNT.value: transfer[CSVHeaders.AMOUNT.value],
        }

        self.transaction_service.creat_trnsaction(withdraw)
        self.transaction_service.creat_trnsaction(deposit)

        return {"Message": "Transfer created"}

    def get_all_transfers(self) -> list[dict[str, Any]]:
        """Returns all transfers as dicts."""
        transfers = self.repo.get_all()

        return [transfer_to_dict(transfer) for transfer in transfers]

    def get_all_by_account(self, account_id: UUID) -> list[dict[str, Any]]:
        """Returns all transfers for account."""
        all_transfers = self.repo.get_all()
        return [
            transfer_to_dict(transfer)
            for transfer in all_transfers
            if transfer.from_account_id == account_id
            or transfer.to_account_id == account_id
        ]

    def get_by_id(self, transfer_id: UUID) -> dict[str, Any]:
        """Returns transfer by id."""
        transfer = self.repo.get(transfer_id)
        if transfer is None:
            raise ValueError(f"Transfer with id {transfer_id} not found")

        return transfer_to_dict(transfer)

    def delete_transfer(self, transfer_id: UUID) -> dict[str, str]:
        """Deletes transfer and returns message."""
        self.repo.delete(transfer_id)

        return {"Message": "Transfer deleted"}
