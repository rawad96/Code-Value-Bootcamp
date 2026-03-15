import pytest
from unittest.mock import Mock, AsyncMock
from uuid import uuid4

from solution.services.account_service import AccountService
from solution.models.category import CategoryType

from decimal import Decimal

from constants.headers import TablesHeaders

test_data = {"name": "Test Bank", "opening_balance": 1000}


@pytest.mark.asyncio
async def test_create_account(account_service: AccountService) -> None:
    created_id = uuid4()
    mock_account = Mock()
    mock_account.id = created_id
    mock_account.name = test_data[TablesHeaders.NAME.value]
    mock_account.opening_balance = test_data[TablesHeaders.OPENING_BALANCE.value]
    mock_account.is_deleted = False

    account_service.repo.create.return_value = mock_account

    result = await account_service.create_account(test_data)

    session = account_service.session_maker.return_value.obj
    session.begin.assert_called_once()
    account_service.session_maker.assert_called_once()
    account_service.repo.create.assert_awaited_once()

    new_account, session_passed = account_service.repo.create.call_args[0]
    assert new_account.name == test_data[TablesHeaders.NAME.value]
    assert new_account.opening_balance == test_data[TablesHeaders.OPENING_BALANCE.value]
    assert session_passed is session

    assert result[TablesHeaders.NAME.value] == test_data[TablesHeaders.NAME.value]
    assert result[TablesHeaders.OPENING_BALANCE.value] == str(
        test_data[TablesHeaders.OPENING_BALANCE.value]
    )
    assert result[TablesHeaders.ID.value] == str(created_id)
    assert result[TablesHeaders.IS_DELETED.value] is False


@pytest.mark.asyncio
async def test_get_all_accounts(account_service: AccountService) -> None:
    first_acc = {"name": "Test Bank 1", "opening_balance": 1000}
    second_acc = {"name": "Test Bank 2", "opening_balance": 2000}

    acc1 = Mock()
    acc1.id = uuid4()
    acc1.name = first_acc[TablesHeaders.NAME.value]
    acc1.opening_balance = first_acc[TablesHeaders.OPENING_BALANCE.value]
    acc1.is_deleted = False

    acc2 = Mock()
    acc2.id = uuid4()
    acc2.name = second_acc[TablesHeaders.NAME.value]
    acc2.opening_balance = second_acc[TablesHeaders.OPENING_BALANCE.value]
    acc2.is_deleted = False

    account_service.repo.get_all.return_value = [acc1, acc2]

    result = await account_service.get_all_accounts()

    session = account_service.session_maker.return_value.obj

    account_service.session_maker.assert_called_once()
    account_service.repo.get_all.assert_awaited_once_with(session)

    assert len(result) == 2

    assert result[0][TablesHeaders.NAME.value] == acc1.name
    assert result[1][TablesHeaders.NAME.value] == acc2.name

    assert result[0][TablesHeaders.ID.value] == str(acc1.id)
    assert result[1][TablesHeaders.ID.value] == str(acc2.id)


@pytest.mark.asyncio
async def test_get_by_id(account_service: AccountService) -> None:
    account_id = uuid4()

    mock_account = Mock()
    mock_account.id = account_id
    mock_account.name = test_data[TablesHeaders.NAME.value]
    mock_account.opening_balance = test_data[TablesHeaders.OPENING_BALANCE.value]
    mock_account.is_deleted = False

    account_service.repo.get.return_value = mock_account

    result = await account_service.get_by_id(account_id)

    session = account_service.session_maker.return_value.obj

    account_service.session_maker.assert_called_once()
    account_service.repo.get.assert_awaited_once_with(str(account_id), session)

    assert result[TablesHeaders.ID.value] == str(account_id)
    assert result[TablesHeaders.NAME.value] == test_data[TablesHeaders.NAME.value]


@pytest.mark.asyncio
async def test_get_by_id_not_found(account_service: AccountService) -> None:
    account_id = uuid4()
    account_service.repo.get.return_value = None
    result = await account_service.get_by_id(account_id)

    assert result is None


@pytest.mark.asyncio
async def test_update_account(account_service: AccountService) -> None:
    account_id = uuid4()

    test_data = {
        TablesHeaders.ID.value: account_id,
        TablesHeaders.NAME.value: "Updated Bank",
        TablesHeaders.OPENING_BALANCE.value: 2000,
    }

    mock_account = Mock()
    mock_account.id = account_id
    mock_account.name = test_data[TablesHeaders.NAME.value]
    mock_account.opening_balance = test_data[TablesHeaders.OPENING_BALANCE.value]
    mock_account.is_deleted = False

    account_service.repo.update.return_value = mock_account

    result = await account_service.update_account(test_data)

    session = account_service.session_maker.return_value.obj

    account_service.repo.update.assert_awaited_once()

    new_account, session_passed = account_service.repo.update.call_args[0]

    assert new_account.name == test_data[TablesHeaders.NAME.value]
    assert new_account.opening_balance == test_data[TablesHeaders.OPENING_BALANCE.value]
    assert session_passed is session

    assert result[TablesHeaders.NAME.value] == test_data[TablesHeaders.NAME.value]


@pytest.mark.asyncio
async def test_delete_account(account_service: AccountService) -> None:
    account_id = uuid4()
    result = await account_service.delete_account(account_id)
    session = account_service.session_maker.return_value.obj
    account_service.repo.delete.assert_awaited_once_with(str(account_id), session)

    assert result == {"Message": "Account deleted"}


@pytest.mark.asyncio
async def test_calculate_balance(account_service: AccountService) -> None:
    account_id = uuid4()

    mock_account = Mock()
    mock_account.id = account_id
    mock_account.opening_balance = test_data[TablesHeaders.OPENING_BALANCE.value]

    account_service.repo.get.return_value = mock_account

    transactions = [
        {
            TablesHeaders.AMOUNT.value: 500,
            TablesHeaders.CATEGORY_ID.value: "1",
        },
        {
            TablesHeaders.AMOUNT.value: 200,
            TablesHeaders.CATEGORY_ID.value: "2",
        },
    ]

    account_service.transaction_service.get_all_by_account.return_value = transactions

    category_cache = {
        "1": {TablesHeaders.TYPE.value: CategoryType.INCOME.value},
        "2": {TablesHeaders.TYPE.value: CategoryType.EXPENSE.value},
    }

    account_service._build_category_cache = AsyncMock(return_value=category_cache)

    result = await account_service.calculate_balance(account_id)

    assert result == Decimal(1300)


@pytest.mark.asyncio
async def test_calculate_balance_account_not_found(
    account_service: AccountService,
) -> None:
    account_id = uuid4()
    account_service.repo.get.return_value = None

    with pytest.raises(ValueError):
        await account_service.calculate_balance(account_id)


@pytest.mark.asyncio
async def test_calculate_net_worth(account_service: AccountService) -> None:
    acc1 = Mock()
    acc1.id = uuid4()

    acc2 = Mock()
    acc2.id = uuid4()

    account_service.repo.get_all.return_value = [acc1, acc2]

    account_service.calculate_balance = AsyncMock(
        side_effect=[Decimal(1000), Decimal(2000)]
    )

    result = await account_service.calculate_net_worth()

    assert result == Decimal(3000)
