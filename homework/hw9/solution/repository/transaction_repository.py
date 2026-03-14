from .base_repository import BaseRepository
from ..models.transaction import Transaction


from datetime import date, datetime
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession


class TransactionRepository(BaseRepository[Transaction]):
    def __init__(self) -> None:
        super().__init__(Transaction)

    def _parse_date(self, date_str: str) -> date:
        """Parses date string from CSV."""
        if "/" in date_str:
            return datetime.strptime(date_str, "%m/%d/%Y").date()
        try:
            return date.fromisoformat(date_str)
        except ValueError as error:
            print(error)
        for fmt in ("%d-%m-%Y", "%m-%d-%Y"):
            try:
                return datetime.strptime(date_str, fmt).date()
            except ValueError as error:
                print(error)
        raise ValueError(f"Invalid date format: {date_str!r}")
