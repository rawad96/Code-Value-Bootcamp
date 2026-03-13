from solution.ui import accounts_ui
from solution.ui import categories_ui
from solution.ui import transactions_ui
from solution.ui import transfers_ui
from solution.ui import reports_ui
from solution.ui import data_portability_ui
from solution.ui import cli_menues


class BudgetCLI:
    def __init__(self):
        self.accounts_menu = accounts_ui.accounts_menu
        self.categories_menu = categories_ui.categories_menu
        self.transactions_menu = transactions_ui.transactions_menu
        self.transfers_menu = transfers_ui.transfers_menu
        self.reports_menu = reports_ui.reports_menu
        self.data_portability_menu = data_portability_ui.data_portability_menu

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

            elif choice == "6":
                self.data_portability_menu()

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
        print("6 Data Portability (Import/Export)")
        print("0 Exit")


if __name__ == "__main__":
    BudgetCLI().run()
