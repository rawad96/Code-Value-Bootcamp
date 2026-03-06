from __future__ import annotations
from dataclasses import dataclass
from operator import index


@dataclass
class Income:
    description: str
    amount: float


@dataclass
class Expense:
    description: str
    amount: float


def remove_by_index(items: list, index: int) -> None:
    if index < 0 or index >= len(items):
        raise IndexError("Invalid index.")
    items.pop(index)


def remove_by_description(items: list, description: str) -> None:
    index_in_items = -1
    for index, item in enumerate(items):
        if item.description == description:
            index_in_items = index
            break
    if index_in_items == -1:
        raise IndexError("Invalid description.")
    items.pop(index_in_items)


class BudgetPlanner:
    def __init__(self) -> None:
        self._incomes: list[Income] = []
        self._expenses: list[Expense] = []

    def add_income(self, description: str, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self._incomes.append(Income(description, amount))

    def add_expense(self, description: str, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self._expenses.append(Expense(description, amount))

    def remove_income(self, index_or_description: int | str) -> None:
        if isinstance(index_or_description, int):
            remove_by_index(self._incomes, index_or_description)
        else:
            remove_by_description(self._incomes, index_or_description)

    def remove_expense(self, index_or_description: int | str) -> None:
        if isinstance(index_or_description, int):
            remove_by_index(self._expenses, index_or_description)
        else:
            remove_by_description(self._expenses, index_or_description)

    def clear_all(self) -> None:
        self._incomes.clear()
        self._expenses.clear()

    def get_remaining_budget(self) -> dict:
        total_income = sum(item.amount for item in self._incomes)
        total_expenses = sum(item.amount for item in self._expenses)
        remaining = total_income - total_expenses
        return {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "remaining_budget": remaining,
        }

    @property
    def incomes(self) -> list[Income]:
        return list(self._incomes)

    @property
    def expenses(self) -> list[Expense]:
        return list(self._expenses)
