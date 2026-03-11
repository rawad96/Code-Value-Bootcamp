from solution.services.transaction_service import TransactionService
from solution.models.transaction import Transaction
from unittest.mock import Mock
from uuid import uuid4
from decimal import Decimal


def test_create_transaction():
    mock_repo = Mock()
    service = TransactionService(repo=mock_repo)

    transaction = Transaction(
        id=str(uuid4()),
        account_id=str(uuid4()),
        category_id=str(uuid4()),
        amount=Decimal(1000),
        date="2024-01-01",
    )

    result = service.creat_trnsaction(transaction)

    mock_repo.create.assert_called_once()
    assert result == {"Message": "Trnsaction created"}


def test_get_all_transaction():
    mock_repo = Mock()
    service = TransactionService(repo=mock_repo)

    transactions = [
        Transaction(
            id=str(uuid4()),
            account_id=str(uuid4()),
            category_id=str(uuid4()),
            amount=Decimal(200),
            date="2024-01-01",
        ),
        Transaction(
            id=str(uuid4()),
            account_id=str(uuid4()),
            category_id=str(uuid4()),
            amount=Decimal(50),
            date="2024-01-02",
        ),
    ]

    mock_repo.get_all.return_value = transactions

    result = service.get_all_transaction()

    mock_repo.get_all.assert_called_once()
    assert result == transactions


def test_get_all_by_account():
    mock_repo = Mock()
    service = TransactionService(repo=mock_repo)

    account_one_id = str(uuid4())
    transaction_one = Transaction(
        id=str(uuid4()),
        account_id=account_one_id,
        category_id=str(uuid4()),
        amount=Decimal(100),
        date="2024-01-01",
    )
    transaction_two = Transaction(
        id=str(uuid4()),
        account_id=account_one_id,
        category_id=str(uuid4()),
        amount=Decimal(50),
        date="2024-01-02",
    )
    transaction_three = Transaction(
        id=str(uuid4()),
        account_id=str(uuid4()),
        category_id=str(uuid4()),
        amount=Decimal(70),
        date="2024-01-03",
    )

    mock_repo.get_all.return_value = [
        transaction_one,
        transaction_two,
        transaction_three,
    ]

    result = service.get_all_by_account(account_one_id)

    assert result == [transaction_one, transaction_two]


def test_get_by_id():
    mock_repo = Mock()
    service = TransactionService(repo=mock_repo)

    transaction_one_id = str(uuid4())
    transaction = Transaction(
        id=transaction_one_id,
        account_id=str(uuid4()),
        category_id="10",
        amount=Decimal(100),
        date="2024-01-01",
    )

    mock_repo.get.return_value = transaction

    result = service.get_by_id(transaction_one_id)

    mock_repo.get.assert_called_once_with(transaction_one_id)
    assert result == transaction


def test_delete_transaction():
    mock_repo = Mock()
    service = TransactionService(repo=mock_repo)

    transaction_one_id = str(uuid4())
    result = service.delete_transaction(transaction_one_id)

    mock_repo.delete.assert_called_once_with(transaction_one_id)
    assert result == {"Message": "Transaction deleted"}
