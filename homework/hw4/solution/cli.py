from budget_planner import BudgetPlanner
from budget_storage import BudgetStorage


class BudgetCLI:

    def __init__(self, planner: BudgetPlanner, storage: BudgetStorage) -> None:
        self._planner = planner
        self._storage = storage

    def run(self) -> None:
        self._storage.load(self._planner)

        while True:
            self._print_menu()
            choice = input("Choose an option: ")

            actions = {
                "1": self._handle_add_income,
                "2": self._handle_add_expense,
                "3": self._handle_summary,
                "4": self._handle_remove_income,
                "5": self._handle_remove_expense,
                "6": self._handle_clear,
            }

            try:
                if choice in actions:
                    action = actions[choice]
                    action()
                    continue
                elif choice == "7":
                    self._storage.save(self._planner)
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice.")
            except (ValueError, IndexError) as error:
                print(f"Error: {error}")

            self._storage.save(self._planner)

    def _print_menu(self) -> None:
        print("\n===== Budget Planner =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Remove Income")
        print("5. Remove Expense")
        print("6. Clear All Data")
        print("7. Exit\n")

    def _handle_add_income(self) -> None:
        desc = input("Enter income description: ")
        amount = float(input("Enter income amount: "))
        self._planner.add_income(desc, amount)
        print("Income added successfully!")

    def _handle_add_expense(self) -> None:
        desc = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        self._planner.add_expense(desc, amount)
        print("Expense added successfully!")

    def _handle_summary(self) -> None:
        print("\n--- Income Sources ---")
        for idx, income in enumerate(self._planner.incomes):
            print(f"{idx}. {income.description} - {income.amount}")

        print("\n--- Expenses ---")
        for idx, expense in enumerate(self._planner.expenses):
            print(f"{idx}. {expense.description} - {expense.amount}")

        summary = self._planner.get_remaining_budget()
        print("\n--- Totals ---")
        print(f"Total Income: {summary['total_income']}")
        print(f"Total Expenses: {summary['total_expenses']}")
        print(f"Remaining Budget: {summary['remaining_budget']}")

    def _handle_remove_income(self) -> None:
        index = int(input("Enter income index to remove: "))
        self._planner.remove_income(index)
        print("Income removed successfully!")

    def _handle_remove_expense(self) -> None:
        index = int(input("Enter expense index to remove: "))
        self._planner.remove_expense(index)
        print("Expense removed successfully!")

    def _handle_clear(self) -> None:
        self._planner.clear_all()
        print("All data cleared!")
