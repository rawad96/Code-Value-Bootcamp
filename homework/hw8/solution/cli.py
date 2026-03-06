from budget_planner import BudgetPlanner
from budget_storage import BudgetStorage
import requests

BUDGET_PLANNER_URL = "http://localhost:8000"


class BudgetCLI:

    def run(self) -> None:

        while True:
            self._print_menu()
            choice = input("Choose an option: ")

            actions: dict = {
                "1": self._handle_add_income,
                "2": self._handle_add_expense,
                "3": self._handle_summary,
                "4": self._handle_remove_income,
                "5": self._handle_remove_expense,
                "6": self._handle_clear,
            }
            action = actions.get(choice)
            if action is None:
                if choice == "7":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice.")
                    continue
            action()

            # try:
            #     if choice in actions:
            #         action()
            #         continue
            #     elif choice == "7":
            #         # self._storage.save(self._planner)
            #         print("Goodbye!")
            #         break
            #     else:
            #         print("Invalid choice.")
            # except (ValueError, IndexError) as error:
            #     print(f"Error: {error}")

            # self._storage.save(self._planner)

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
        try:
            response = requests.post(
                f"{BUDGET_PLANNER_URL}/add_income",
                json={"description": desc, "amount": amount},
            )
            response.raise_for_status()
            print("Income added successfully!")
        except requests.RequestException as error:
            print(f"Failed to add income: {error}")

    def _handle_add_expense(self) -> None:
        desc = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        try:
            response = requests.post(
                f"{BUDGET_PLANNER_URL}/add_expense",
                json={"description": desc, "amount": amount},
            )
            response.raise_for_status()
            print("Expense added successfully!")
        except requests.RequestException as error:
            print(f"Failed to add expense: {error}")

    def _handle_summary(self) -> None:
        print("\n--- Income Sources ---")
        try:
            response = requests.get(f"{BUDGET_PLANNER_URL}/summary")
            response.raise_for_status()
        except requests.RequestException as error:
            print(f"Failed to retrieve summary: {error}")
        summary = response.json()
        for idx, income in enumerate(summary["incomes"]):
            print(f"{idx}. {income['description']} - {income['amount']}")

        print("\n--- Expenses ---")
        for idx, expense in enumerate(summary["expenses"]):
            print(f"{idx}. {expense['description']} - {expense['amount']}")

        print("\n--- Totals ---")
        print(f"Total Income: {summary['total_income']}")
        print(f"Total Expenses: {summary['total_expenses']}")
        print(f"Remaining Budget: {summary['remaining_budget']}")

    def _handle_remove_income(self) -> None:
        index_or_description = input("Enter income index or description to remove: ")
        try:
            response = requests.delete(
                f"{BUDGET_PLANNER_URL}/delete_income",
                json={"index_or_description": index_or_description},
            )
            response.raise_for_status()
            print("Income removed successfully!")
        except requests.RequestException as error:
            print(f"Failed to remove income: {error}")

    def _handle_remove_expense(self) -> None:
        index_or_description = input("Enter expense index or description to remove: ")
        try:
            response = requests.delete(
                f"{BUDGET_PLANNER_URL}/delete_expense",
                json={"index_or_description": index_or_description},
            )
            response.raise_for_status()
            print("Expense removed successfully!")
        except requests.RequestException as error:
            print(f"Failed to remove expense: {error}")

    def _handle_clear(self) -> None:
        try:
            response = requests.post(f"{BUDGET_PLANNER_URL}/clear")
            response.raise_for_status()
            print("All data cleared!")
        except requests.RequestException as error:
            print(f"Failed to clear data: {error}")
