account_headers = ["id", "name", "opening_balance", "is_deleted"]

category_headers = ["id", "name", "type", "is_deleted"]

transaction_headers = [
    "id",
    "account_id",
    "category_id",
    "amount",
    "date",
    "is_deleted",
]

transfer_headers = [
    "id",
    "from_account_id",
    "to_account_id",
    "amount",
    "date",
    "description",
    "is_deleted",
]


account_headers_request = ["name", "opening_balance"]

category_headers_request = ["name", "type"]

transaction_headers_request = [
    "account_id",
    "category_id",
    "amount",
]

transfer_headers_request = [
    "from_account_id",
    "to_account_id",
    "amount",
    "description",
]
