from enum import Enum


class CSVHeaders(Enum):
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


csv_accessor_headers = [
    CSVHeaders.ID.value,
    CSVHeaders.NAME.value,
    CSVHeaders.OPENING_BALANCE.value,
    CSVHeaders.IS_DELETED.value,
]

account_headers = [
    CSVHeaders.ID.value,
    CSVHeaders.NAME.value,
    CSVHeaders.OPENING_BALANCE.value,
    CSVHeaders.IS_DELETED.value,
]

category_headers = [
    CSVHeaders.ID.value,
    CSVHeaders.NAME.value,
    CSVHeaders.TYPE.value,
    CSVHeaders.IS_DELETED.value,
]

transaction_headers = [
    CSVHeaders.ID.value,
    CSVHeaders.ACCOUNT_ID.value,
    CSVHeaders.CATEGORY_ID.value,
    CSVHeaders.AMOUNT.value,
    CSVHeaders.DATE.value,
    CSVHeaders.IS_DELETED.value,
]

transfer_headers = [
    CSVHeaders.ID.value,
    CSVHeaders.FROM_ACCOUNT_ID.value,
    CSVHeaders.TO_ACCOUNT_ID.value,
    CSVHeaders.AMOUNT.value,
    CSVHeaders.DATE.value,
    CSVHeaders.DESCRIPTION.value,
    CSVHeaders.IS_DELETED.value,
]

account_headers_request = [
    CSVHeaders.NAME.value,
    CSVHeaders.OPENING_BALANCE.value,
]

category_headers_request = [
    CSVHeaders.NAME.value,
    CSVHeaders.TYPE.value,
]

transaction_headers_request = [
    CSVHeaders.ACCOUNT_ID.value,
    CSVHeaders.CATEGORY_ID.value,
    CSVHeaders.AMOUNT.value,
]

transfer_headers_request = [
    CSVHeaders.FROM_ACCOUNT_ID.value,
    CSVHeaders.TO_ACCOUNT_ID.value,
    CSVHeaders.AMOUNT.value,
    CSVHeaders.DESCRIPTION.value,
]
