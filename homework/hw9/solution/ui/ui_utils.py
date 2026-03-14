from solution.api.api_client import get
from typing import Any

from constants.headers import TablesHeaders

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
        except ValueError as error:
            print(error)
        else:
            if 1 <= choice <= len(items):
                return items[choice - 1]

        print("Invalid choice")


def choose_account() -> dict:
    accounts = get("/accounts/")
    account = choose_from_list(accounts, TablesHeaders.NAME.value)

    if account:
        return {
            TablesHeaders.ACCOUNT_ID.value: account[TablesHeaders.ID.value],
            TablesHeaders.OPENING_BALANCE.value: account[
                TablesHeaders.OPENING_BALANCE.value
            ],
        }
    return {}


def choose_category() -> str:
    """Lets user pick category, returns id."""
    categories = get("/categories/")
    category = choose_from_list(categories, TablesHeaders.NAME.value)

    if category:
        return category[TablesHeaders.ID.value]

    return ""


def choose_transaction() -> str:
    transactions = get("/transactions/")

    for index, transaction in enumerate(transactions, start=1):
        amount = transaction[TablesHeaders.AMOUNT.value]
        account_id = transaction[TablesHeaders.ACCOUNT_ID.value]
        category_id = transaction[TablesHeaders.CATEGORY_ID.value]
        date = transaction[TablesHeaders.DATE.value]
        print(
            f"{index}. amount:{amount} "
            f"account_id:{account_id} "
            f"category_id:{category_id} "
            f"date:{date}"
        )

    choice = int(input("Choose transaction: ")) - 1

    return transactions[choice][TablesHeaders.ID.value]


def choose_transfer() -> str:
    """Lets user pick transfer, returns id."""
    transfers = get("/transfers/")

    for index, transfer in enumerate(transfers, start=1):
        from_account_id = transfer[TablesHeaders.FROM_ACCOUNT_ID.value]
        to_account_id = transfer[TablesHeaders.TO_ACCOUNT_ID.value]
        amount = transfer[TablesHeaders.AMOUNT.value]
        print(f"{index}. {from_account_id} -> " f"{to_account_id} | " f"{amount}")

    choice = int(input("Choose transfer: ")) - 1

    return transfers[choice][TablesHeaders.ID.value]
