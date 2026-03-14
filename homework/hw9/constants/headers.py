from enum import Enum


class TablesHeaders(Enum):
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
    TablesHeaders.ID.value,
    TablesHeaders.NAME.value,
    TablesHeaders.OPENING_BALANCE.value,
    TablesHeaders.IS_DELETED.value,
]

account_headers = [
    TablesHeaders.ID.value,
    TablesHeaders.NAME.value,
    TablesHeaders.OPENING_BALANCE.value,
    TablesHeaders.IS_DELETED.value,
]

category_headers = [
    TablesHeaders.ID.value,
    TablesHeaders.NAME.value,
    TablesHeaders.TYPE.value,
    TablesHeaders.IS_DELETED.value,
]

transaction_headers = [
    TablesHeaders.ID.value,
    TablesHeaders.ACCOUNT_ID.value,
    TablesHeaders.CATEGORY_ID.value,
    TablesHeaders.AMOUNT.value,
    TablesHeaders.DATE.value,
    TablesHeaders.IS_DELETED.value,
]

transfer_headers = [
    TablesHeaders.ID.value,
    TablesHeaders.FROM_ACCOUNT_ID.value,
    TablesHeaders.TO_ACCOUNT_ID.value,
    TablesHeaders.AMOUNT.value,
    TablesHeaders.DATE.value,
    TablesHeaders.DESCRIPTION.value,
    TablesHeaders.IS_DELETED.value,
]

account_headers_request = [
    TablesHeaders.NAME.value,
    TablesHeaders.OPENING_BALANCE.value,
]

category_headers_request = [
    TablesHeaders.NAME.value,
    TablesHeaders.TYPE.value,
]

transaction_headers_request = [
    TablesHeaders.ACCOUNT_ID.value,
    TablesHeaders.CATEGORY_ID.value,
    TablesHeaders.AMOUNT.value,
]

transfer_headers_request = [
    TablesHeaders.FROM_ACCOUNT_ID.value,
    TablesHeaders.TO_ACCOUNT_ID.value,
    TablesHeaders.AMOUNT.value,
    TablesHeaders.DESCRIPTION.value,
]
