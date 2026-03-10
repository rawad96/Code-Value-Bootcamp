import pytest
from unittest.mock import Mock
from uuid import uuid4
from datetime import date

from solution.models.transaction import Transaction

from solution.repository.transaction_repositort import TransactionRepository


@pytest.fixture
def mock_accessor():
    return Mock()


def test_creat_transaction(mock_accessor):
    transaction_repo = TransactionRepository(accessor=mock_accessor)

    account_uuid = uuid4()
    transaction_uuid = uuid4()
    category_uuid = uuid4()

    transaction = Transaction(
        id=transaction_uuid,
        account_id=account_uuid,
        category_id=category_uuid,
        amount=2000.00,
        date=date.today(),
    )

    transaction_repo.create(transaction)

    mock_accessor.append_row.assert_called_once()

    args = mock_accessor.append_row.call_args[0][0]

    assert args["id"] == str(transaction_uuid)
    assert args["account_id"] == str(account_uuid)
    assert args["category_id"] == str(category_uuid)
    assert args["amount"] == "2000.0"
    assert args["date"] == date.today().isoformat()


def test_transaction_get_by_id(mock_accessor):
    account_id = uuid4()
    transaction_id = uuid4()
    category_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            "id": str(transaction_id),
            "account_id": str(account_id),
            "category_id": str(category_id),
            "amount": "2000.0",
            "date": date.today().isoformat(),
        }
    ]

    repo = TransactionRepository(accessor=mock_accessor)

    returned_transaction = repo.get(transaction_id)

    assert isinstance(returned_transaction, Transaction)
    assert returned_transaction.id == transaction_id


def test_transaction_get_all(mock_accessor):
    account_id = uuid4()
    income_transaction_id = uuid4()
    income_category_id = uuid4()

    expense_transaction_id = uuid4()
    expense_category_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            "id": str(income_transaction_id),
            "account_id": str(account_id),
            "category_id": str(income_category_id),
            "amount": "2000.0",
            "date": date.today().isoformat(),
        },
        {
            "id": str(expense_transaction_id),
            "account_id": str(account_id),
            "category_id": str(expense_category_id),
            "amount": "2000.0",
            "date": date.today().isoformat(),
        },
    ]

    repo = TransactionRepository(accessor=mock_accessor)

    returned_transactions = repo.get_all()

    assert all(
        isinstance(transaction, Transaction) for transaction in returned_transactions
    )


def test_transaction_update(mock_accessor):
    account_id = uuid4()
    transaction_id = uuid4()
    category_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            "id": str(transaction_id),
            "account_id": str(account_id),
            "category_id": str(category_id),
            "amount": "2000.0",
            "date": date.today().isoformat(),
        }
    ]

    repo = TransactionRepository(accessor=mock_accessor)

    updated_transaction = Transaction(
        id=transaction_id,
        account_id=account_id,
        category_id=category_id,
        amount=1000.00,
        date=date.today(),
    )

    repo.update(updated_transaction)

    mock_accessor.write_all.assert_called_once()


def test_transaction_delete(mock_accessor):
    account_id = uuid4()
    transaction_id = uuid4()
    category_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            "id": str(transaction_id),
            "account_id": str(account_id),
            "category_id": str(category_id),
            "amount": "2000.0",
            "date": date.today().isoformat(),
        }
    ]

    repo = TransactionRepository(accessor=mock_accessor)

    repo.delete(transaction_id)

    mock_accessor.write_all.assert_called_once()
