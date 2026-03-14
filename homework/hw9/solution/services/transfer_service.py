from ..repository.transfer_repository import TransferRepository
from ..services.transaction_service import TransactionService
from ..services.category_service import CategoryService
from ..models.transfer import Transfer
from uuid import UUID
from typing import Optional, Any
from constants.headers import TablesHeaders

from solution.database import async_session_maker
from sqlalchemy.ext.asyncio import AsyncSession


def transfer_to_dict(transfer: Transfer) -> dict[str, Any]:
    """Returns transfer as dict."""
    return {
        TablesHeaders.ID.value: str(transfer.id),
        TablesHeaders.FROM_ACCOUNT_ID.value: str(transfer.from_account_id),
        TablesHeaders.TO_ACCOUNT_ID.value: str(transfer.to_account_id),
        TablesHeaders.AMOUNT.value: str(transfer.amount),
        TablesHeaders.DATE.value: transfer.date.isoformat(),
        TablesHeaders.DESCRIPTION.value: transfer.description,
    }


class TransferService:
    def __init__(
        self,
        repo: Optional[TransferRepository] = None,
        transaction_service: Optional[TransactionService] = None,
        category_service: Optional[CategoryService] = None,
        session_maker: AsyncSession = None,
    ):
        self.repo = repo or TransferRepository()
        self.transaction_service = transaction_service or TransactionService()
        self.category_service = category_service or CategoryService()
        self.session_maker = session_maker or async_session_maker

    async def creat_transfer(self, transfer: dict[str, Any]) -> dict[str, str]:
        """Creates transfer and returns it."""
        async with self.session_maker() as session:
            async with session.begin():
                new_transfer = Transfer(
                    from_account_id=transfer[TablesHeaders.FROM_ACCOUNT_ID.value],
                    to_account_id=transfer[TablesHeaders.TO_ACCOUNT_ID.value],
                    amount=transfer[TablesHeaders.AMOUNT.value],
                    description=transfer[TablesHeaders.DESCRIPTION.value],
                )
                created_transfer = await self.repo.create(new_transfer, session)

                transfer_out = await self.category_service.get_by_name("Transfer Out")
                transfer_in = await self.category_service.get_by_name("Transfer In")

                if transfer_in is None or transfer_out is None:
                    raise ValueError(
                        "Transfer categories not found: transfer_in or transfer_out is None"
                    )

                withdraw = {
                    TablesHeaders.ACCOUNT_ID.value: transfer[
                        TablesHeaders.FROM_ACCOUNT_ID.value
                    ],
                    TablesHeaders.CATEGORY_ID.value: transfer_out[
                        TablesHeaders.ID.value
                    ],
                    TablesHeaders.AMOUNT.value: transfer[TablesHeaders.AMOUNT.value],
                }

                deposit = {
                    TablesHeaders.ACCOUNT_ID.value: transfer[
                        TablesHeaders.TO_ACCOUNT_ID.value
                    ],
                    TablesHeaders.CATEGORY_ID.value: transfer_in[
                        TablesHeaders.ID.value
                    ],
                    TablesHeaders.AMOUNT.value: transfer[TablesHeaders.AMOUNT.value],
                }

                await self.transaction_service.creat_trnsaction(withdraw)
                await self.transaction_service.creat_trnsaction(deposit)

            return transfer_to_dict(created_transfer)

    async def get_all_transfers(self) -> list[dict[str, Any]]:
        """Returns all transfers as dicts."""
        async with self.session_maker() as session:
            transfers = await self.repo.get_all(session)
            return [transfer_to_dict(transfer) for transfer in transfers]

    async def get_all_by_account(self, account_id: UUID) -> list[dict[str, Any]]:
        """Returns all transfers for account."""
        async with self.session_maker() as session:
            transfers = await self.repo.get_all(session)
            return [
                transfer_to_dict(transfer)
                for transfer in transfers
                if transfer.from_account_id == str(account_id)
                or transfer.to_account_id == str(account_id)
            ]

    async def get_by_id(self, transfer_id: UUID) -> dict[str, Any] | None:
        """Returns transfer by id."""
        async with self.session_maker() as session:
            transfer = await self.repo.get(str(transfer_id), session)
            if transfer is None:
                return None
            return transfer_to_dict(transfer)

    async def delete_transfer(self, transfer_id: UUID) -> dict[str, str]:
        """Deletes transfer and returns message."""
        async with self.session_maker() as session:
            async with session.begin():
                await self.repo.delete(str(transfer_id), session)
            return {"Message": "Transfer deleted"}
