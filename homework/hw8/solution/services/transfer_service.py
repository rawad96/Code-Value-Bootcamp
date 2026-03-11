from ..repository.transfer_repository import TransferRepository
from ..services.transaction_service import TransactionService
from ..services.category_service import CategoryService
from ..models.transaction import Transaction
from ..models.transfer import Transfer
from uuid import uuid4, UUID
from typing import Optional


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

    def creat_transfer(self, transfer: Transfer) -> dict[str, str]:
        new_transfer = Transfer(
            id=uuid4(),
            from_account_id=transfer.from_account_id,
            to_account_id=transfer.to_account_id,
            amount=transfer.amount,
            date=transfer.date,
            description=transfer.description,
        )
        self.repo.create(new_transfer)

        transfer_out = self.category_service.get_by_name("Transfer Out")
        transfer_in = self.category_service.get_by_name("Transfer In")

        withdraw = Transaction(
            id=uuid4(),
            account_id=transfer.from_account_id,
            category_id=transfer_out.id,
            amount=transfer.amount,
            date=transfer.date,
        )

        deposit = Transaction(
            id=uuid4(),
            account_id=transfer.to_account_id,
            category_id=transfer_in.id,
            amount=transfer.amount,
            date=transfer.date,
        )

        self.transaction_service.creat_trnsaction(withdraw)
        self.transaction_service.creat_trnsaction(deposit)

        return {"Message": "Transfer created"}

    def get_all_transfers(self) -> list[Transfer]:
        transfers = self.repo.get_all()

        return transfers

    def get_all_by_account(self, account_id: UUID) -> list[Transfer]:
        all_transfers = self.repo.get_all()
        return [
            transfer
            for transfer in all_transfers
            if transfer.from_account_id == account_id
            or transfer.to_account_id == account_id
        ]

    def get_by_id(self, transfer_id: UUID) -> Transfer:
        transfer = self.repo.get(transfer_id)

        return transfer

    def delete_transfer(self, transfer_id: UUID) -> dict[str, str]:
        self.repo.delete(transfer_id)

        return {"Message": "Transfer deleted"}
