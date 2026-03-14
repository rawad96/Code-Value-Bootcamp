from typing import Any, Optional
from decimal import Decimal
from datetime import datetime

from .account_service import AccountService
from .transaction_service import TransactionService
from .category_service import CategoryService
from constants.headers import CSVHeaders

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

    def monthly_summary(self, year: int, month: int) -> dict[str, Any]:
        """Returns income, expenses and net flow for month."""
        transactions = self.transaction_service.get_all_transaction()
        income = Decimal(0)
        expenses = Decimal(0)

        for transaction in transactions:
            if (
                transaction[CSVHeaders.DATE.value].year == year
                and transaction[CSVHeaders.DATE.value].month == month
            ):
                category = self.category_service.get_by_id(
                    transaction[CSVHeaders.CATEGORY_ID.value]
                )

                if category is None:
                    raise ValueError(f"Missed Category")

                if category[CSVHeaders.TYPE.value] == INCOME:
                    income += Decimal(transaction[CSVHeaders.AMOUNT.value])
                else:
                    expenses += Decimal(transaction[CSVHeaders.AMOUNT.value])

        net_flow = income - expenses
        return {
            "year": year,
            "month": month,
            "total_income": str(income),
            "total_expenses": str(expenses),
            "net_cash_flow": str(net_flow),
        }

    def spending_by_category(self, year: int, month: int) -> list[dict[str, Any]]:
        """Returns total per category for month."""
        transactions = self.transaction_service.get_all_transaction()
        category_totals: dict[str, Decimal] = {}

        for transaction in transactions:
            if (
                transaction[CSVHeaders.DATE.value].year == year
                and transaction[CSVHeaders.DATE.value].month == month
            ):
                category = self.category_service.get_by_id(
                    transaction[CSVHeaders.CATEGORY_ID.value]
                )

                if category is None:
                    raise ValueError(f"Missed Category")

                if category[CSVHeaders.TYPE.value] == EXPENSE:
                    category_totals[category[CSVHeaders.NAME.value]] = (
                        category_totals.get(category[CSVHeaders.NAME.value], Decimal(0))
                        + Decimal(transaction[CSVHeaders.AMOUNT.value])
                    )

        return [
            {"category": key, "total": str(value)}
            for key, value in category_totals.items()
        ]

    def dashboard(self) -> dict[str, Any]:
        """Returns net worth and current month summary."""
        now = datetime.now()
        net_worth = self.account_service.calculate_net_worth()

        transactions = self.transaction_service.get_all_transaction()
        monthly_income = Decimal(0)
        monthly_expenses = Decimal(0)

        for transaction in transactions:
            if (
                transaction[CSVHeaders.DATE.value].year == now.year
                and transaction[CSVHeaders.DATE.value].month == now.month
            ):
                category = self.category_service.get_by_id(
                    transaction[CSVHeaders.CATEGORY_ID.value]
                )

                if category is None:
                    raise ValueError(f"Missed Category")

                if category[CSVHeaders.TYPE.value] == INCOME:
                    monthly_income += Decimal(transaction[CSVHeaders.AMOUNT.value])
                else:
                    monthly_expenses += Decimal(transaction[CSVHeaders.AMOUNT.value])

        return {
            "net_worth": str(net_worth),
            "monthly_income": str(monthly_income),
            "monthly_expenses": str(monthly_expenses),
            "monthly_net_cash_flow": str(monthly_income - monthly_expenses),
        }
