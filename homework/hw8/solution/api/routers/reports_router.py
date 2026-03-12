from fastapi import APIRouter, HTTPException, status
from decimal import Decimal
from typing import Any

from solution.services.account_service import AccountService
from solution.services.transaction_service import TransactionService
from solution.services.category_service import CategoryService
from solution.services.transfer_service import TransferService

router = APIRouter(prefix="/reports", tags=["Reports"])

account_service = AccountService()
transaction_service = TransactionService()
category_service = CategoryService()
transfer_service = TransferService()


# --- Helper functions ---
def transaction_to_dict(transaction: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": str(transaction["id"]),
        "account_id": str(transaction["account_id"]),
        "category_id": str(transaction["category_id"]),
        "amount": str(transaction["amount"]),
        "date": transaction["date"],
    }


def account_to_dict(account: Any) -> dict[str, Any]:
    return {
        "id": str(account["id"]),
        "name": account["name"],
        "opening_balance": str(account["opening_balance"]),
        "is_deleted": account["is_deleted"],
    }


@router.get("/monthly-summary/{year}/{month}")
def monthly_summary(year: int, month: int) -> dict[str, Any]:
    """
    Return monthly summary: total income, total expenses, net cash flow
    """
    try:
        transactions = transaction_service.get_all_transaction()
        income = Decimal(0)
        expenses = Decimal(0)
        for t in transactions:
            if t.date.year == year and t.date.month == month:
                category = category_service.get_by_id(t.category_id)
                if category.type == "income":
                    income += Decimal(t.amount)
                else:
                    expenses += Decimal(t.amount)
        net_flow = income - expenses
        return {
            "year": year,
            "month": month,
            "total_income": str(income),
            "total_expenses": str(expenses),
            "net_cash_flow": str(net_flow),
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to calculate monthly summary: {e}",
        )


@router.get("/spending-by-category/{year}/{month}")
def spending_by_category(year: int, month: int) -> List[dict[str, Any]]:
    """
    Return spending breakdown by category for a given month
    """
    try:
        transactions = transaction_service.get_all_transaction()
        category_totals: dict[str, Decimal] = {}

        for t in transactions:
            if t.date.year == year and t.date.month == month:
                category = category_service.get_by_id(t.category_id)
                if category.type == "expense":
                    category_totals[category.name] = category_totals.get(
                        category.name, Decimal(0)
                    ) + Decimal(t.amount)

        result = [{"category": k, "total": str(v)} for k, v in category_totals.items()]
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to calculate spending by category: {e}",
        )


@router.get("/dashboard")
def dashboard() -> dict[str, Any]:
    """
    Return overall dashboard: net worth, this month's income, expenses, net cash flow
    """
    from datetime import datetime

    now = datetime.now()
    try:
        net_worth = account_service.calculate_net_worth()

        transactions = transaction_service.get_all_transaction()
        monthly_income = Decimal(0)
        monthly_expenses = Decimal(0)
        for t in transactions:
            if t.date.year == now.year and t.date.month == now.month:
                category = category_service.get_by_id(t.category_id)
                if category.type == "income":
                    monthly_income += Decimal(t.amount)
                else:
                    monthly_expenses += Decimal(t.amount)

        net_cash_flow = monthly_income - monthly_expenses

        return {
            "net_worth": str(net_worth),
            "monthly_income": str(monthly_income),
            "monthly_expenses": str(monthly_expenses),
            "monthly_net_cash_flow": str(net_cash_flow),
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate dashboard: {e}",
        )
