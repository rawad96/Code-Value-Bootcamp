from uuid import uuid4
from datetime import date
from decimal import Decimal
from unittest.mock import Mock

import pytest

from constants.headers import CSVHeaders
from solution.models.transfer import Transfer
from solution.repository.transfer_repository import TransferRepository


TRUE = "true"
FALSE = "false"


@pytest.fixture
def mock_accessor() -> Mock:
    """Returns mock accessor."""
    return Mock()


def test_create_transfer(mock_accessor: Mock) -> None:
    """Checks create writes one row with entity data."""
    transfer_repo = TransferRepository(accessor=mock_accessor)

    transfer_id = uuid4()
    from_account_id = uuid4()
    to_account_id = uuid4()

    transfer = Transfer(
        id=transfer_id,
        from_account_id=from_account_id,
        to_account_id=to_account_id,
        amount=Decimal("2000.00"),
        date=date.today(),
        description="Food",
        is_deleted=FALSE,
    )

    transfer_repo.create(transfer)

    mock_accessor.append_row.assert_called_once()

    args = mock_accessor.append_row.call_args[0][0]

    assert args[CSVHeaders.ID.value] == str(transfer_id)
    assert args[CSVHeaders.FROM_ACCOUNT_ID.value] == str(from_account_id)
    assert args[CSVHeaders.TO_ACCOUNT_ID.value] == str(to_account_id)
    assert args[CSVHeaders.AMOUNT.value] == "2000.00"
    assert args[CSVHeaders.DATE.value] == date.today().isoformat()
    assert args[CSVHeaders.DESCRIPTION.value] == "Food"
    assert args[CSVHeaders.IS_DELETED.value] == FALSE


def test_transfer_get_by_id(mock_accessor: Mock) -> None:
    transfer_id = uuid4()
    from_account_id = uuid4()
    to_account_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(transfer_id),
            CSVHeaders.FROM_ACCOUNT_ID.value: str(from_account_id),
            CSVHeaders.TO_ACCOUNT_ID.value: str(to_account_id),
            CSVHeaders.AMOUNT.value: "2000.00",
            CSVHeaders.DATE.value: date.today().isoformat(),
            CSVHeaders.DESCRIPTION.value: "Food",
            CSVHeaders.IS_DELETED.value: FALSE,
        }
    ]

    repo = TransferRepository(accessor=mock_accessor)

    returned_transfer = repo.get(transfer_id)

    assert isinstance(returned_transfer, Transfer)
    assert returned_transfer.id == transfer_id


def test_transfer_get_all(mock_accessor: Mock) -> None:
    """Checks get_all returns all non-deleted transfers."""
    transfer_id1 = uuid4()
    transfer_id2 = uuid4()

    from_account_id = uuid4()
    to_account_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(transfer_id1),
            CSVHeaders.FROM_ACCOUNT_ID.value: str(from_account_id),
            CSVHeaders.TO_ACCOUNT_ID.value: str(to_account_id),
            CSVHeaders.AMOUNT.value: "2000.00",
            CSVHeaders.DATE.value: date.today().isoformat(),
            CSVHeaders.DESCRIPTION.value: "Food",
            CSVHeaders.IS_DELETED.value: FALSE,
        },
        {
            CSVHeaders.ID.value: str(transfer_id2),
            CSVHeaders.FROM_ACCOUNT_ID.value: str(from_account_id),
            CSVHeaders.TO_ACCOUNT_ID.value: str(to_account_id),
            CSVHeaders.AMOUNT.value: "1000.00",
            CSVHeaders.DATE.value: date.today().isoformat(),
            CSVHeaders.DESCRIPTION.value: "shopping",
            CSVHeaders.IS_DELETED.value: FALSE,
        },
    ]

    repo = TransferRepository(accessor=mock_accessor)

    returned_transfers = repo.get_all()

    assert len(returned_transfers) == 2
    assert all(isinstance(transfer, Transfer) for transfer in returned_transfers)


def test_transfer_update(mock_accessor: Mock) -> None:
    transfer_id = uuid4()
    from_account_id = uuid4()
    to_account_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(transfer_id),
            CSVHeaders.FROM_ACCOUNT_ID.value: str(from_account_id),
            CSVHeaders.TO_ACCOUNT_ID.value: str(to_account_id),
            CSVHeaders.AMOUNT.value: "2000.00",
            CSVHeaders.DATE.value: date.today().isoformat(),
            CSVHeaders.DESCRIPTION.value: "Food",
            CSVHeaders.IS_DELETED.value: FALSE,
        }
    ]

    repo = TransferRepository(accessor=mock_accessor)

    updated_transfer = Transfer(
        id=transfer_id,
        from_account_id=from_account_id,
        to_account_id=to_account_id,
        amount=Decimal("1000.00"),
        date=date.today(),
        description="Food",
        is_deleted=FALSE,
    )

    repo.update(updated_transfer)

    mock_accessor.write_all.assert_called_once()


def test_transfer_delete(mock_accessor: Mock) -> None:
    """Checks delete marks row as deleted."""
    transfer_id = uuid4()
    from_account_id = uuid4()
    to_account_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(transfer_id),
            CSVHeaders.FROM_ACCOUNT_ID.value: str(from_account_id),
            CSVHeaders.TO_ACCOUNT_ID.value: str(to_account_id),
            CSVHeaders.AMOUNT.value: "2000.00",
            CSVHeaders.DATE.value: date.today().isoformat(),
            CSVHeaders.DESCRIPTION.value: "Food",
            CSVHeaders.IS_DELETED.value: FALSE,
        }
    ]

    repo = TransferRepository(accessor=mock_accessor)

    repo.delete(transfer_id)

    mock_accessor.write_all.assert_called_once()
