from repository.account_repository import AccountRepository
from models.account import Account
from .transaction_service import TransactionService
from models.category import CategoryType
from .category_service import CategoryService

from uuid import uuid4
from decimal import Decimal


class AccountService:
    def __init__(
        self, transaction_service: TransactionService, category_service: CategoryService
    ):
        self.repo = AccountRepository()
        self.transaction_service = transaction_service
        self.category_service = category_service

    def create_account(self, account: Account) -> dict[str, str]:
        new_account = Account(
            id=uuid4(), name=account.name, opening_balance=account.opening_balance
        )
        self.repo.create(new_account)

        return {"Message": "Account created"}

    def get_all_accounts(self) -> list[Account]:
        accounts = self.repo.get_all()

        return accounts

    def get_by_id(self, account_id: str) -> Account:
        account = self.repo.get(account_id)

        return account

    def update_account(self, account: Account) -> Account:
        updated_account = self.repo.update(account)

        return updated_account

    def delete_account(self, account_id: str) -> dict[str, str]:
        self.repo.delete(account_id)

        return {"Message": "Account deleted"}

    def calculate_balance(self, account_id: str) -> Decimal:
        account = self.repo.get(account_id)
        transactions = self.transaction_service.get_all_by_account(account_id)
        balance = Decimal(account.opening_balance)
        category_cache = {}

        for transaction in transactions:
            if transaction.category_id not in category_cache:
                category_cache[transaction.category_id] = (
                    self.category_service.get_by_id(transaction.category_id)
                )
            category_type = category_cache[transaction.category_id]

            if category_type.type == CategoryType.INCOME:
                balance += Decimal(transaction.amount)
            else:
                balance -= Decimal(transaction.amount)

        return balance

    def calculate_net_worth(self) -> Decimal:
        accounts = self.get_all_accounts()
        net_worth = Decimal(0)

        for account in accounts:
            net_worth += self.calculate_balance(account.id)

        return net_worth
