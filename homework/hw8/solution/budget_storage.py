import json
from budget_planner import BudgetPlanner
from pathlib import Path

DESCRIPTION = "description"
AMOUNT = "amount"


class BudgetStorage:

    def __init__(self, file_path: str) -> None:
        self._file_path = Path(file_path)

    def save(self, planner: BudgetPlanner) -> None:
        data = {
            "incomes": [
                {DESCRIPTION: income.description, AMOUNT: income.amount}
                for income in planner.incomes
            ],
            "expenses": [
                {DESCRIPTION: expense.description, AMOUNT: expense.amount}
                for expense in planner.expenses
            ],
        }

        with self._file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load(self, planner: BudgetPlanner) -> None:
        if not self._file_path.exists():
            return

        with self._file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        planner.clear_all()

        for income in data.get("incomes", []):
            planner.add_income(income[DESCRIPTION], income[AMOUNT])

        for expense in data.get("expenses", []):
            planner.add_expense(expense[DESCRIPTION], expense[AMOUNT])
