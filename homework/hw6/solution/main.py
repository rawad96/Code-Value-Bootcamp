from budget_planner import BudgetPlanner
from budget_storage import BudgetStorage
from cli import BudgetCLI
from budget_planner_api import app, load_data
import uvicorn


def main() -> None:
    cli = BudgetCLI()
    # load_data()
    cli.run()
    # uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
