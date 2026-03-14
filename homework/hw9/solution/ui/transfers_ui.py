from solution.api.api_client import get, post, delete
from solution.ui.ui_utils import choose_account, choose_transfer


def view_transfers() -> None:
    """Shows all transfers."""
    transfers = get("/transfers/")

    print("\n-----All Transfers-----")
    for transfer in transfers:
        print(
            f"{transfer['from_account_id']} -> {transfer['to_account_id']} | "
            f"{transfer['amount']} | {transfer['description']}"
        )


def add_transfer() -> None:
    print("\nFrom account")
    from_account = choose_account()

    print("\nTo account")
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

    print("\nTransfer created")


def delete_transfer() -> None:
    """Deletes transfer."""
    transfer_id = choose_transfer()
    delete(f"/transfers/{transfer_id}")

    print("\nTransfer deleted")
