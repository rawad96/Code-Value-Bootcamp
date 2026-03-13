from enum import IntEnum


class MenuOptions(IntEnum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6


class AccountOptions(IntEnum):
    VIEW_ACCOUNTS = 1
    ADD_ACCOUNT = 2
    EDIT_ACCOUNT = 3
    DELETE_ACCOUNT = 4
    VIEW_ACCOUNT_BALANCE = 5
    VIEW_NET_WORTH = 6


class CategoryOptions(IntEnum):
    VIEW_CATEGORIES = 1
    ADD_CATEGORY = 2
    DELETE_CATEGORY = 3


class TransactionOptions(IntEnum):
    VIEW_TRANSACTIONS = 1
    ADD_TRANSACTION = 2
    DELETE_TRANSACTION = 3


class TransferOptions(IntEnum):
    VIEW_TRANSFERS = 1
    ADD_TRANSFER = 2
    DELETE_TRANSFER = 3


class ReportOptions(IntEnum):
    MONTHLY_SUMMARY = 1
    CATEGORY_BREAKDOWN = 2
    DASHBOARD = 3


class DataPortabilityOptions(IntEnum):
    EXPORT_DATA = 1
    IMPORT_DATA = 2
