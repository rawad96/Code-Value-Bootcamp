import tempfile
from pathlib import Path
from decimal import Decimal
from uuid import uuid4

from solution.models.account import Account
from solution.repository.account_repository import AccountRepository
from solution.repository.csv_accessor import CsvFileAccessor

from constants.headers import account_headers


def test_account_repository_create():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)

        accessor = CsvFileAccessor(
            file_name="accounts.csv",
            headers=account_headers,
            base_path=tmp_path,
        )

        repo = AccountRepository(accessor=accessor)

        uuid_id = uuid4()
        uuid_id_second = uuid4()
        account = Account(
            id=uuid_id, name="Main Account", opening_balance=Decimal("1000.50")
        )
        second_account = Account(
            id=uuid_id_second, name="Second Account", opening_balance=Decimal("200.00")
        )

        repo.create(account)
        repo.create(second_account)

        file_path = tmp_path / "accounts.csv"
        assert file_path.exists()

        returned_account = repo.get(uuid_id)
        assert isinstance(returned_account, Account)
        assert returned_account == account

        returned_accounts = repo.get_all()
        assert all(isinstance(acc, Account) for acc in returned_accounts)


def test_account_repository_get_by_id():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)

        accessor = CsvFileAccessor(
            file_name="accounts.csv",
            headers=account_headers,
            base_path=tmp_path,
        )

        repo = AccountRepository(accessor=accessor)

        uuid_id = uuid4()
        account = Account(
            id=uuid_id, name="Main Account", opening_balance=Decimal("1000.50")
        )

        repo.create(account)

        file_path = tmp_path / "accounts.csv"
        assert file_path.exists()

        returned_account = repo.get(uuid_id)
        assert isinstance(returned_account, Account)
        assert returned_account == account


def test_account_repository_get_all():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)

        accessor = CsvFileAccessor(
            file_name="accounts.csv",
            headers=account_headers,
            base_path=tmp_path,
        )

        repo = AccountRepository(accessor=accessor)

        uuid_id = uuid4()
        uuid_id_second = uuid4()
        account = Account(
            id=uuid_id, name="Main Account", opening_balance=Decimal("1000.50")
        )
        second_account = Account(
            id=uuid_id_second, name="Second Account", opening_balance=Decimal("200.00")
        )

        repo.create(account)
        repo.create(second_account)

        file_path = tmp_path / "accounts.csv"
        assert file_path.exists()

        returned_accounts = repo.get_all()
        assert all(isinstance(acc, Account) for acc in returned_accounts)


def test_account_repository_update():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)

        accessor = CsvFileAccessor(
            file_name="accounts.csv",
            headers=account_headers,
            base_path=tmp_path,
        )

        repo = AccountRepository(accessor=accessor)

        uuid_id = uuid4()
        account = Account(
            id=uuid_id, name="Main Account", opening_balance=Decimal("1000.50")
        )

        repo.create(account)

        file_path = tmp_path / "accounts.csv"
        assert file_path.exists()

        updated_account = Account(
            id=uuid_id, name="Main Account", opening_balance=Decimal("2000.00")
        )

        repo.update(updated_account)
        returned_account = repo.get(uuid_id)
        assert isinstance(returned_account, Account)
        assert returned_account == updated_account


def test_account_repository_delete():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)

        accessor = CsvFileAccessor(
            file_name="accounts.csv",
            headers=account_headers,
            base_path=tmp_path,
        )

        repo = AccountRepository(accessor=accessor)

        uuid_id = uuid4()
        account = Account(
            id=uuid_id, name="Main Account", opening_balance=Decimal("1000.50")
        )

        repo.create(account)

        file_path = tmp_path / "accounts.csv"
        assert file_path.exists()

        repo.delete(str(uuid_id))
        assert repo.get(str(uuid_id)) == None
