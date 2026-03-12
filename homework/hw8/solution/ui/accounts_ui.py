from solution.api.api_client import get, post, delete, put
from solution.ui.ui_utils import choose_account


def view_accounts():
    accounts = get("/accounts/")

    for account in accounts:
        print(f"\n{account['name']} | Opening balance: {account['opening_balance']}")


def add_account():
    name = input("Account name: ")
    balance = input("Opening balance: ")
    post("/accounts/", {"name": name, "opening_balance": balance})

    print("\nAccount created")


def edit_account():
    account = choose_account()
    new_name = input("New name: ")
    put(
        "/accounts/",
        {
            "id": account["account_id"],
            "name": new_name,
            "opening_balance": account["opening_balance"],
        },
    )

    print("\nAccount updated")


def delete_account():
    account = choose_account()
    delete(f"/accounts/{account["account_id"]}")

    print("\nAccount deleted")


def view_account_balance():
    account = choose_account()
    balance = get(f"\n/accounts/{account["account_id"]}/balance")

    print(f"Balance: {balance}")


def view_net_worth():
    net = get("/accounts/get/net/worth")

    print(f"\nNet Worth: {net}")
