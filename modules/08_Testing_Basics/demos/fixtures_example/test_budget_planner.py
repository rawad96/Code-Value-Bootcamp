import pytest
from budget_planner import BudgetPlanner


@pytest.fixture
def planner() -> BudgetPlanner:
    planner = BudgetPlanner()
    planner.add_income(1000, "Salary")
    planner.add_income(200, "Freelance")
    planner.add_income(300, "Investments")
    return planner


def test_number_of_incomes(planner):
    assert planner.number_of_incomes() == 3


def test_balance(planner):
    assert planner.get_balance() == 1500


def test_average_income_amount(planner):
    assert planner.average_income_amount() == 500
