ID = "id"
NAME = "name"
AMOUNT = "amount"
IS_DELETED = "is_deleted"
OPENING_BALANCE = "opening_balance"
ACCOUNT_ID = "account_id"
TYPE = "type"
FROM_ACCOUNT_ID = "from_account_id"
TO_ACCOUNT_ID = "to_account_id"
DATE = "date"
DESCRIPTION = "description"
CATEGORY_ID = "category_id"

account_headers = [ID, NAME, OPENING_BALANCE, IS_DELETED]

category_headers = [ID, NAME, TYPE, IS_DELETED]

transaction_headers = [
    ID,
    ACCOUNT_ID,
    CATEGORY_ID,
    AMOUNT,
    DATE,
    IS_DELETED,
]

transfer_headers = [
    ID,
    FROM_ACCOUNT_ID,
    TO_ACCOUNT_ID,
    AMOUNT,
    DATE,
    DESCRIPTION,
    IS_DELETED,
]


account_headers_request = [NAME, OPENING_BALANCE]

category_headers_request = [NAME, TYPE]

transaction_headers_request = [
    ACCOUNT_ID,
    CATEGORY_ID,
    AMOUNT,
]

transfer_headers_request = [
    FROM_ACCOUNT_ID,
    TO_ACCOUNT_ID,
    AMOUNT,
    DESCRIPTION,
]
