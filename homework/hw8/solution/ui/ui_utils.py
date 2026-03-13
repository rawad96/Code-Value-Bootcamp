from solution.api.api_client import get
from typing import Any

from constants.headers import CSVHeaders

INCOME = "income"
EXPENSE = "expense"


def choose_from_list(items: list[dict], label_key: str) -> dict | None:
    """Lets user pick one item from list, returns it or None."""
    if not items:
        print("No items available")
        return None

    for index, item in enumerate(items, start=1):
        print(f"{index}. {item[label_key]}")

    while True:
        try:
            choice = int(input("Choose: "))
            if 1 <= choice <= len(items):
                return items[choice - 1]
        except ValueError as error:
            print(error)

        print("Invalid choice")


def choose_account() -> dict:
    accounts = get("/accounts/")
    account = choose_from_list(accounts, CSVHeaders.NAME.value)

    if account:
        return {
            CSVHeaders.ACCOUNT_ID.value: account[CSVHeaders.ID.value],
            CSVHeaders.OPENING_BALANCE.value: account[CSVHeaders.OPENING_BALANCE.value],
        }
    return {}


def choose_category() -> str:
    """Lets user pick category, returns id."""
    categories = get("/categories/")
    category = choose_from_list(categories, CSVHeaders.NAME.value)

    if category:
        return category[CSVHeaders.ID.value]

    return ""


def choose_transaction() -> str:
    transactions = get("/transactions/")

    for index, transaction in enumerate(transactions, start=1):
        print(
            f"{index}. {CSVHeaders.AMOUNT.value}:{transaction[CSVHeaders.AMOUNT.value]} "
            f"{CSVHeaders.ACCOUNT_ID.value}:{transaction[CSVHeaders.ACCOUNT_ID.value]} "
            f"{CSVHeaders.CATEGORY_ID.value}:{transaction[CSVHeaders.CATEGORY_ID.value]} "
            f"{CSVHeaders.DATE.value}:{transaction[CSVHeaders.DATE.value]}"
        )

    choice = int(input("Choose transaction: ")) - 1

    return transactions[choice][CSVHeaders.ID.value]


def choose_transfer() -> str:
    """Lets user pick transfer, returns id."""
    transfers = get("/transfers/")

    for index, transfer in enumerate(transfers, start=1):
        print(
            f"{index}. {transfer[CSVHeaders.FROM_ACCOUNT_ID.value]} -> "
            f"{transfer[CSVHeaders.TO_ACCOUNT_ID.value]} | "
            f"{transfer[CSVHeaders.AMOUNT.value]}"
        )

    choice = int(input("Choose transfer: ")) - 1

    return transfers[choice][CSVHeaders.ID.value]
