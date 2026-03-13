from solution.ui import accounts_ui
from solution.ui import categories_ui
from solution.ui import transactions_ui
from solution.ui import transfers_ui
from solution.ui import reports_ui
from solution.ui import data_portability_ui
from solution.ui.menu_options import (
    MenuOptions,
    AccountOptions,
    CategoryOptions,
    DataPortabilityOptions,
    ReportOptions,
    TransactionOptions,
    TransferOptions,
)


BACK = "0 Back"
CHOOSE_OPTION = "Choose option: "
BREAK = "0"
INVALID_CHOICE = "Invalid choice"


def print_invalid_choice() -> None:
    print(INVALID_CHOICE)


def accounts_menu() -> None:
    """Runs account actions menu loop."""
    actions = {
        AccountOptions.VIEW_ACCOUNTS: accounts_ui.view_accounts,
        AccountOptions.ADD_ACCOUNT: accounts_ui.add_account,
        AccountOptions.EDIT_ACCOUNT: accounts_ui.edit_account,
        AccountOptions.DELETE_ACCOUNT: accounts_ui.delete_account,
        AccountOptions.VIEW_ACCOUNT_BALANCE: accounts_ui.view_account_balance,
        AccountOptions.VIEW_NET_WORTH: accounts_ui.view_net_worth,
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

        try:
            menu_choice = MenuOptions(int(input(CHOOSE_OPTION)))
        except ValueError:
            print_invalid_choice()

        if menu_choice == MenuOptions.ZERO:
            break

        try:
            choice = AccountOptions(menu_choice)
        except ValueError:
            print_invalid_choice()
            continue

        action = actions.get(choice)

        if action:
            try:
                action()
            except Exception as error:
                print(error)
        else:
            print_invalid_choice()


def categories_menu() -> None:
    actions = {
        CategoryOptions.VIEW_CATEGORIES: categories_ui.view_categories,
        CategoryOptions.ADD_CATEGORY: categories_ui.add_category,
        CategoryOptions.DELETE_CATEGORY: categories_ui.delete_category,
    }

    while True:
        print("\n--- Category Actions ---")
        print("1 View Categories")
        print("2 Add Category")
        print("3 Delete Category")
        print(BACK)

        try:
            menu_choice = MenuOptions(int(input(CHOOSE_OPTION)))
        except ValueError:
            print_invalid_choice()

        if menu_choice == MenuOptions.ZERO:
            break

        try:
            choice = CategoryOptions(menu_choice)
        except ValueError:
            print_invalid_choice()
            continue

        action = actions.get(choice)

        if action:
            try:
                action()
            except Exception as error:
                print(error)

        else:
            print_invalid_choice()


def transactions_menu() -> None:
    """Runs transaction actions menu loop."""
    actions = {
        TransactionOptions.VIEW_TRANSACTIONS: transactions_ui.view_transactions,
        TransactionOptions.ADD_TRANSACTION: transactions_ui.add_transaction,
        TransactionOptions.DELETE_TRANSACTION: transactions_ui.delete_transaction,
    }

    while True:
        print("\n--- Transaction Actions ---")
        print("1 View Transactions")
        print("2 Add Transaction")
        print("3 Delete Transaction")
        print(BACK)

        try:
            menu_choice = MenuOptions(int(input(CHOOSE_OPTION)))
        except ValueError:
            print_invalid_choice()

        if menu_choice == MenuOptions.ZERO:
            break

        try:
            choice = TransactionOptions(menu_choice)
        except ValueError:
            print_invalid_choice()
            continue

        action = actions.get(choice)

        if action:
            try:
                action()
            except Exception as error:
                print(error)

        else:
            print_invalid_choice()


def transfers_menu() -> None:
    """Runs transfer actions menu loop."""
    actions = {
        TransferOptions.VIEW_TRANSFERS: transfers_ui.view_transfers,
        TransferOptions.ADD_TRANSFER: transfers_ui.add_transfer,
        TransferOptions.DELETE_TRANSFER: transfers_ui.delete_transfer,
    }

    while True:
        print("\n--- Transfer Actions ---")
        print("1 View Transfers")
        print("2 Add Transfer")
        print("3 Delete Transfer")
        print(BACK)

        try:
            menu_choice = MenuOptions(int(input(CHOOSE_OPTION)))
        except ValueError:
            print_invalid_choice()

        if menu_choice == MenuOptions.ZERO:
            break

        try:
            choice = TransferOptions(menu_choice)
        except ValueError:
            print_invalid_choice()
            continue

        action = actions.get(choice)

        if action:
            try:
                action()
            except Exception as error:
                print(error)

        else:
            print_invalid_choice()


def reports_menu() -> None:
    """Runs reports menu loop."""
    actions = {
        ReportOptions.MONTHLY_SUMMARY: reports_ui.monthly_summary,
        ReportOptions.CATEGORY_BREAKDOWN: reports_ui.category_breakdown,
        ReportOptions.DASHBOARD: reports_ui.dashboard,
    }

    while True:
        print("\n--- Reports ---")
        print("1 Monthly Summary")
        print("2 Category Breakdown")
        print("3 Dashboard")
        print(BACK)

        try:
            menu_choice = MenuOptions(int(input(CHOOSE_OPTION)))
        except ValueError:
            print_invalid_choice()

        if menu_choice == MenuOptions.ZERO:
            break

        try:
            choice = ReportOptions(menu_choice)
        except ValueError:
            print_invalid_choice()
            continue

        action = actions.get(choice)

        if action:
            try:
                action()
            except Exception as error:
                print(error)

        else:
            print_invalid_choice()


def data_portability_menu() -> None:
    """Runs import/export menu loop."""
    actions = {
        DataPortabilityOptions.EXPORT_DATA: data_portability_ui.export_data,
        DataPortabilityOptions.IMPORT_DATA: data_portability_ui.import_data,
    }

    while True:
        print("\n--- Data Portability ---")
        print("1 Export all data")
        print("2 Import data from ZIP")
        print(BACK)

        try:
            menu_choice = MenuOptions(int(input(CHOOSE_OPTION)))
        except ValueError:
            print_invalid_choice()

        if menu_choice == MenuOptions.ZERO:
            break

        try:
            choice = DataPortabilityOptions(menu_choice)
        except ValueError:
            print_invalid_choice()
            continue

        action = actions.get(choice)
        if action:
            try:
                action()
            except Exception as error:
                print(error)
        else:
            print_invalid_choice()
