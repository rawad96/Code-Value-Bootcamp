from .base_repository import BaseRepository
from ..models.transfer import Transfer

from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession


class TransferRepository(BaseRepository[Transfer]):
    def __init__(self):
        super().__init__(Transfer)
