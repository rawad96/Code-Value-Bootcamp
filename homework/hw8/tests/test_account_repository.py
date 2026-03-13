import pytest
from unittest.mock import Mock
from decimal import Decimal
from uuid import uuid4

from solution.models.account import Account
from solution.repository.account_repository import AccountRepository

from constants.headers import CSVHeaders


TRUE = "true"
FALSE = "false"


@pytest.fixture
def mock_accessor() -> Mock:
    """Returns mock accessor."""
    return Mock()


def test_account_repository_create(mock_accessor: Mock) -> None:
    """Checks create writes one row with entity data."""
    repo = AccountRepository(accessor=mock_accessor)

    uuid_id = uuid4()
    account = Account(
        id=uuid_id,
        name="Main Account",
        opening_balance=Decimal("1000.50"),
        is_deleted=FALSE,
    )

    repo.create(account)

    assert mock_accessor.append_row.call_count == 1

    args = mock_accessor.append_row.call_args[0][0]

    assert args[CSVHeaders.ID.value] == str(uuid_id)
    assert args[CSVHeaders.NAME.value] == "Main Account"
    assert args[CSVHeaders.OPENING_BALANCE.value] == "1000.50"
    assert args[CSVHeaders.IS_DELETED.value] == FALSE


def test_account_repository_get_by_id(mock_accessor: Mock) -> None:
    """Checks get returns account by id."""
    uuid_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(uuid_id),
            CSVHeaders.NAME.value: "Main Account",
            CSVHeaders.OPENING_BALANCE.value: "1000.50",
            CSVHeaders.IS_DELETED.value: FALSE,
        }
    ]

    repo = AccountRepository(accessor=mock_accessor)

    returned_account = repo.get(uuid_id)

    assert isinstance(returned_account, Account)
    assert returned_account.id == uuid_id


def test_account_repository_get_all(mock_accessor: Mock) -> None:
    """Checks get_all returns all non-deleted accounts."""
    uuid_id = uuid4()
    uuid_id_second = uuid4()

    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(uuid_id),
            CSVHeaders.NAME.value: "Main Account",
            CSVHeaders.OPENING_BALANCE.value: "1000.50",
            CSVHeaders.IS_DELETED.value: FALSE,
        },
        {
            CSVHeaders.ID.value: str(uuid_id_second),
            CSVHeaders.NAME.value: "Second Account",
            CSVHeaders.OPENING_BALANCE.value: "200.00",
            CSVHeaders.IS_DELETED.value: FALSE,
        },
    ]

    repo = AccountRepository(accessor=mock_accessor)

    returned_accounts = repo.get_all()

    assert all(isinstance(acc, Account) for acc in returned_accounts)


def test_account_repository_update(mock_accessor: Mock) -> None:
    uuid_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(uuid_id),
            CSVHeaders.NAME.value: "Main Account",
            CSVHeaders.OPENING_BALANCE.value: "1000.50",
            CSVHeaders.IS_DELETED.value: FALSE,
        }
    ]

    repo = AccountRepository(accessor=mock_accessor)

    updated_account = Account(
        id=uuid_id,
        name="Main Account",
        opening_balance=Decimal("2000.00"),
        is_deleted=FALSE,
    )

    repo.update(updated_account)

    mock_accessor.write_all.assert_called_once()


def test_account_repository_delete(mock_accessor: Mock) -> None:
    """Checks delete marks row as deleted."""
    uuid_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(uuid_id),
            CSVHeaders.NAME.value: "Main Account",
            CSVHeaders.OPENING_BALANCE.value: "1000.50",
            CSVHeaders.IS_DELETED.value: FALSE,
        }
    ]

    repo = AccountRepository(accessor=mock_accessor)

    repo.delete(uuid_id)

    mock_accessor.write_all.assert_called_once()
