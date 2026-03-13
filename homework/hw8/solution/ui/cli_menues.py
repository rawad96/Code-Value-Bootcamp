from solution.ui import accounts_ui
from solution.ui import categories_ui
from solution.ui import transactions_ui
from solution.ui import transfers_ui
from solution.ui import reports_ui
from solution.ui import data_portability_ui
from enum import IntEnum


class MenuOptions(IntEnum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6


BACK = "0 Back"
CHOOSE_OPTION = "Choose option: "
BREAK = "0"
INVALID_CHOICE = "Invalid choice"


def accounts_menu() -> None:

    actions = {
        MenuOptions.ONE: accounts_ui.view_accounts,
        MenuOptions.TWO: accounts_ui.add_account,
        MenuOptions.THREE: accounts_ui.edit_account,
        MenuOptions.FOUR: accounts_ui.delete_account,
        MenuOptions.FIVE: accounts_ui.view_account_balance,
        MenuOptions.SIX: accounts_ui.view_net_worth,
    }

    while True:

        print("\n--- Account Actions ---")
        print("1 View Accounts")
        print("2 Add Account")
        print("3 Edit Account")
        print("4 Delete Account")
        print("5 Account Balance")
        print("6 Net Worth")
        print(BACK)

        choice = input(CHOOSE_OPTION)

        if choice == BREAK:
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except Exception as error:
                print(error)
        else:
            print("Invalid choice")


def categories_menu() -> None:

    actions = {
        MenuOptions.ONE: categories_ui.view_categories,
        MenuOptions.TWO: categories_ui.add_category,
        MenuOptions.THREE: categories_ui.delete_category,
    }

    while True:

        print("\n--- Category Actions ---")
        print("1 View Categories")
        print("2 Add Category")
        print("3 Delete Category")
        print(BACK)

        choice = input(CHOOSE_OPTION)

        if choice == BREAK:
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except Exception as error:
                print(error)

        else:
            print(INVALID_CHOICE)


def transactions_menu() -> None:

    actions = {
        MenuOptions.ONE: transactions_ui.view_transactions,
        MenuOptions.TWO: transactions_ui.add_transaction,
        MenuOptions.THREE: transactions_ui.delete_transaction,
    }

    while True:

        print("\n--- Transaction Actions ---")
        print("1 View Transactions")
        print("2 Add Transaction")
        print("3 Delete Transaction")
        print(BACK)

        choice = input(CHOOSE_OPTION)

        if choice == BREAK:
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except Exception as error:
                print(error)

        else:
            print(INVALID_CHOICE)


def transfers_menu() -> None:

    actions = {
        MenuOptions.ONE: transfers_ui.view_transfers,
        MenuOptions.TWO: transfers_ui.add_transfer,
        MenuOptions.THREE: transfers_ui.delete_transfer,
    }

    while True:

        print("\n--- Transfer Actions ---")
        print("1 View Transfers")
        print("2 Add Transfer")
        print("3 Delete Transfer")
        print(BACK)

        choice = input(CHOOSE_OPTION)

        if choice == BREAK:
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except Exception as error:
                print(error)

        else:
            print(INVALID_CHOICE)


def reports_menu() -> None:

    actions = {
        MenuOptions.ONE: reports_ui.monthly_summary,
        MenuOptions.TWO: reports_ui.category_breakdown,
        MenuOptions.THREE: reports_ui.dashboard,
    }

    while True:

        print("\n--- Reports ---")
        print("1 Monthly Summary")
        print("2 Category Breakdown")
        print("3 Dashboard")
        print(BACK)

        choice = input(CHOOSE_OPTION)

        if choice == BREAK:
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except Exception as error:
                print(error)

        else:
            print(INVALID_CHOICE)


def data_portability_menu() -> None:
    actions = {
        MenuOptions.ONE: data_portability_ui.export_data,
        MenuOptions.TWO: data_portability_ui.import_data,
    }

    while True:
        print("\n--- Data Portability ---")
        print("1 Export all data")
        print("2 Import data from ZIP")
        print(BACK)

        choice = input(CHOOSE_OPTION)

        if choice == BREAK:
            break

        action = actions.get(choice)
        if action:
            try:
                action()
            except Exception as error:
                print(error)
        else:
            print(INVALID_CHOICE)
