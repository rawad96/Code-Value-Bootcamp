from solution.ui import cli_menues
from solution.ui.menu_options import MenuOptions
from typing import Any

BACK = "0 Back"
CHOOSE_OPTION = "Choose option: "
BREAK = "0"
INVALID_CHOICE = "Invalid choice"


class BudgetCLI:
    def __init__(self) -> None:
        """Sets up menu actions."""
        self.accounts_menu = cli_menues.accounts_menu
        self.categories_menu = cli_menues.categories_menu
        self.transactions_menu = cli_menues.transactions_menu
        self.transfers_menu = cli_menues.transfers_menu
        self.reports_menu = cli_menues.reports_menu
        self.data_portability_menu = cli_menues.data_portability_menu

    def run(self) -> None:
        """Runs main menu loop."""
        while True:
            self.print_main_menu()
            try:
                choice = MenuOptions(int(input(CHOOSE_OPTION)))
            except ValueError:
                print(INVALID_CHOICE)

            if choice == MenuOptions.ZERO:
                print("Goodbye!")
                break

            action = self.get_action(choice)
            if action is None:
                print("Invalid choice")

    def print_main_menu(self) -> None:
        """Prints main menu options."""
        print("\n===== Budget Planner =====")
        print("1 Account Actions")
        print("2 Category Actions")
        print("3 Transaction Actions")
        print("4 Transfer Actions")
        print("5 Reports")
        print("6 Data Portability (Import/Export)")
        print("0 Exit")

    def get_action(self, choice: str) -> Any:
        """Returns menu action for choice or None."""
        actions = {
            MenuOptions.ONE: self.accounts_menu,
            MenuOptions.TWO: self.categories_menu,
            MenuOptions.THREE: self.transactions_menu,
            MenuOptions.FOUR: self.transfers_menu,
            MenuOptions.FIVE: self.reports_menu,
            MenuOptions.SIX: self.data_portability_menu,
        }

        action = actions.get(choice)

        if action:
            return action()

        return None


if __name__ == "__main__":
    BudgetCLI().run()
