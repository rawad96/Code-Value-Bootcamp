from ..repository.transaction_repository import TransactionRepository
from ..models.transaction import Transaction
from uuid import UUID
from typing import Optional, Any
from constants.headers import TablesHeaders

from solution.models.transaction import Transaction

from solution.database import async_session_maker
from sqlalchemy.ext.asyncio import AsyncSession


def transaction_to_dict(transaction: Transaction) -> dict[str, Any]:
    """Returns transaction as dict."""
    return {
        TablesHeaders.ID.value: str(transaction.id),
        TablesHeaders.ACCOUNT_ID.value: str(transaction.account_id),
        TablesHeaders.CATEGORY_ID.value: str(transaction.category_id),
        TablesHeaders.AMOUNT.value: transaction.amount,
        TablesHeaders.DATE.value: transaction.date,
    }


class TransactionService:
    def __init__(
        self,
        repo: Optional[TransactionRepository] = None,
        session_maker: AsyncSession = None,
    ):
        self.repo = repo or TransactionRepository()
        self.session_maker = session_maker or async_session_maker

    async def creat_trnsaction(self, trnsaction: dict[str, Any]) -> dict[str, Any]:
        """Creates transaction and returns it."""
        async with self.session_maker() as session:
            async with session.begin():
                new_transaction = Transaction(
                    account_id=trnsaction[TablesHeaders.ACCOUNT_ID.value],
                    category_id=trnsaction[TablesHeaders.CATEGORY_ID.value],
                    amount=trnsaction[TablesHeaders.AMOUNT.value],
                )
                result = await self.repo.create(new_transaction, session)
            return transaction_to_dict(result)

    async def get_all_transaction(self) -> list[dict[str, Any]]:
        """Returns all transactions as dicts."""
        async with self.session_maker() as session:
            transactions = await self.repo.get_all(session)
            return [transaction_to_dict(transaction) for transaction in transactions]

    async def get_all_by_account(self, account_id: UUID) -> list[dict[str, Any]]:
        """Returns all transactions for account."""
        async with self.session_maker() as session:
            transactions = await self.repo.get_all(session)
            return [
                transaction_to_dict(transaction)
                for transaction in transactions
                if transaction.account_id == str(account_id)
            ]

    async def get_by_id(self, transaction_id: UUID) -> dict[str, Any] | None:
        """Returns transaction by id or None."""
        async with self.session_maker() as session:
            transaction = await self.repo.get(str(transaction_id), session)
            if transaction is None:
                return None
            return transaction_to_dict(transaction)

    async def delete_transaction(self, transaction_id: UUID) -> dict[str, str]:
        """Deletes transaction and returns message."""
        async with self.session_maker() as session:
            async with session.begin():
                await self.repo.delete(str(transaction_id), session)
            return {"Message": "Transaction deleted"}
