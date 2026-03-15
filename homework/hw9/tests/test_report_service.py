from solution.services.reports_service import ReportsService
from constants.headers import TablesHeaders
from unittest.mock import AsyncMock
import pytest
from datetime import datetime


INCOME = "income"
EXPENSE = "expense"


@pytest.mark.asyncio
async def test_monthly_summary(reports_service: ReportsService) -> None:
    year = 2024
    month = 1

    transactions = [
        {
            TablesHeaders.AMOUNT.value: 500,
            TablesHeaders.CATEGORY_ID.value: "1",
            TablesHeaders.DATE.value: datetime(2024, 1, 10),
        },
        {
            TablesHeaders.AMOUNT.value: 200,
            TablesHeaders.CATEGORY_ID.value: "2",
            TablesHeaders.DATE.value: datetime(2024, 1, 15),
        },
    ]

    category_cache = {
        "1": {TablesHeaders.TYPE.value: INCOME},
        "2": {TablesHeaders.TYPE.value: EXPENSE},
    }

    reports_service.transaction_service.get_all_transaction = AsyncMock(
        return_value=transactions
    )
    reports_service._build_category_cache = AsyncMock(return_value=category_cache)

    result = await reports_service.monthly_summary(year, month)

    assert result["total_income"] == "500"
    assert result["total_expenses"] == "200"
    assert result["net_cash_flow"] == "300"
