from solution.ui.accounts_ui import *
from solution.ui.categories_ui import *
from solution.ui.transactions_ui import *
from solution.ui.transfers_ui import *
from solution.ui.reports_ui import *


class BudgetCLI:
    def run(self):
        while True:
            self.print_main_menu()
            choice = input("Choose option: ")

            if choice == "1":
                self.accounts_menu()

            elif choice == "2":
                self.categories_menu()

            elif choice == "3":
                self.transactions_menu()

            elif choice == "4":
                self.transfers_menu()

            elif choice == "5":
                self.reports_menu()

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid choice")

    def print_main_menu(self):
        print("\n===== Budget Planner =====")
        print("1 Account Actions")
        print("2 Category Actions")
        print("3 Transaction Actions")
        print("4 Transfer Actions")
        print("5 Reports")
        print("0 Exit")

    def accounts_menu(self):

        actions = {
            "1": view_accounts,
            "2": add_account,
            "3": edit_account,
            "4": delete_account,
            "5": view_account_balance,
            "6": view_net_worth,
        }

        while True:

            print("\n--- Account Actions ---")
            print("1 View Accounts")
            print("2 Add Account")
            print("3 Edit Account")
            print("4 Delete Account")
            print("5 Account Balance")
            print("6 Net Worth")
            print("0 Back")

            choice = input("Choose option: ")

            if choice == "0":
                break

            action = actions.get(choice)

            if action:
                try:
                    action()
                    print()
                except Exception as e:
                    print("Error:", e)

            else:
                print("Invalid choice")

    def categories_menu(self):

        actions = {"1": view_categories, "2": add_category, "3": delete_category}

        while True:

            print("\n--- Category Actions ---")
            print("1 View Categories")
            print("2 Add Category")
            print("3 Delete Category")
            print("0 Back")

            choice = input("Choose option: ")

            if choice == "0":
                break

            action = actions.get(choice)

            if action:
                try:
                    action()
                    print()
                except Exception as e:
                    print("Error:", e)

            else:
                print("Invalid choice")

    def transactions_menu(self):

        actions = {
            "1": view_transactions,
            "2": add_transaction,
            "3": delete_transaction,
        }

        while True:

            print("\n--- Transaction Actions ---")
            print("1 View Transactions")
            print("2 Add Transaction")
            print("3 Delete Transaction")
            print("0 Back")

            choice = input("Choose option: ")

            if choice == "0":
                break

            action = actions.get(choice)

            if action:
                try:
                    action()
                    print()
                except Exception as e:
                    print("Error:", e)

            else:
                print("Invalid choice")

    def transfers_menu(self):

        actions = {"1": view_transfers, "2": add_transfer, "3": delete_transfer}

        while True:

            print("\n--- Transfer Actions ---")
            print("1 View Transfers")
            print("2 Add Transfer")
            print("3 Delete Transfer")
            print("0 Back")

            choice = input("Choose option: ")

            if choice == "0":
                break

            action = actions.get(choice)

            if action:
                try:
                    action()
                    print()
                except Exception as e:
                    print("Error:", e)

            else:
                print("Invalid choice")

    def reports_menu(self):

        actions = {"1": monthly_summary, "2": category_breakdown, "3": dashboard}

        while True:

            print("\n--- Reports ---")
            print("1 Monthly Summary")
            print("2 Category Breakdown")
            print("3 Dashboard")
            print("0 Back")

            choice = input("Choose option: ")

            if choice == "0":
                break

            action = actions.get(choice)

            if action:
                try:
                    action()
                    print()
                except Exception as e:
                    print("Error:", e)

            else:
                print("Invalid choice")


if __name__ == "__main__":
    BudgetCLI().run()
