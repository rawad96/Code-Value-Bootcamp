from solution.api.api_client import get, post, delete
from solution.ui.ui_utils import choose_account, choose_category, choose_transaction


def view_transactions() -> None:
    """Shows all transactions."""
    transactions = get("/transactions/")

    print("\n-----All Transactions-----")
    for transaction in transactions:
        print(
            f"{transaction['amount']} | "
            f"account:{transaction['account_id']} | "
            f"category:{transaction['category_id']} | "
            f"{transaction['date']}"
        )


def add_transaction() -> None:
    print("\nChoose account")
    account = choose_account()

    print("\nChoose category")
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

    print("\nTransaction added")


def delete_transaction() -> None:
    """Deletes transaction."""
    transaction_id = choose_transaction()
    delete(f"/transactions/{transaction_id}")

    print("\nTransaction deleted")
