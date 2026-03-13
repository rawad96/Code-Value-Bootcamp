from solution.api.api_client import get, post, delete
from solution.ui.ui_utils import choose_account, choose_transfer


def view_transfers() -> None:
    transfers = get("/transfers/")

    for transfer in transfers:
        print(
            f"{transfer['from_account_id']} -> {transfer['to_account_id']} | "
            f"{transfer['amount']} | {transfer['description']}"
        )


def add_transfer() -> None:
    print("From account")
    from_account = choose_account()

    print("To account")
    to_account = choose_account()

    amount = input("Amount: ")
    description = input("Description: ")

    post(
        "/transfers/",
        {
            "from_account_id": from_account["account_id"],
            "to_account_id": to_account["account_id"],
            "amount": amount,
            "description": description,
        },
    )

    print("Transfer created")


def delete_transfer() -> None:
    transfer_id = choose_transfer()
    delete(f"/transfers/{transfer_id}")

    print("Transfer deleted")
