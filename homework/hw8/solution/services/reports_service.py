from typing import Any, Optional
from decimal import Decimal
from datetime import datetime

from .account_service import AccountService
from .transaction_service import TransactionService
from .category_service import CategoryService

AMOUNT = "amount"
DATE = "date"
TYPE = "type"
CATEGORY_ID = "category_id"
INCOME = "income"
EXPENSE = "expense"
NAME = "name"


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
        transactions = self.transaction_service.get_all_transaction()
        income = Decimal(0)
        expenses = Decimal(0)

        for transaction in transactions:
            if transaction[DATE].year == year and transaction[DATE].month == month:
                category = self.category_service.get_by_id(transaction[CATEGORY_ID])
                if category[TYPE] == INCOME:
                    income += Decimal(transaction[AMOUNT])
                else:
                    expenses += Decimal(transaction[AMOUNT])

        net_flow = income - expenses
        return {
            "year": year,
            "month": month,
            "total_income": str(income),
            "total_expenses": str(expenses),
            "net_cash_flow": str(net_flow),
        }

    def spending_by_category(self, year: int, month: int) -> list[dict[str, Any]]:
        transactions = self.transaction_service.get_all_transaction()
        category_totals: dict[str, Decimal] = {}

        for transaction in transactions:
            if transaction[DATE].year == year and transaction[DATE].month == month:
                category = self.category_service.get_by_id(transaction[CATEGORY_ID])
                if category[TYPE] == EXPENSE:
                    category_totals[category[NAME]] = category_totals.get(
                        category[NAME], Decimal(0)
                    ) + Decimal(transaction[AMOUNT])

        return [
            {"category": key, "total": str(value)}
            for key, value in category_totals.items()
        ]

    def dashboard(self) -> dict[str, Any]:
        now = datetime.now()
        net_worth = self.account_service.calculate_net_worth()

        transactions = self.transaction_service.get_all_transaction()
        monthly_income = Decimal(0)
        monthly_expenses = Decimal(0)

        for transaction in transactions:
            if (
                transaction[DATE].year == now.year
                and transaction[DATE].month == now.month
            ):
                category = self.category_service.get_by_id(transaction[CATEGORY_ID])
                if category[TYPE] == INCOME:
                    monthly_income += Decimal(transaction[AMOUNT])
                else:
                    monthly_expenses += Decimal(transaction[AMOUNT])

        return {
            "net_worth": str(net_worth),
            "monthly_income": str(monthly_income),
            "monthly_expenses": str(monthly_expenses),
            "monthly_net_cash_flow": str(monthly_income - monthly_expenses),
        }
