import pytest
from unittest.mock import Mock
from uuid import uuid4
from datetime import date
from decimal import Decimal

from constants.headers import CSVHeaders
from solution.models.transaction import Transaction
from solution.repository.transaction_repository import TransactionRepository


TRUE = "true"
FALSE = "false"


@pytest.fixture
def mock_accessor() -> Mock:
    """Returns mock accessor."""
    return Mock()


def test_create_transaction(mock_accessor: Mock) -> None:
    """Checks create writes one row with entity data."""
    transaction_repo = TransactionRepository(accessor=mock_accessor)

    account_uuid = uuid4()
    transaction_uuid = uuid4()
    category_uuid = uuid4()

    transaction = Transaction(
        id=transaction_uuid,
        account_id=account_uuid,
        category_id=category_uuid,
        amount=Decimal("2000.00"),
        date=date.today(),
        is_deleted=FALSE,
    )

    transaction_repo.create(transaction)

    mock_accessor.append_row.assert_called_once()

    args = mock_accessor.append_row.call_args[0][0]

    assert args[CSVHeaders.ID.value] == str(transaction_uuid)
    assert args[CSVHeaders.ACCOUNT_ID.value] == str(account_uuid)
    assert args[CSVHeaders.CATEGORY_ID.value] == str(category_uuid)
    assert args[CSVHeaders.AMOUNT.value] == "2000.00"
    assert args[CSVHeaders.DATE.value] == date.today().isoformat()
    assert args[CSVHeaders.IS_DELETED.value] == FALSE


def test_transaction_get_by_id(mock_accessor: Mock) -> None:
    account_id = uuid4()
    transaction_id = uuid4()
    category_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(transaction_id),
            CSVHeaders.ACCOUNT_ID.value: str(account_id),
            CSVHeaders.CATEGORY_ID.value: str(category_id),
            CSVHeaders.AMOUNT.value: "2000.00",
            CSVHeaders.DATE.value: date.today().isoformat(),
            CSVHeaders.IS_DELETED.value: FALSE,
        }
    ]

    repo = TransactionRepository(accessor=mock_accessor)

    returned_transaction = repo.get(transaction_id)

    assert isinstance(returned_transaction, Transaction)
    assert returned_transaction.id == transaction_id


def test_transaction_get_all(mock_accessor: Mock) -> None:
    """Checks get_all returns all non-deleted transactions."""
    account_id = uuid4()

    income_transaction_id = uuid4()
    income_category_id = uuid4()

    expense_transaction_id = uuid4()
    expense_category_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(income_transaction_id),
            CSVHeaders.ACCOUNT_ID.value: str(account_id),
            CSVHeaders.CATEGORY_ID.value: str(income_category_id),
            CSVHeaders.AMOUNT.value: "2000.00",
            CSVHeaders.DATE.value: date.today().isoformat(),
            CSVHeaders.IS_DELETED.value: FALSE,
        },
        {
            CSVHeaders.ID.value: str(expense_transaction_id),
            CSVHeaders.ACCOUNT_ID.value: str(account_id),
            CSVHeaders.CATEGORY_ID.value: str(expense_category_id),
            CSVHeaders.AMOUNT.value: "1500.00",
            CSVHeaders.DATE.value: date.today().isoformat(),
            CSVHeaders.IS_DELETED.value: FALSE,
        },
    ]

    repo = TransactionRepository(accessor=mock_accessor)

    returned_transactions = repo.get_all()

    assert all(
        isinstance(transaction, Transaction) for transaction in returned_transactions
    )


def test_transaction_update(mock_accessor: Mock) -> None:
    """Checks update writes new row for same id."""
    account_id = uuid4()
    transaction_id = uuid4()
    category_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(transaction_id),
            CSVHeaders.ACCOUNT_ID.value: str(account_id),
            CSVHeaders.CATEGORY_ID.value: str(category_id),
            CSVHeaders.AMOUNT.value: "2000.00",
            CSVHeaders.DATE.value: date.today().isoformat(),
            CSVHeaders.IS_DELETED.value: FALSE,
        }
    ]

    repo = TransactionRepository(accessor=mock_accessor)

    updated_transaction = Transaction(
        id=transaction_id,
        account_id=account_id,
        category_id=category_id,
        amount=Decimal("1000.00"),
        date=date.today(),
        is_deleted=FALSE,
    )

    repo.update(updated_transaction)

    mock_accessor.write_all.assert_called_once()


def test_transaction_delete(mock_accessor: Mock) -> None:
    """Checks delete marks row as deleted."""
    account_id = uuid4()
    transaction_id = uuid4()
    category_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(transaction_id),
            CSVHeaders.ACCOUNT_ID.value: str(account_id),
            CSVHeaders.CATEGORY_ID.value: str(category_id),
            CSVHeaders.AMOUNT.value: "2000.00",
            CSVHeaders.DATE.value: date.today().isoformat(),
            CSVHeaders.IS_DELETED.value: FALSE,
        }
    ]

    repo = TransactionRepository(accessor=mock_accessor)

    repo.delete(transaction_id)

    mock_accessor.write_all.assert_called_once()
