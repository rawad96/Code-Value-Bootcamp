import pytest
from solution.budget_planner import BudgetPlanner

SALARY = 3000.0
RENT = 1200.0


def test_add_income() -> None:
    planner = BudgetPlanner()
    planner.add_income("Salary", SALARY)
    assert len(planner.incomes) == 1
    assert planner.incomes[0].description == "Salary"
    assert planner.incomes[0].amount == SALARY


def test_add_expense() -> None:
    planner = BudgetPlanner()
    planner.add_expense("Rent", RENT)
    assert len(planner.expenses) == 1
    assert planner.expenses[0].description == "Rent"
    assert planner.expenses[0].amount == RENT


def test_get_remaining_budget() -> None:
    planner = BudgetPlanner()
    planner.add_income("Salary", SALARY)
    planner.add_expense("Rent", RENT)

    summary = planner.get_remaining_budget()
    assert summary["total_income"] == SALARY
    assert summary["total_expenses"] == RENT
    assert summary["remaining_budget"] == (SALARY - RENT)


def test_remove_income() -> None:
    planner = BudgetPlanner()
    planner.add_income("Salary", SALARY)
    planner.remove_income(0)
    assert len(planner.incomes) == 0


def test_remove_expense() -> None:
    planner = BudgetPlanner()
    planner.add_expense("Rent", RENT)
    planner.remove_expense(0)
    assert len(planner.expenses) == 0


def test_clear_all() -> None:
    planner = BudgetPlanner()
    planner.add_income("Salary", SALARY)
    planner.add_expense("Rent", RENT)
    planner.clear_all()
    assert len(planner.incomes) == 0
    assert len(planner.expenses) == 0
