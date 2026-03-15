from unittest.mock import Mock
from uuid import uuid4


import pytest

from constants.headers import TablesHeaders
from solution.services.transaction_service import TransactionService


ACCOUNT_ID = TablesHeaders.ACCOUNT_ID.value
CATEGORY_ID = TablesHeaders.CATEGORY_ID.value
AMOUNT = TablesHeaders.AMOUNT.value
MESSAGE = "Message"


@pytest.mark.asyncio
async def test_creat_trnsaction(transaction_service: TransactionService) -> None:
    created_id = uuid4()
    test_data = {
        TablesHeaders.ACCOUNT_ID.value: "acc1",
        TablesHeaders.CATEGORY_ID.value: "cat1",
        TablesHeaders.AMOUNT.value: 500,
    }

    mock_transaction = Mock()
    mock_transaction.id = created_id
    mock_transaction.account_id = test_data[TablesHeaders.ACCOUNT_ID.value]
    mock_transaction.category_id = test_data[TablesHeaders.CATEGORY_ID.value]
    mock_transaction.amount = test_data[TablesHeaders.AMOUNT.value]
    transaction_service.repo.create.return_value = mock_transaction
    result = await transaction_service.creat_trnsaction(test_data)
    session = transaction_service.session_maker.return_value.obj

    session.begin.assert_called_once()
    transaction_service.session_maker.assert_called_once()
    transaction_service.repo.create.assert_awaited_once()

    new_transaction, session_passed = transaction_service.repo.create.call_args[0]

    assert new_transaction.account_id == test_data[TablesHeaders.ACCOUNT_ID.value]
    assert new_transaction.category_id == test_data[TablesHeaders.CATEGORY_ID.value]
    assert new_transaction.amount == test_data[TablesHeaders.AMOUNT.value]
    assert session_passed is session

    assert result[TablesHeaders.AMOUNT.value] == test_data[TablesHeaders.AMOUNT.value]


@pytest.mark.asyncio
async def test_get_all_transaction(transaction_service: TransactionService) -> None:
    tr1 = Mock()
    tr1.id = uuid4()
    tr1.account_id = "acc1"
    tr1.category_id = "cat1"
    tr1.amount = 100

    tr2 = Mock()
    tr2.id = uuid4()
    tr2.account_id = "acc2"
    tr2.category_id = "cat2"
    tr2.amount = 200

    transaction_service.repo.get_all.return_value = [tr1, tr2]
    result = await transaction_service.get_all_transaction()
    session = transaction_service.session_maker.return_value.obj

    transaction_service.session_maker.assert_called_once()
    transaction_service.repo.get_all.assert_awaited_once_with(session)

    assert len(result) == 2
    assert result[0][TablesHeaders.AMOUNT.value] == tr1.amount
    assert result[1][TablesHeaders.AMOUNT.value] == tr2.amount


@pytest.mark.asyncio
async def test_get_all_by_account(transaction_service: TransactionService) -> None:
    account_id = uuid4()

    tr1 = Mock()
    tr1.id = uuid4()
    tr1.account_id = str(account_id)
    tr1.category_id = "cat1"
    tr1.amount = 100

    tr2 = Mock()
    tr2.id = uuid4()
    tr2.account_id = "other"
    tr2.category_id = "cat2"
    tr2.amount = 200

    transaction_service.repo.get_all.return_value = [tr1, tr2]
    result = await transaction_service.get_all_by_account(account_id)
    session = transaction_service.session_maker.return_value.obj
    transaction_service.repo.get_all.assert_awaited_once_with(session)

    assert len(result) == 1
    assert result[0][TablesHeaders.AMOUNT.value] == tr1.amount


@pytest.mark.asyncio
async def test_get_by_id(transaction_service: TransactionService) -> None:
    transaction_id = uuid4()

    mock_transaction = Mock()
    mock_transaction.id = transaction_id
    mock_transaction.account_id = "acc1"
    mock_transaction.category_id = "cat1"
    mock_transaction.amount = 500

    transaction_service.repo.get.return_value = mock_transaction
    result = await transaction_service.get_by_id(transaction_id)
    session = transaction_service.session_maker.return_value.obj

    transaction_service.session_maker.assert_called_once()
    transaction_service.repo.get.assert_awaited_once_with(
        str(transaction_id),
        session,
    )

    assert result[TablesHeaders.AMOUNT.value] == mock_transaction.amount


@pytest.mark.asyncio
async def test_get_by_id_not_found(
    transaction_service: TransactionService,
) -> None:
    transaction_id = uuid4()
    transaction_service.repo.get.return_value = None
    result = await transaction_service.get_by_id(transaction_id)

    assert result is None


@pytest.mark.asyncio
async def test_delete_transaction(
    transaction_service: TransactionService,
) -> None:
    transaction_id = uuid4()
    result = await transaction_service.delete_transaction(transaction_id)
    session = transaction_service.session_maker.return_value.obj

    transaction_service.repo.delete.assert_awaited_once_with(
        str(transaction_id),
        session,
    )

    assert result == {"Message": "Transaction deleted"}
