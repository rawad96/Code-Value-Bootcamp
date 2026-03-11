from solution.models.transfer import Transfer
from solution.services.transfer_service import TransferService
from unittest.mock import Mock
from uuid import uuid4
from decimal import Decimal


def test_create_transfer():
    mock_repo = Mock()
    mock_transaction_service = Mock()
    mock_category_service = Mock()

    transfer_out = Mock()
    transfer_out.id = uuid4()

    transfer_in = Mock()
    transfer_in.id = uuid4()

    mock_category_service.get_by_name.side_effect = [transfer_out, transfer_in]

    service = TransferService(
        repo=mock_repo,
        transaction_service=mock_transaction_service,
        category_service=mock_category_service,
    )

    transfer = Transfer(
        id=uuid4(),
        from_account_id=uuid4(),
        to_account_id=uuid4(),
        amount=Decimal(100),
        date="2024-01-01",
        description="test",
    )

    result = service.creat_transfer(transfer)

    mock_repo.create.assert_called_once()
    assert mock_transaction_service.creat_trnsaction.call_count == 2
    assert result == {"Message": "Transfer created"}


def test_get_all_transfers():
    mock_repo = Mock()
    mock_transaction_service = Mock()
    mock_category_service = Mock()

    service = TransferService(
        repo=mock_repo,
        transaction_service=mock_transaction_service,
        category_service=mock_category_service,
    )

    first_transfer = Transfer(
        id=uuid4(),
        from_account_id=uuid4(),
        to_account_id=uuid4(),
        amount=Decimal(100),
        date="2024-01-01",
        description="test",
    )
    second_transfer = Transfer(
        id=uuid4(),
        from_account_id=uuid4(),
        to_account_id=uuid4(),
        amount=Decimal(50),
        date="2024-01-02",
        description="test",
    )

    mock_repo.get_all.return_value = [first_transfer, second_transfer]

    result = service.get_all_transfers()

    mock_repo.get_all.assert_called_once()
    assert result == [first_transfer, second_transfer]


def test_get_all_by_account():
    mock_repo = Mock()
    mock_transaction_service = Mock()
    mock_category_service = Mock()

    service = TransferService(
        repo=mock_repo,
        transaction_service=mock_transaction_service,
        category_service=mock_category_service,
    )

    account_id = uuid4()
    transfer_one = Transfer(
        id=uuid4(),
        from_account_id=account_id,
        to_account_id=uuid4(),
        amount=Decimal(100),
        date="2024-01-01",
        description="",
    )
    transfer_two = Transfer(
        id=uuid4(),
        from_account_id=uuid4(),
        to_account_id=account_id,
        amount=Decimal(50),
        date="2024-01-02",
        description="",
    )
    transfer_three = Transfer(
        id=uuid4(),
        from_account_id=uuid4(),
        to_account_id=uuid4(),
        amount=Decimal(70),
        date="2024-01-03",
        description="",
    )

    mock_repo.get_all.return_value = [transfer_one, transfer_two, transfer_three]

    result = service.get_all_by_account(account_id)

    assert result == [transfer_one, transfer_two]


def test_get_by_id():
    mock_repo = Mock()
    mock_transaction_service = Mock()
    mock_category_service = Mock()

    service = TransferService(
        repo=mock_repo,
        transaction_service=mock_transaction_service,
        category_service=mock_category_service,
    )

    transfer_id = uuid4()
    transfer = Transfer(
        id=transfer_id,
        from_account_id=uuid4(),
        to_account_id=uuid4(),
        amount=Decimal(100),
        date="2024-01-01",
        description="",
    )

    mock_repo.get.return_value = transfer

    result = service.get_by_id(transfer_id)

    mock_repo.get.assert_called_once_with(transfer_id)
    assert result == transfer


def test_delete_transfer():
    mock_repo = Mock()
    mock_transaction_service = Mock()
    mock_category_service = Mock()

    service = TransferService(
        repo=mock_repo,
        transaction_service=mock_transaction_service,
        category_service=mock_category_service,
    )

    transfer_id = uuid4()
    result = service.delete_transfer(transfer_id)

    mock_repo.delete.assert_called_once_with(transfer_id)
    assert result == {"Message": "Transfer deleted"}
