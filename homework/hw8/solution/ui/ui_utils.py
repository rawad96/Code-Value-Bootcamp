from solution.api.api_client import get


def choose_from_list(items: list[dict], label_key: str) -> dict:
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
        except ValueError:
            pass

        print("Invalid choice")


def choose_account():
    accounts = get("/accounts/")
    account = choose_from_list(accounts, "name")

    if account:
        return {
            "account_id": account["id"],
            "opening_balance": account["opening_balance"],
        }


def choose_category():
    categories = get("/categories/")
    category = choose_from_list(categories, "name")

    if category:
        return category["id"]


def choose_transaction():
    transactions = get("/transactions/")

    for index, transaction in enumerate(transactions, start=1):
        print(
            f"{index}. amount:{transaction['amount']} "
            f"account:{transaction['account_id']} "
            f"category:{transaction['category_id']} "
            f"date:{transaction['date']}"
        )

    choice = int(input("Choose transaction: ")) - 1

    return transactions[choice]["id"]


def choose_transfer():
    transfers = get("/transfers/")

    for i, t in enumerate(transfers, start=1):
        print(f"{i}. {t['from_account_id']} -> {t['to_account_id']} | {t['amount']}")

    choice = int(input("Choose transfer: ")) - 1

    return transfers[choice]["id"]
