from .base_repository import BaseRepository
from ..models.account import Account


class AccountRepository(BaseRepository[Account]):
    def __init__(self):
        super().__init__(Account)
