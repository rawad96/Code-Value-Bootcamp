import pytest
from unittest.mock import Mock
from decimal import Decimal
from uuid import uuid4, UUID

from solution.models.account import Account
from solution.repository.account_repository import AccountRepository
from solution.repository.csv_accessor import CsvFileAccessor


@pytest.fixture
def mock_accessor():
    return Mock()


def test_account_repository_create(mock_accessor):
    repo = AccountRepository(accessor=mock_accessor)

    uuid_id = uuid4()
    account = Account(
        id=uuid_id, name="Main Account", opening_balance=Decimal("1000.50")
    )

    repo.create(account)

    assert mock_accessor.append_row.call_count == 1

    args = mock_accessor.append_row.call_args[0][0]

    assert args["id"] == str(uuid_id)
    assert args["name"] == "Main Account"
    assert args["opening_balance"] == "1000.50"


def test_account_repository_get_by_id(mock_accessor):
    uuid_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            "id": str(uuid_id),
            "name": "Main Account",
            "opening_balance": "1000.50",
        }
    ]

    repo = AccountRepository(accessor=mock_accessor)

    returned_account = repo.get(uuid_id)

    assert isinstance(returned_account, Account)
    assert returned_account.id == uuid_id


def test_account_repository_get_all(mock_accessor):
    uuid_id = uuid4()
    uuid_id_second = uuid4()

    mock_accessor.read_all.return_value = [
        {
            "id": str(uuid_id),
            "name": "Main Account",
            "opening_balance": "1000.50",
        },
        {
            "id": str(uuid_id_second),
            "name": "Second Account",
            "opening_balance": "200.00",
        },
    ]

    repo = AccountRepository(accessor=mock_accessor)

    returned_accounts = repo.get_all()

    assert all(isinstance(acc, Account) for acc in returned_accounts)


def test_account_repository_update(mock_accessor):
    uuid_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            "id": str(uuid_id),
            "name": "Main Account",
            "opening_balance": "1000.50",
        }
    ]

    repo = AccountRepository(accessor=mock_accessor)

    updated_account = Account(
        id=uuid_id, name="Main Account", opening_balance=Decimal("2000.00")
    )

    repo.update(updated_account)

    mock_accessor.write_all.assert_called_once()


def test_account_repository_delete(mock_accessor):
    uuid_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            "id": str(uuid_id),
            "name": "Main Account",
            "opening_balance": "1000.50",
        }
    ]

    repo = AccountRepository(accessor=mock_accessor)

    repo.delete(uuid_id)

    mock_accessor.write_all.assert_called_once()
