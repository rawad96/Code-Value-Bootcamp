from ..repository.account_repository import AccountRepository
from ..models.account import Account
from .transaction_service import TransactionService
from ..models.category import CategoryType
from .category_service import CategoryService

from solution.database import async_session_maker

from uuid import UUID
from decimal import Decimal
from typing import Optional, Any

from constants.headers import TablesHeaders


def account_to_dict(account: Account) -> dict[str, Any]:
    """Returns account as dict."""
    return {
        TablesHeaders.ID.value: str(account.id),
        TablesHeaders.NAME.value: account.name,
        TablesHeaders.OPENING_BALANCE.value: str(account.opening_balance),
        TablesHeaders.IS_DELETED.value: account.is_deleted,
    }


class AccountService:
    def __init__(
        self,
        repo: Optional[AccountRepository] = None,
        transaction_service: Optional[TransactionService] = None,
        category_service: Optional[CategoryService] = None,
        session_maker=None,
    ):
        self.repo = repo or AccountRepository()
        self.transaction_service = transaction_service or TransactionService()
        self.category_service = category_service or CategoryService()
        self.session_maker = session_maker or async_session_maker

    async def create_account(self, account: dict[str, Any]) -> dict[str, str]:
        """Creates account and returns message."""
        async with self.session_maker() as session:
            async with session.begin():
                new_account = Account(
                    name=account["name"],
                    opening_balance=account["opening_balance"],
                )
                result = await self.repo.create(new_account, session)
            return account_to_dict(result)

    async def get_all_accounts(self) -> list[dict[str, Any]]:
        """Returns all accounts as dicts."""
        async with self.session_maker() as session:
            accounts = await self.repo.get_all(session)
            return [account_to_dict(account) for account in accounts]

        return [account_to_dict(account) for account in accounts]

    async def get_by_id(self, account_id: UUID) -> dict[str, Any] | None:
        """Returns account by id or None."""
        async with self.session_maker() as session:
            account = await self.repo.get(account_id, session)
            if account is None:
                return None
            return account_to_dict(account)

    async def update_account(self, account: dict[str, Any]) -> dict[str, Any]:
        """Updates account and returns it as dict."""
        async with self.session_maker() as session:
            async with session.begin():
                new_account = Account(
                    id=account["id"],
                    name=account["name"],
                    opening_balance=account["opening_balance"],
                    is_deleted=False,
                )
                updated_account = await self.repo.update(new_account, session)
            return account_to_dict(updated_account)

    async def delete_account(self, account_id: UUID) -> dict[str, str]:
        """Deletes account and returns message."""
        async with self.session_maker() as session:
            await self.repo.delete(account_id, session)
            return {"Message": "Account deleted"}

    async def calculate_balance(self, account_id: UUID) -> Decimal:
        """Calculates balance for a given account."""
        async with self.session_maker() as session:
            account = await self.repo.get(account_id, session)
            if account is None:
                raise ValueError(f"Account with id {account_id} not found")

            transactions = await self.transaction_service.get_all_by_account(account_id)
            balance = Decimal(account.opening_balance)
            category_cache = {}

            if not transactions:
                return balance

            for transaction in transactions:
                category_id = transaction[TablesHeaders.CATEGORY_ID.value]

                if category_id not in category_cache:
                    category_cache[category_id] = await self.category_service.get_by_id(
                        category_id
                    )

                category_type = category_cache[category_id]
                if category_type is None:
                    raise ValueError(f"Missed Category Type for category {category_id}")

                if category_type[TablesHeaders.TYPE.value] == CategoryType.INCOME.value:
                    balance += Decimal(transaction[TablesHeaders.AMOUNT.value])
                else:
                    balance -= Decimal(transaction[TablesHeaders.AMOUNT.value])

            return balance

    async def calculate_net_worth(self) -> Decimal:
        """Returns total net worth of all accounts."""
        async with self.session_maker() as session:
            accounts = await self.repo.get_all(session)
            net_worth = Decimal(0)
            for account in accounts:
                balance = await self.calculate_balance(account.id)
                net_worth += balance
            return net_worth
