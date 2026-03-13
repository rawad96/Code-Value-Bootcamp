from solution.api.api_client import get
from typing import Any

AMOUNT = "amount"
DATE = "date"
TYPE = "type"
CATEGORY_ID = "category_id"
ACCOUNT_ID = "account_id"
FROM_ACCOUNT_ID = "from_account_id"
TO_ACCOUNT_ID = "to_account_id"
INCOME = "income"
EXPENSE = "expense"
NAME = "name"
ID = "id"
OPENING_BALANCE = "opening_balance"


def choose_from_list(items: list[dict], label_key: str) -> dict | None:
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
    account = choose_from_list(accounts, NAME)

    if account:
        return {
            ACCOUNT_ID: account[ID],
            OPENING_BALANCE: account[OPENING_BALANCE],
        }
    return {}


def choose_category() -> str:
    categories = get("/categories/")
    category = choose_from_list(categories, NAME)

    if category:
        return category[ID]

    return ""


def choose_transaction() -> str:
    transactions = get("/transactions/")

    for index, transaction in enumerate(transactions, start=1):
        print(
            f"{index}. {AMOUNT}:{transaction[AMOUNT]} "
            f"{ACCOUNT_ID}:{transaction[ACCOUNT_ID]} "
            f"{CATEGORY_ID}:{transaction[CATEGORY_ID]} "
            f"{DATE}:{transaction[DATE]}"
        )

    choice = int(input("Choose transaction: ")) - 1

    return transactions[choice][ID]


def choose_transfer() -> str:
    transfers = get("/transfers/")

    for index, transfer in enumerate(transfers, start=1):
        print(
            f"{index}. {transfer[FROM_ACCOUNT_ID]} -> "
            f"{transfer[TO_ACCOUNT_ID]} | "
            f"{transfer[AMOUNT]}"
        )

    choice = int(input("Choose transfer: ")) - 1

    return transfers[choice][ID]
