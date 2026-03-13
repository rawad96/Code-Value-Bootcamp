from unittest.mock import Mock
from uuid import uuid4, UUID
from decimal import Decimal
from datetime import date
from typing import Any

import pytest

from constants.headers import CSVHeaders
from solution.services.transaction_service import TransactionService
from solution.models.transaction import Transaction


ACCOUNT_ID = CSVHeaders.ACCOUNT_ID.value
CATEGORY_ID = CSVHeaders.CATEGORY_ID.value
AMOUNT = CSVHeaders.AMOUNT.value
MESSAGE = "Message"


@pytest.fixture
def mock_repo() -> Mock:
    """Returns mock repo."""
    return Mock()


@pytest.fixture
def service(mock_repo: Mock) -> TransactionService:
    """Returns TransactionService with mock repo."""
    return TransactionService(repo=mock_repo)


def test_create_transaction(service: TransactionService, mock_repo: Mock) -> None:
    """Checks creat_trnsaction calls repo.create and returns message."""
    transaction_data: dict[str, Any] = {
        ACCOUNT_ID: uuid4(),
        CATEGORY_ID: uuid4(),
        AMOUNT: Decimal(1000),
    }

    result = service.creat_trnsaction(transaction_data)

    mock_repo.create.assert_called_once()

    assert result == {MESSAGE: "Trnsaction created"}


def test_get_all_transaction(service: TransactionService, mock_repo: Mock) -> None:
    """Checks get_all_transaction returns list of dicts."""
    transactions = [
        Transaction(
            id=uuid4(),
            account_id=uuid4(),
            category_id=uuid4(),
            amount=Decimal(200),
            date=date.today(),
            is_deleted="false",
        ),
        Transaction(
            id=uuid4(),
            account_id=uuid4(),
            category_id=uuid4(),
            amount=Decimal(50),
            date=date.today(),
            is_deleted="false",
        ),
    ]

    mock_repo.get_all.return_value = transactions

    result = service.get_all_transaction()

    mock_repo.get_all.assert_called_once()

    assert len(result) == 2
    assert result[0][AMOUNT] == Decimal(200)


def test_get_all_by_account(service: TransactionService, mock_repo: Mock) -> None:
    account_id: UUID = uuid4()

    transaction_one = Transaction(
        id=uuid4(),
        account_id=account_id,
        category_id=uuid4(),
        amount=Decimal(100),
        date=date.today(),
        is_deleted="false",
    )

    transaction_two = Transaction(
        id=uuid4(),
        account_id=account_id,
        category_id=uuid4(),
        amount=Decimal(50),
        date=date.today(),
        is_deleted="false",
    )

    transaction_three = Transaction(
        id=uuid4(),
        account_id=uuid4(),
        category_id=uuid4(),
        amount=Decimal(70),
        date=date.today(),
        is_deleted="false",
    )

    mock_repo.get_all.return_value = [
        transaction_one,
        transaction_two,
        transaction_three,
    ]

    result = service.get_all_by_account(account_id)

    assert len(result) == 2


def test_get_by_id(service: TransactionService, mock_repo: Mock) -> None:
    """Checks get_by_id returns transaction dict."""
    transaction_id: UUID = uuid4()

    transaction = Transaction(
        id=transaction_id,
        account_id=uuid4(),
        category_id=uuid4(),
        amount=Decimal(100),
        date=date.today(),
        is_deleted="false",
    )

    mock_repo.get.return_value = transaction

    result = service.get_by_id(transaction_id)

    mock_repo.get.assert_called_once_with(transaction_id)

    assert result["id"] == str(transaction_id)


def test_delete_transaction(service: TransactionService, mock_repo: Mock) -> None:
    """Checks delete_transaction calls repo.delete and returns message."""
    transaction_id: UUID = uuid4()

    result = service.delete_transaction(transaction_id)
    mock_repo.delete.assert_called_once_with(transaction_id)

    assert result == {MESSAGE: "Transaction deleted"}
