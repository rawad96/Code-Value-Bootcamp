from solution.api.api_client import get


def monthly_summary() -> None:
    month = int(input("Month: "))
    year = int(input("Year: "))

    summary = get(f"/reports/monthly_summary?year={year}&month={month}")

    print("Income:", summary["total_income"])
    print("Expenses:", summary["total_expenses"])
    print("Cash Flow:", summary["net_cash_flow"])


def category_breakdown() -> None:
    month = int(input("Month: "))
    year = int(input("Year: "))

    data = get(f"/reports/spending_by_category?year={year}&month={month}")

    for item in data:
        print(f"{item['category']} : {item['total']}")


def dashboard() -> None:
    dashboard = get("/reports/dashboard")

    print("Net Worth:", dashboard["net_worth"])
    print("Income:", dashboard["monthly_income"])
    print("Expenses:", dashboard["monthly_expenses"])
    print("Cash Flow:", dashboard["monthly_net_cash_flow"])
