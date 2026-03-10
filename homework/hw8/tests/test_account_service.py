from solution.services.account_service import AccountService
from unittest.mock import Mock
from solution.models.account import Account
from solution.models.category import CategoryType
from decimal import Decimal
from uuid import uuid4


def test_create_account():
    mock_repo = Mock()
    mock_transaction_service = Mock()
    mock_category_service = Mock()

    service = AccountService(
        repo=mock_repo,
        transaction_service=mock_transaction_service,
        category_service=mock_category_service,
    )

    account = Account(id=uuid4(), name="Bank", opening_balance=Decimal(1200.0))

    result = service.create_account(account)

    mock_repo.create.assert_called_once()

    assert result == {"Message": "Account created"}


def test_get_all_accounts():
    mock_repo = Mock()
    mock_transaction_service = Mock()
    mock_category_service = Mock()

    service = AccountService(
        repo=mock_repo,
        transaction_service=mock_transaction_service,
        category_service=mock_category_service,
    )

    accounts = [
        Account(id=uuid4(), name="bank1", opening_balance=Decimal(1000)),
        Account(id=uuid4(), name="bank2", opening_balance=Decimal(2000)),
    ]

    mock_repo.get_all.return_value = accounts
    result = service.get_all_accounts()

    mock_repo.get_all.assert_called_once()

    assert len(accounts) == 2
    assert result == accounts


def test_get_by_id():
    mock_repo = Mock()
    mock_transaction_service = Mock()
    mock_category_service = Mock()

    service = AccountService(
        repo=mock_repo,
        transaction_service=mock_transaction_service,
        category_service=mock_category_service,
    )

    account_id = uuid4()
    account = Account(id=str(account_id), name="Bank", opening_balance=Decimal(1000))
    mock_repo.get.return_value = account

    result = service.get_by_id(str(account_id))

    mock_repo.get.assert_called_once_with(str(account_id))

    assert result == account


def test_update_account():
    mock_repo = Mock()
    mock_transaction_service = Mock()
    mock_category_service = Mock()

    service = AccountService(
        repo=mock_repo,
        transaction_service=mock_transaction_service,
        category_service=mock_category_service,
    )

    account_id = uuid4()
    account = Account(id=str(account_id), name="Bank", opening_balance=Decimal(1000))
    mock_repo.update.return_value = account

    result = service.update_account(account)

    mock_repo.update.assert_called_once_with(account)

    assert result == account


def test_delete_account():
    mock_repo = Mock()
    mock_transaction_service = Mock()
    mock_category_service = Mock()

    service = AccountService(
        repo=mock_repo,
        transaction_service=mock_transaction_service,
        category_service=mock_category_service,
    )

    account_id = uuid4()
    result = service.delete_account(str(account_id))

    mock_repo.delete.assert_called_once_with(str(account_id))

    assert result == {"Message": "Account deleted"}


def test_calculate_balance():
    mock_repo = Mock()
    mock_transaction_service = Mock()
    mock_category_service = Mock()

    service = AccountService(
        repo=mock_repo,
        transaction_service=mock_transaction_service,
        category_service=mock_category_service,
    )

    account_id = uuid4()
    account = Account(id=str(account_id), name="Bank", opening_balance=Decimal(1000))
    mock_repo.get.return_value = account

    first_category_id = uuid4()
    second_category_id = uuid4()

    first_transaction = Mock(amount=Decimal(50), category_id=first_category_id)
    second_transaction = Mock(amount=Decimal(20), category_id=second_category_id)

    mock_transaction_service.get_all_by_account.return_value = [
        first_transaction,
        second_transaction,
    ]

    first_category = Mock(type=CategoryType.INCOME)
    second_category = Mock(type=CategoryType.EXPENSE)

    mock_category_service.get_by_id.side_effect = [first_category, second_category]

    result = service.calculate_balance(account_id)

    assert result == Decimal(1030)


def test_calculate_net_worth():
    mock_repo = Mock()
    mock_transaction_service = Mock()
    mock_category_service = Mock()

    service = AccountService(
        repo=mock_repo,
        transaction_service=mock_transaction_service,
        category_service=mock_category_service,
    )

    first_account_id = uuid4()
    second_account_id = uuid4()

    first_account = Account(
        id=first_account_id, name="Bank", opening_balance=Decimal(1000)
    )
    second_account = Account(
        id=second_account_id, name="Cash", opening_balance=Decimal(500)
    )

    service.get_all_accounts = Mock(return_value=[first_account, second_account])
    service.calculate_balance = Mock(side_effect=[Decimal(1500), Decimal(400)])

    result = service.calculate_net_worth()

    assert result == Decimal(1900)
