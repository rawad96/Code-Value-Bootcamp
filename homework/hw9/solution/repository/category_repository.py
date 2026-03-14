from .base_repository import BaseRepository
from ..models.category import Category
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession


class CategoryRepository(BaseRepository[Category]):
    def __init__(self):
        super().__init__(Category)
