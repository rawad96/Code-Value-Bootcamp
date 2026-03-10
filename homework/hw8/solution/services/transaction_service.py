from ..repository.transaction_repositort import TransactionRepository
from ..models.transaction import Transaction
from uuid import uuid4


class TransactionService:
    def __init__(self):
        self.repo = TransactionRepository()

    def creat_trnsaction(self, trnsaction: Transaction) -> dict[str, str]:
        new_trnsaction = Transaction(
            id=uuid4(),
            account_id=trnsaction.account_id,
            category_id=trnsaction.category_id,
            amount=trnsaction.amount,
            date=trnsaction.date,
        )
        self.repo.create(new_trnsaction)

        return {"Message": "Trnsaction created"}

    def get_all_transaction(self) -> list[Transaction]:
        transactions = self.repo.get_all()

        return transactions

    def get_all_by_account(self, account_id: str) -> list[Transaction]:
        all_trnsactions = self.repo.get_all()
        return [
            transaction
            for transaction in all_trnsactions
            if transaction.account_id == account_id
        ]

    def get_by_id(self, transaction_id: str) -> Transaction:
        transaction = self.repo.get(transaction_id)

        return transaction

    def delete_transaction(self, transaction_id: str) -> dict[str, str]:
        self.repo.delete(transaction_id)

        return {"Message": "Transaction deleted"}
