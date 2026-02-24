import requests
import responses

BASE_URL = "http://localhost:8000"

TOTAL_INCOME = 5000.0
TOTAL_EXPENSES = 500.0
REMAINING_BUDGET = 4500.0


@responses.activate
def test_add_income_api() -> None:
    responses.add(
        responses.POST,
        f"{BASE_URL}/add_income",
        json={"message": "Income added successfully."},
        status=200,
    )
    response = requests.post(
        f"{BASE_URL}/add_income",
        json={"description": "Salary", "amount": 5000.0},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Income added successfully."}


@responses.activate
def test_add_expense_api() -> None:
    responses.add(
        responses.POST,
        f"{BASE_URL}/add_expense",
        json={"message": "Expense added successfully."},
        status=200,
    )
    response = requests.post(
        f"{BASE_URL}/add_expense",
        json={"description": "Food", "amount": 1500.0},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Expense added successfully."}


@responses.activate
def test_get_summary_api() -> None:
    responses.add(
        responses.GET,
        f"{BASE_URL}/summary",
        json={
            "incomes": [{"description": "Salary", "amount": 5000.0}],
            "expenses": [{"description": "Food", "amount": 500.0}],
            "total_income": 5000.0,
            "total_expenses": 500.0,
            "remaining_budget": 4500.0,
        },
        status=200,
    )
    response = requests.get(f"{BASE_URL}/summary")
    assert response.status_code == 200
    data = response.json()
    assert data["total_income"] == TOTAL_INCOME
    assert data["total_expenses"] == TOTAL_EXPENSES
    assert data["remaining_budget"] == REMAINING_BUDGET


@responses.activate
def test_delete_income_api() -> None:
    responses.add(
        responses.DELETE,
        f"{BASE_URL}/delete_income",
        json={"message": "Income removed successfully."},
        status=200,
    )
    response = requests.delete(
        f"{BASE_URL}/delete_income",
        json={"index_or_description": 0},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Income removed successfully."}


@responses.activate
def test_delete_expense_api() -> None:
    responses.add(
        responses.DELETE,
        f"{BASE_URL}/delete_expense",
        json={"message": "Expense removed successfully."},
        status=200,
    )
    response = requests.delete(
        f"{BASE_URL}/delete_expense",
        json={"index_or_description": "Food"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Expense removed successfully."}


@responses.activate
def test_clear_all_api() -> None:
    responses.add(
        responses.POST,
        f"{BASE_URL}/clear",
        json={"message": "All data cleared successfully."},
        status=200,
    )
    response = requests.post(f"{BASE_URL}/clear")
    assert response.status_code == 200
    assert response.json() == {"message": "All data cleared successfully."}
