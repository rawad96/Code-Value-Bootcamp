from uuid import uuid4
from datetime import date
from unittest.mock import Mock
import pytest

from solution.models.transfer import Transfer

from solution.repository.transfer_repository import TransferRepository


@pytest.fixture
def mock_accessor():
    return Mock()


def test_creat_transfer(mock_accessor):
    transfer_repo = TransferRepository(accessor=mock_accessor)

    transfer_id = uuid4()
    from_account_id = uuid4()
    to_account_id = uuid4()

    transfer = Transfer(
        id=transfer_id,
        from_account_id=from_account_id,
        to_account_id=to_account_id,
        amount=2000.00,
        date=date.today(),
        description="Food",
    )

    transfer_repo.create(transfer)

    mock_accessor.append_row.assert_called_once()

    args = mock_accessor.append_row.call_args[0][0]

    assert args["id"] == str(transfer_id)
    assert args["from_account_id"] == str(from_account_id)
    assert args["to_account_id"] == str(to_account_id)
    assert args["amount"] == "2000.0"
    assert args["date"] == date.today().isoformat()
    assert args["description"] == "Food"


def test_transfer_get_by_id(mock_accessor):
    transfer_id = uuid4()
    from_account_id = uuid4()
    to_account_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            "id": str(transfer_id),
            "from_account_id": str(from_account_id),
            "to_account_id": str(to_account_id),
            "amount": "2000.0",
            "date": date.today().isoformat(),
            "description": "Food",
        }
    ]

    repo = TransferRepository(accessor=mock_accessor)

    returned_transfer = repo.get(transfer_id)

    assert isinstance(returned_transfer, Transfer)
    assert returned_transfer.id == transfer_id


def test_transfer_get_all(mock_accessor):
    transfer_id1 = uuid4()
    transfer_id2 = uuid4()

    from_account_id = uuid4()
    to_account_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            "id": str(transfer_id1),
            "from_account_id": str(from_account_id),
            "to_account_id": str(to_account_id),
            "amount": "2000.0",
            "date": date.today().isoformat(),
            "description": "Food",
        },
        {
            "id": str(transfer_id2),
            "from_account_id": str(from_account_id),
            "to_account_id": str(to_account_id),
            "amount": "1000.0",
            "date": date.today().isoformat(),
            "description": "shopping",
        },
    ]

    repo = TransferRepository(accessor=mock_accessor)

    returned_transfers = repo.get_all()

    assert len(returned_transfers) == 2
    assert all(isinstance(transfer, Transfer) for transfer in returned_transfers)


def test_transfer_update(mock_accessor):
    transfer_id = uuid4()
    from_account_id = uuid4()
    to_account_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            "id": str(transfer_id),
            "from_account_id": str(from_account_id),
            "to_account_id": str(to_account_id),
            "amount": "2000.0",
            "date": date.today().isoformat(),
            "description": "Food",
        }
    ]

    repo = TransferRepository(accessor=mock_accessor)

    updated_transfer = Transfer(
        id=transfer_id,
        from_account_id=from_account_id,
        to_account_id=to_account_id,
        amount=1000.00,
        date=date.today(),
        description="Food",
    )

    repo.update(updated_transfer)

    mock_accessor.write_all.assert_called_once()


def test_transfer_delete(mock_accessor):
    transfer_id = uuid4()
    from_account_id = uuid4()
    to_account_id = uuid4()

    mock_accessor.read_all.return_value = [
        {
            "id": str(transfer_id),
            "from_account_id": str(from_account_id),
            "to_account_id": str(to_account_id),
            "amount": "2000.0",
            "date": date.today().isoformat(),
            "description": "Food",
        }
    ]

    repo = TransferRepository(accessor=mock_accessor)

    repo.delete(transfer_id)

    mock_accessor.write_all.assert_called_once()
