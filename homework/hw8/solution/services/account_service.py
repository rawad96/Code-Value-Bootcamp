from ..repository.account_repository import AccountRepository
from ..models.account import Account
from .transaction_service import TransactionService
from ..models.category import CategoryType
from .category_service import CategoryService

from uuid import uuid4, UUID
from decimal import Decimal
from typing import Optional, Any


def account_to_dict(account: Account) -> dict[str, Any]:
    return {
        "id": str(account.id),
        "name": account.name,
        "opening_balance": str(account.opening_balance),
        "is_deleted": account.is_deleted,
    }


class AccountService:
    def __init__(
        self,
        repo: Optional[AccountRepository] = None,
        transaction_service: Optional[TransactionService] = None,
        category_service: Optional[CategoryService] = None,
    ):
        self.repo = repo or AccountRepository()
        self.transaction_service = transaction_service or TransactionService()
        self.category_service = category_service or CategoryService()

    def create_account(self, account: dict[str, Any]) -> dict[str, str]:
        new_account = Account(
            id=uuid4(),
            name=account["name"],
            opening_balance=account["opening_balance"],
            is_deleted="false",
        )
        self.repo.create(new_account)

        return {"Message": "Account created"}

    def get_all_accounts(self) -> list[dict[str, Any]]:
        accounts = self.repo.get_all()

        return [account_to_dict(account) for account in accounts]

    def get_by_id(self, account_id: UUID) -> dict[str, Any]:
        account = self.repo.get(account_id)

        return account_to_dict(account)

    def update_account(self, account: dict[str, Any]) -> dict[str, Any]:
        new_account = Account(
            id=account["id"],
            name=account["name"],
            opening_balance=account["opening_balance"],
            is_deleted="false",
        )
        updated_account = self.repo.update(new_account)

        return account_to_dict(updated_account)

    def delete_account(self, account_id: UUID) -> dict[str, str]:
        self.repo.delete(account_id)

        return {"Message": "Account deleted"}

    def calculate_balance(self, account_id: UUID) -> Decimal:
        account = self.repo.get(account_id)
        transactions = self.transaction_service.get_all_by_account(account_id)
        balance = Decimal(account.opening_balance)
        category_cache = {}

        for transaction in transactions:
            if transaction["category_id"] not in category_cache:
                category_cache[transaction["category_id"]] = (
                    self.category_service.get_by_id(transaction["category_id"])
                )
            category_type = category_cache[transaction["category_id"]]

            if category_type["type"] == CategoryType.INCOME.value:
                balance += Decimal(transaction["amount"])
            else:
                balance -= Decimal(transaction["amount"])

        return balance

    def calculate_net_worth(self) -> Decimal:
        accounts = self.repo.get_all()
        net_worth = Decimal(0)

        for account in accounts:
            net_worth += self.calculate_balance(account.id)

        return net_worth
