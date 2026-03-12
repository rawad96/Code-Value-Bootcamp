from ..repository.transaction_repository import TransactionRepository
from ..models.transaction import Transaction
from uuid import uuid4, UUID
from typing import Optional, Any
from datetime import datetime


def transaction_to_dict(transaction: Transaction) -> dict[str, Any]:
    return {
        "id": str(transaction.id),
        "account_id": str(transaction.account_id),
        "category_id": str(transaction.category_id),
        "amount": transaction.amount,
        "date": transaction.date,
    }


class TransactionService:
    def __init__(self, repo: Optional[TransactionRepository] = None):
        self.repo = repo or TransactionRepository()

    def creat_trnsaction(self, trnsaction: dict[str, Any]) -> dict[str, str]:
        new_trnsaction = Transaction(
            id=uuid4(),
            account_id=trnsaction["account_id"],
            category_id=trnsaction["category_id"],
            amount=trnsaction["amount"],
            date=datetime.now().date(),
            is_deleted="false",
        )
        self.repo.create(new_trnsaction)

        return {"Message": "Trnsaction created"}

    def get_all_transaction(self) -> list[dict[str, Any]]:
        transactions = self.repo.get_all()
        returned_transaction = [
            transaction_to_dict(transaction) for transaction in transactions
        ]

        return returned_transaction

    def get_all_by_account(self, account_id: UUID) -> list[dict[str, Any]]:
        all_trnsactions = self.repo.get_all()
        return [
            transaction_to_dict(transaction)
            for transaction in all_trnsactions
            if transaction.account_id == account_id
        ]

    def get_by_id(self, transaction_id: UUID) -> dict[str, Any]:
        transaction = self.repo.get(transaction_id)

        return transaction_to_dict(transaction)

    def delete_transaction(self, transaction_id: UUID) -> dict[str, str]:
        self.repo.delete(transaction_id)

        return {"Message": "Transaction deleted"}
