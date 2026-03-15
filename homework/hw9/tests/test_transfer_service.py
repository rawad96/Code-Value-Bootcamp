from solution.services.transfer_service import TransferService

from unittest.mock import Mock, AsyncMock
from uuid import uuid4

import pytest

from constants.headers import TablesHeaders

MESSAGE = "Message"

test_data = {
    TablesHeaders.FROM_ACCOUNT_ID.value: "acc1",
    TablesHeaders.TO_ACCOUNT_ID.value: "acc2",
    TablesHeaders.AMOUNT.value: 500,
    TablesHeaders.DESCRIPTION.value: "test transfer",
}


@pytest.mark.asyncio
async def test_creat_transfer(transfer_service: TransferService) -> None:
    created_id = uuid4()

    transfer_out = {
        TablesHeaders.ID.value: "cat_out",
    }

    transfer_in = {
        TablesHeaders.ID.value: "cat_in",
    }

    mock_transfer = Mock()
    mock_transfer.id = created_id
    mock_transfer.from_account_id = test_data[TablesHeaders.FROM_ACCOUNT_ID.value]
    mock_transfer.to_account_id = test_data[TablesHeaders.TO_ACCOUNT_ID.value]
    mock_transfer.amount = test_data[TablesHeaders.AMOUNT.value]
    mock_transfer.description = test_data[TablesHeaders.DESCRIPTION.value]
    mock_transfer.date = Mock()
    mock_transfer.date.isoformat.return_value = "2024-01-01"

    transfer_service.repo.create.return_value = mock_transfer

    transfer_service.category_service.get_by_name = AsyncMock(
        side_effect=[transfer_out, transfer_in],
    )

    transfer_service.transaction_service.creat_trnsaction = AsyncMock()

    result = await transfer_service.creat_transfer(test_data)

    session = transfer_service.session_maker.return_value.obj

    assert session.begin.call_count == 1
    transfer_service.session_maker.assert_called()

    transfer_service.transaction_service.creat_trnsaction.assert_awaited()

    transfer_service.repo.create.assert_awaited_once()

    new_transfer, session_passed = transfer_service.repo.create.call_args[0]

    assert new_transfer.amount == test_data[TablesHeaders.AMOUNT.value]
    assert session_passed is session

    assert result[TablesHeaders.ID.value] == str(created_id)


@pytest.mark.asyncio
async def test_creat_transfer_missing_categories(
    transfer_service: TransferService,
) -> None:
    test_data = {
        TablesHeaders.FROM_ACCOUNT_ID.value: "acc1",
        TablesHeaders.TO_ACCOUNT_ID.value: "acc2",
        TablesHeaders.AMOUNT.value: 500,
        TablesHeaders.DESCRIPTION.value: "test transfer",
    }

    transfer_service.category_service.get_by_name = AsyncMock(
        return_value=None,
    )

    with pytest.raises(ValueError):
        await transfer_service.creat_transfer(test_data)


@pytest.mark.asyncio
async def test_get_all_transfers(transfer_service: TransferService) -> None:
    tr1 = Mock()
    tr1.id = uuid4()
    tr1.from_account_id = "acc1"
    tr1.to_account_id = "acc2"
    tr1.amount = 100
    tr1.description = "t1"
    tr1.date = Mock()
    tr1.date.isoformat.return_value = "2024-01-01"

    tr2 = Mock()
    tr2.id = uuid4()
    tr2.from_account_id = "acc3"
    tr2.to_account_id = "acc4"
    tr2.amount = 200
    tr2.description = "t2"
    tr2.date = Mock()
    tr2.date.isoformat.return_value = "2024-01-02"

    transfer_service.repo.get_all.return_value = [tr1, tr2]

    result = await transfer_service.get_all_transfers()

    session = transfer_service.session_maker.return_value.obj

    transfer_service.session_maker.assert_called_once()
    transfer_service.repo.get_all.assert_awaited_once_with(session)

    assert len(result) == 2
    assert result[0][TablesHeaders.AMOUNT.value] == str(tr1.amount)


@pytest.mark.asyncio
async def test_get_all_by_account(transfer_service: TransferService) -> None:
    account_id = uuid4()

    tr1 = Mock()
    tr1.id = uuid4()
    tr1.from_account_id = str(account_id)
    tr1.to_account_id = "acc2"
    tr1.amount = 100
    tr1.description = "t1"
    tr1.date = Mock()
    tr1.date.isoformat.return_value = "2024-01-01"

    tr2 = Mock()
    tr2.id = uuid4()
    tr2.from_account_id = "other"
    tr2.to_account_id = "acc3"
    tr2.amount = 200
    tr2.description = "t2"
    tr2.date = Mock()
    tr2.date.isoformat.return_value = "2024-01-02"

    transfer_service.repo.get_all.return_value = [tr1, tr2]

    result = await transfer_service.get_all_by_account(account_id)

    session = transfer_service.session_maker.return_value.obj

    transfer_service.repo.get_all.assert_awaited_once_with(session)

    assert len(result) == 1


@pytest.mark.asyncio
async def test_get_by_id(transfer_service: TransferService) -> None:
    transfer_id = uuid4()

    mock_transfer = Mock()
    mock_transfer.id = transfer_id
    mock_transfer.from_account_id = "acc1"
    mock_transfer.to_account_id = "acc2"
    mock_transfer.amount = 500
    mock_transfer.description = "test"
    mock_transfer.date = Mock()
    mock_transfer.date.isoformat.return_value = "2024-01-01"

    transfer_service.repo.get.return_value = mock_transfer

    result = await transfer_service.get_by_id(transfer_id)

    session = transfer_service.session_maker.return_value.obj

    transfer_service.session_maker.assert_called_once()
    transfer_service.repo.get.assert_awaited_once_with(
        str(transfer_id),
        session,
    )

    assert result[TablesHeaders.ID.value] == str(transfer_id)


@pytest.mark.asyncio
async def test_get_by_id_not_found(
    transfer_service: TransferService,
) -> None:
    transfer_id = uuid4()

    transfer_service.repo.get.return_value = None

    result = await transfer_service.get_by_id(transfer_id)

    assert result is None
