from ..repository.transaction_repository import TransactionRepository
from ..models.transaction import Transaction
from uuid import uuid4, UUID
from typing import Optional, Any
from datetime import datetime
from constants.headers import CSVHeaders

from solution.models.transaction import Transaction


def transaction_to_dict(transaction: Transaction) -> dict[str, Any]:
    """Returns transaction as dict."""
    return {
        CSVHeaders.ID.value: str(transaction.id),
        CSVHeaders.ACCOUNT_ID.value: str(transaction.account_id),
        CSVHeaders.CATEGORY_ID.value: str(transaction.category_id),
        CSVHeaders.AMOUNT.value: transaction.amount,
        CSVHeaders.DATE.value: transaction.date,
    }


class TransactionService:
    def __init__(self, repo: Optional[TransactionRepository] = None):
        self.repo = repo or TransactionRepository()

    def creat_trnsaction(self, trnsaction: dict[str, Any]) -> dict[str, str]:
        """Creates transaction and returns message."""
        new_trnsaction = Transaction(
            id=uuid4(),
            account_id=trnsaction[CSVHeaders.ACCOUNT_ID.value],
            category_id=trnsaction[CSVHeaders.CATEGORY_ID.value],
            amount=trnsaction[CSVHeaders.AMOUNT.value],
            date=datetime.now().date(),
            is_deleted="false",
        )
        self.repo.create(new_trnsaction)

        return {"Message": "Trnsaction created"}

    def get_all_transaction(self) -> list[dict[str, Any]]:
        """Returns all transactions as dicts."""
        transactions = self.repo.get_all()
        returned_transaction = [
            transaction_to_dict(transaction) for transaction in transactions
        ]

        return returned_transaction

    def get_all_by_account(self, account_id: UUID) -> list[dict[str, Any]]:
        """Returns all transactions for account."""
        all_trnsactions = self.repo.get_all()
        return [
            transaction_to_dict(transaction)
            for transaction in all_trnsactions
            if transaction.account_id == account_id
        ]

    def get_by_id(self, transaction_id: UUID) -> dict[str, Any] | None:
        """Returns transaction by id or None."""
        transaction = self.repo.get(transaction_id)
        if transaction is None:
            return None

        return transaction_to_dict(transaction)

    def delete_transaction(self, transaction_id: UUID) -> dict[str, str]:
        """Deletes transaction and returns message."""
        self.repo.delete(transaction_id)

        return {"Message": "Transaction deleted"}
