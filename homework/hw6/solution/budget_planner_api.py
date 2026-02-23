from fastapi import FastAPI
import uvicorn
from budget_planner import BudgetPlanner
from budget_storage import BudgetStorage
from budget_planner_schema import IncomeOrExpense, RemoveItem


app = FastAPI()
planner = BudgetPlanner()
storage = BudgetStorage("budget_data.json")

MESSAGE = "message"
ERROR = "error"


def load_data() -> None:
    storage.load(planner)


@app.get("/summary")
async def get_remaining_budget() -> dict | tuple[dict, int]:
    try:
        incomes = planner.incomes
        expenses = planner.expenses
        remaining_budget = planner.get_remaining_budget()
        summary = {
            "incomes": [
                {"description": income.description, "amount": income.amount}
                for income in incomes
            ],
            "expenses": [
                {"description": expense.description, "amount": expense.amount}
                for expense in expenses
            ],
            "total_income": remaining_budget["total_income"],
            "total_expenses": remaining_budget["total_expenses"],
            "remaining_budget": remaining_budget["remaining_budget"],
        }
        return summary
    except Exception:
        return {ERROR: "Failed to retrieve incomes."}, 500


@app.post("/add_income")
async def add_income(income: IncomeOrExpense) -> dict | tuple[dict, int]:
    try:
        planner.add_income(income.description, income.amount)
        storage.save(planner)
        return {MESSAGE: "Income added successfully."}
    except ValueError:
        return {ERROR: "Invalid income amount."}, 400


@app.post("/add_expense")
async def add_expense(expense: IncomeOrExpense) -> dict | tuple[dict, int]:
    try:
        planner.add_expense(expense.description, expense.amount)
        storage.save(planner)
        return {MESSAGE: "Expense added successfully."}
    except ValueError:
        return {ERROR: "Invalid expense amount."}, 400


@app.delete("/delete_income")
async def remove_income(remove_item: RemoveItem) -> dict | tuple[dict, int]:
    try:
        planner.remove_income(remove_item.index_or_description)
        storage.save(planner)
        return {MESSAGE: "Income removed successfully."}
    except IndexError:
        return {ERROR: "Invalid income index or description."}, 400


@app.delete("/delete_expense")
async def remove_expense(remove_item: RemoveItem) -> dict | tuple[dict, int]:
    try:
        planner.remove_expense(remove_item.index_or_description)
        storage.save(planner)
        return {MESSAGE: "Expense removed successfully."}
    except IndexError:
        return {ERROR: "Invalid expense index or description."}, 400


@app.post("/clear")
async def clear_all() -> dict | tuple[dict, int]:
    planner.clear_all()
    storage.save(planner)
    return {MESSAGE: "All data cleared successfully."}


PORT = 8000

if __name__ == "__main__":
    load_data()
    uvicorn.run(app, host="127.0.0.1", port=PORT)
