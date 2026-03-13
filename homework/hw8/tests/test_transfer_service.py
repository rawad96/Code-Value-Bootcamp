from solution.services.transfer_service import TransferService
from solution.models.transfer import Transfer

from unittest.mock import Mock
from uuid import uuid4
from decimal import Decimal
from typing import Any
from datetime import date

import pytest

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
    mock_repo: Mock, mock_transaction_service: Mock, mock_category_service: Mock
) -> TransferService:
    """Returns TransferService with mocks."""
    return TransferService(
        repo=mock_repo,
        transaction_service=mock_transaction_service,
        category_service=mock_category_service,
    )


def test_create_transfer(
    service: TransferService,
    mock_repo: Mock,
    mock_transaction_service: Mock,
    mock_category_service: Mock,
) -> None:
    transfer_out = {CSVHeaders.ID.value: uuid4()}
    transfer_in = {CSVHeaders.ID.value: uuid4()}

    mock_category_service.get_by_name.side_effect = [transfer_out, transfer_in]

    transfer_data: dict[str, Any] = {
        CSVHeaders.FROM_ACCOUNT_ID.value: uuid4(),
        CSVHeaders.TO_ACCOUNT_ID.value: uuid4(),
        CSVHeaders.AMOUNT.value: Decimal(100),
        CSVHeaders.DESCRIPTION.value: "Test transfer",
    }

    result = service.creat_transfer(transfer_data)

    mock_repo.create.assert_called_once()
    assert mock_transaction_service.creat_trnsaction.call_count == 2
    assert result == {MESSAGE: "Transfer created"}


def test_get_all_transfers(service: TransferService, mock_repo: Mock) -> None:
    """Checks get_all_transfers returns list of dicts."""
    transfer_one = Transfer(
        id=uuid4(),
        from_account_id=uuid4(),
        to_account_id=uuid4(),
        amount=Decimal(100),
        date=date.today(),
        description="test",
        is_deleted="false",
    )
    transfer_two = Transfer(
        id=uuid4(),
        from_account_id=uuid4(),
        to_account_id=uuid4(),
        amount=Decimal(50),
        date=date.today(),
        description="test",
        is_deleted="false",
    )

    mock_repo.get_all.return_value = [transfer_one, transfer_two]

    result = service.get_all_transfers()

    mock_repo.get_all.assert_called_once()
    assert result[0][CSVHeaders.AMOUNT.value] == str(transfer_one.amount)
    assert result[1][CSVHeaders.AMOUNT.value] == str(transfer_two.amount)


def test_get_all_by_account(service: TransferService, mock_repo: Mock) -> None:
    """Checks get_all_by_account returns only transfers for account."""
    account_id = uuid4()

    transfer_one = Transfer(
        id=uuid4(),
        from_account_id=account_id,
        to_account_id=uuid4(),
        amount=Decimal(100),
        date=date.today(),
        description="",
        is_deleted="false",
    )
    transfer_two = Transfer(
        id=uuid4(),
        from_account_id=uuid4(),
        to_account_id=account_id,
        amount=Decimal(50),
        date=date.today(),
        description="",
        is_deleted="false",
    )
    transfer_three = Transfer(
        id=uuid4(),
        from_account_id=uuid4(),
        to_account_id=uuid4(),
        amount=Decimal(70),
        date=date.today(),
        description="",
        is_deleted="false",
    )

    mock_repo.get_all.return_value = [transfer_one, transfer_two, transfer_three]

    result = service.get_all_by_account(account_id)

    assert len(result) == 2
    assert all(
        account_id
        in (
            transfer[CSVHeaders.FROM_ACCOUNT_ID.value],
            transfer[CSVHeaders.TO_ACCOUNT_ID.value],
        )
        for transfer in result
    )


def test_get_by_id(service: TransferService, mock_repo: Mock) -> None:
    transfer_id = uuid4()

    transfer = Transfer(
        id=transfer_id,
        from_account_id=uuid4(),
        to_account_id=uuid4(),
        amount=Decimal(100),
        date=date.today(),
        description="",
        is_deleted="false",
    )

    mock_repo.get.return_value = transfer

    result = service.get_by_id(transfer_id)

    mock_repo.get.assert_called_once_with(transfer_id)
    assert result["id"] == str(transfer_id)


def test_delete_transfer(service: TransferService, mock_repo: Mock) -> None:
    """Checks delete_transfer calls repo.delete and returns message."""
    transfer_id = uuid4()

    result = service.delete_transfer(transfer_id)

    mock_repo.delete.assert_called_once_with(transfer_id)
    assert result == {MESSAGE: "Transfer deleted"}
