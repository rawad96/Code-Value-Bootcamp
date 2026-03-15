from typing import Any, Optional
from decimal import Decimal
from datetime import datetime

from .account_service import AccountService
from .transaction_service import TransactionService
from .category_service import CategoryService
from constants.headers import TablesHeaders


INCOME = "income"
EXPENSE = "expense"


class ReportsService:
    def __init__(
        self,
        account_service: Optional[AccountService] = None,
        transaction_service: Optional[TransactionService] = None,
        category_service: Optional[CategoryService] = None,
    ):
        self.account_service = account_service or AccountService()
        self.transaction_service = transaction_service or TransactionService()
        self.category_service = category_service or CategoryService()

    async def monthly_summary(self, year: int, month: int) -> dict[str, Any]:
        """Returns income, expenses and net flow for month."""
        transactions = await self.transaction_service.get_all_transaction()
        category_cache = await self._build_category_cache()

        income = Decimal(0)
        expenses = Decimal(0)

        for transaction in transactions:
            if (
                transaction[TablesHeaders.DATE.value].year == year
                and transaction[TablesHeaders.DATE.value].month == month
            ):
                category = category_cache.get(
                    transaction[TablesHeaders.CATEGORY_ID.value]
                )

                if category is None:
                    raise ValueError("Missed Category")

                if category[TablesHeaders.TYPE.value] == INCOME:
                    income += Decimal(transaction[TablesHeaders.AMOUNT.value])
                else:
                    expenses += Decimal(transaction[TablesHeaders.AMOUNT.value])

        net_flow = income - expenses

        return {
            "year": year,
            "month": month,
            "total_income": str(income),
            "total_expenses": str(expenses),
            "net_cash_flow": str(net_flow),
        }

    async def spending_by_category(self, year: int, month: int) -> list[dict[str, Any]]:
        """Returns total per category for month."""
        transactions = await self.transaction_service.get_all_transaction()
        category_cache = await self._build_category_cache()

        category_totals: dict[str, Decimal] = {}

        for transaction in transactions:
            if (
                transaction[TablesHeaders.DATE.value].year == year
                and transaction[TablesHeaders.DATE.value].month == month
            ):
                category = category_cache.get(
                    transaction[TablesHeaders.CATEGORY_ID.value]
                )

                if category is None:
                    raise ValueError("Missed Category")

                if category[TablesHeaders.TYPE.value] == EXPENSE:
                    name = category[TablesHeaders.NAME.value]

                    category_totals[name] = category_totals.get(
                        name, Decimal(0)
                    ) + Decimal(transaction[TablesHeaders.AMOUNT.value])

        return [
            {"category": key, "total": str(value)}
            for key, value in category_totals.items()
        ]

    async def dashboard(self) -> dict[str, Any]:
        """Returns net worth and current month summary."""
        now = datetime.now()

        net_worth = await self.account_service.calculate_net_worth()
        transactions = await self.transaction_service.get_all_transaction()
        category_cache = await self._build_category_cache()

        monthly_income = Decimal(0)
        monthly_expenses = Decimal(0)

        for transaction in transactions:
            if (
                transaction[TablesHeaders.DATE.value].year == now.year
                and transaction[TablesHeaders.DATE.value].month == now.month
            ):
                category = category_cache.get(
                    transaction[TablesHeaders.CATEGORY_ID.value]
                )

                if category is None:
                    raise ValueError("Missed Category")

                if category[TablesHeaders.TYPE.value] == INCOME:
                    monthly_income += Decimal(transaction[TablesHeaders.AMOUNT.value])
                else:
                    monthly_expenses += Decimal(transaction[TablesHeaders.AMOUNT.value])

        return {
            "net_worth": str(net_worth),
            "monthly_income": str(monthly_income),
            "monthly_expenses": str(monthly_expenses),
            "monthly_net_cash_flow": str(monthly_income - monthly_expenses),
        }

    async def _build_category_cache(self) -> dict[str, dict[str, Any]]:
        """Returns all categories ids."""
        categories = await self.category_service.get_all_categories()

        return {category[TablesHeaders.ID.value]: category for category in categories}
