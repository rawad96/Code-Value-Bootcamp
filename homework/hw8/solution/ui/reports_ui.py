from solution.api.api_client import get


def monthly_summary():

    month = input("Month: ")
    year = input("Year: ")

    summary = get(f"/reports/monthly_summary?month={month}&year={year}")

    print("Income:", summary["total_income"])
    print("Expenses:", summary["total_expenses"])
    print("Cash Flow:", summary["net_cash_flow"])


def category_breakdown():

    month = input("Month: ")
    year = input("Year: ")

    data = get(f"/reports/category_breakdown?month={month}&year={year}")

    for item in data:
        print(f"{item['category']} : {item['amount']}")


def dashboard():

    dash = get("/dashboard")

    print("Net Worth:", dash["net_worth"])
    print("Income:", dash["income"])
    print("Expenses:", dash["expenses"])
    print("Cash Flow:", dash["cash_flow"])
