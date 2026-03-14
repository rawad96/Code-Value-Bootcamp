import pytest
from unittest.mock import Mock
from decimal import Decimal
from uuid import uuid4, UUID
from typing import Any

from solution.services.account_service import AccountService
from solution.models.account import Account
from solution.models.category import CategoryType

from constants.headers import CSVHeaders

MESSAGE = "Message"


@pytest.fixture
def mock_repo() -> Mock:
    """Returns mock repo."""
    return Mock()


@pytest.fixture
def mock_transaction_service() -> Mock:
    """Returns mock transaction service."""
    return Mock()


@pytest.fixture
def mock_category_service() -> Mock:
    """Returns mock category service."""
    return Mock()


@pytest.fixture
def service(
    mock_repo: Mock,
    mock_transaction_service: Mock,
    mock_category_service: Mock,
) -> AccountService:
    return AccountService(
        repo=mock_repo,
        transaction_service=mock_transaction_service,
        category_service=mock_category_service,
    )


def test_create_account(service: AccountService, mock_repo: Mock) -> None:
    """Checks create_account calls repo.create and returns message."""
    account_data: dict[str, Any] = {
        CSVHeaders.NAME.value: "Bank",
        CSVHeaders.OPENING_BALANCE.value: Decimal(1200),
    }

    result = service.create_account(account_data)

    mock_repo.create.assert_called_once()

    assert result == {MESSAGE: "Account created"}


def test_get_all_accounts(service: AccountService, mock_repo: Mock) -> None:
    """Checks get_all_accounts returns list of dicts."""
    accounts = [
        Account(
            id=uuid4(),
            name="bank1",
            opening_balance=Decimal(1000),
            is_deleted="false",
        ),
        Account(
            id=uuid4(),
            name="bank2",
            opening_balance=Decimal(2000),
            is_deleted="false",
        ),
    ]

    mock_repo.get_all.return_value = accounts

    result = service.get_all_accounts()

    mock_repo.get_all.assert_called_once()

    assert len(result) == 2
    assert result[0][CSVHeaders.NAME.value] == "bank1"


def test_get_by_id(service: AccountService, mock_repo: Mock) -> None:
    """Checks get_by_id returns account dict."""
    account_id: UUID = uuid4()

    account = Account(
        id=account_id,
        name="Bank",
        opening_balance=Decimal(1000),
        is_deleted="false",
    )

    mock_repo.get.return_value = account

    result = service.get_by_id(account_id)

    mock_repo.get.assert_called_once_with(account_id)

    assert result[CSVHeaders.ID.value] == str(account_id)


def test_update_account(service: AccountService, mock_repo: Mock) -> None:
    """Checks update_account calls repo.update and returns dict."""
    account_id = uuid4()

    account_data: dict[str, Any] = {
        CSVHeaders.ID.value: account_id,
        CSVHeaders.NAME.value: "Bank",
        CSVHeaders.OPENING_BALANCE.value: Decimal(1000),
    }

    updated_account = Account(
        id=account_id,
        name="Bank",
        opening_balance=Decimal(1000),
        is_deleted="false",
    )

    mock_repo.update.return_value = updated_account

    result = service.update_account(account_data)

    mock_repo.update.assert_called_once()

    assert result[CSVHeaders.ID.value] == str(account_id)


def test_delete_account(service: AccountService, mock_repo: Mock) -> None:
    account_id = uuid4()

    result = service.delete_account(account_id)
    mock_repo.delete.assert_called_once_with(account_id)

    assert result == {MESSAGE: "Account deleted"}


def test_calculate_balance(
    service: AccountService,
    mock_repo: Mock,
    mock_transaction_service: Mock,
    mock_category_service: Mock,
) -> None:
    """Checks calculate_balance adds income and subtracts expenses."""
    account_id = uuid4()

    account = Account(
        id=account_id,
        name="Bank",
        opening_balance=Decimal(1000),
        is_deleted="false",
    )

    mock_repo.get.return_value = account

    transactions = [
        {CSVHeaders.AMOUNT.value: "50", CSVHeaders.CATEGORY_ID.value: uuid4()},
        {CSVHeaders.AMOUNT.value: "20", CSVHeaders.CATEGORY_ID.value: uuid4()},
    ]

    mock_transaction_service.get_all_by_account.return_value = transactions

    mock_category_service.get_by_id.side_effect = [
        {CSVHeaders.TYPE.value: CategoryType.INCOME.value},
        {CSVHeaders.TYPE.value: CategoryType.EXPENSE.value},
    ]

    result = service.calculate_balance(account_id)

    assert result == Decimal(1030)


def test_calculate_net_worth(service: AccountService, mock_repo: Mock) -> None:
    """Checks calculate_net_worth sums balance of all accounts."""
    first_account_id = uuid4()
    second_account_id = uuid4()

    first_account = Account(
        id=first_account_id,
        name="Bank",
        opening_balance=Decimal(1000),
        is_deleted="false",
    )

    second_account = Account(
        id=second_account_id,
        name="Cash",
        opening_balance=Decimal(500),
        is_deleted="false",
    )

    mock_repo.get_all.return_value = [first_account, second_account]

    service.calculate_balance = Mock(side_effect=[Decimal(1500), Decimal(400)])

    result = service.calculate_net_worth()

    assert result == Decimal(1900)
