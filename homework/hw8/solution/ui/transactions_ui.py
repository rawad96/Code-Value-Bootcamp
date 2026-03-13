from solution.api.api_client import get, post, delete
from solution.ui.ui_utils import choose_account, choose_category, choose_transaction


def view_transactions() -> None:
    transactions = get("/transactions/")

    for transaction in transactions:
        print(
            f"{transaction['amount']} | "
            f"account:{transaction['account_id']} | "
            f"category:{transaction['category_id']} | "
            f"{transaction['date']}"
        )


def add_transaction() -> None:
    print("Choose account")
    account = choose_account()

    print("Choose category")
    category_id = choose_category()

    amount = input("Amount: ")

    post(
        "/transactions/",
        {
            "account_id": account["account_id"],
            "category_id": category_id,
            "amount": amount,
        },
    )

    print("Transaction added")


def delete_transaction() -> None:
    transaction_id = choose_transaction()
    delete(f"/transactions/{transaction_id}")

    print("Transaction deleted")
