from solution.api.api_client import get


def monthly_summary() -> None:
    """Shows income, expenses and net flow for month."""
    month = int(input("Month: "))
    year = int(input("Year: "))

    summary = get(f"/reports/monthly_summary?year={year}&month={month}")

    print("\n-----Monthly Summary-----")
    print("Income:", summary["total_income"])
    print("Expenses:", summary["total_expenses"])
    print("Cash Flow:", summary["net_cash_flow"])


def category_breakdown() -> None:
    """Shows spending per category for month."""
    month = int(input("Month: "))
    year = int(input("Year: "))

    data = get(f"/reports/spending_by_category?year={year}&month={month}")

    print("\n-----Category Breakdown-----")
    for item in data:
        print(f"{item['category']} : {item['total']}")


def dashboard() -> None:
    """Shows net worth and current month summary."""
    dashboard = get("/reports/dashboard")

    print("\n-----Dashboard-----")
    print("Net Worth:", dashboard["net_worth"])
    print("Income:", dashboard["monthly_income"])
    print("Expenses:", dashboard["monthly_expenses"])
    print("Cash Flow:", dashboard["monthly_net_cash_flow"])
