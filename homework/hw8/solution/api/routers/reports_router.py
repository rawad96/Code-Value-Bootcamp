from fastapi import APIRouter, HTTPException, status
from typing import Any

from solution.services.reports_service import ReportsService

router = APIRouter(prefix="/reports", tags=["Reports"])

service = ReportsService()


@router.get("/monthly_summary")
def monthly_summary(year: int, month: int) -> dict[str, Any]:
    """Returns income, expenses and net flow for month."""
    try:
        summary = service.monthly_summary(year, month)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error),
        )

    return summary


@router.get("/spending_by_category")
def spending_by_category(year: int, month: int) -> list[dict[str, Any]]:
    try:
        spending = service.spending_by_category(year, month)

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error),
        )

    return spending


@router.get("/dashboard")
def dashboard() -> dict[str, Any]:
    """Returns net worth and current month summary."""
    try:
        dashboard = service.dashboard()
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error),
        )
    return dashboard
