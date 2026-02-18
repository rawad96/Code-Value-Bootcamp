from budget_planner import BudgetPlanner
from budget_storage import BudgetStorage
from cli import BudgetCLI


def main() -> None:
    planner = BudgetPlanner()
    storage = BudgetStorage("./jsons/budget_data.json")

    cli = BudgetCLI(planner, storage)
    cli.run()


if __name__ == "__main__":
    main()
