import tempfile
from pathlib import Path
from uuid import uuid4
from datetime import date

from solution.models.transaction import Transaction

from solution.repository.csv_accessor import CsvFileAccessor
from solution.repository.transaction_repositort import TransactionRepository

from constants.headers import transaction_headers


def test_creat_transaction():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)

        transaction_accessor = CsvFileAccessor(
            file_name="transactions.csv",
            headers=transaction_headers,
            base_path=tmp_path,
        )

        transaction_repo = TransactionRepository(accessor=transaction_accessor)

        account_uuid = uuid4()
        transaction_uuid = uuid4()
        category_uuid = uuid4()

        transaction = Transaction(
            id=transaction_uuid,
            account_id=account_uuid,
            category_id=category_uuid,
            amount=2000.00,
            date=date.today(),
        )

        transaction_repo.create(transaction)

        returned_transaction = transaction_repo.get(transaction_uuid)

        assert isinstance(returned_transaction, Transaction)
        assert returned_transaction == transaction


def test_transaction_get_by_id():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)

        accessor = CsvFileAccessor(
            file_name="transactions.csv",
            headers=transaction_headers,
            base_path=tmp_path,
        )

        repo = TransactionRepository(accessor=accessor)

        account_id = uuid4()
        transaction_id = uuid4()
        category_id = uuid4()

        transaction = Transaction(
            id=transaction_id,
            account_id=account_id,
            category_id=category_id,
            amount=2000.00,
            date=date.today(),
        )

        repo.create(transaction)

        file_path = tmp_path / "transactions.csv"
        assert file_path.exists()

        returned_transaction = repo.get(transaction_id)
        assert isinstance(returned_transaction, Transaction)
        assert returned_transaction == transaction


def test_transaction_get_all():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)

        accessor = CsvFileAccessor(
            file_name="transactions.csv",
            headers=transaction_headers,
            base_path=tmp_path,
        )

        repo = TransactionRepository(accessor=accessor)

        account_id = uuid4()
        income_transaction_id = uuid4()
        income_category_id = uuid4()

        expense_transaction_id = uuid4()
        expense_category_id = uuid4()

        income = Transaction(
            id=income_transaction_id,
            account_id=account_id,
            category_id=income_category_id,
            amount=2000.00,
            date=date.today(),
        )

        expense = Transaction(
            id=expense_transaction_id,
            account_id=account_id,
            category_id=expense_category_id,
            amount=2000.00,
            date=date.today(),
        )

        repo.create(income)
        repo.create(expense)

        file_path = tmp_path / "transactions.csv"
        assert file_path.exists()

        returned_transactions = repo.get_all()
        assert all(
            isinstance(transaction, Transaction)
            for transaction in returned_transactions
        )


def test_transaction_update():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)

        accessor = CsvFileAccessor(
            file_name="transactions.csv",
            headers=transaction_headers,
            base_path=tmp_path,
        )

        repo = TransactionRepository(accessor=accessor)

        account_id = uuid4()
        transaction_id = uuid4()
        category_id = uuid4()

        transaction = Transaction(
            id=transaction_id,
            account_id=account_id,
            category_id=category_id,
            amount=2000.00,
            date=date.today(),
        )

        repo.create(transaction)

        file_path = tmp_path / "transactions.csv"
        assert file_path.exists()

        updated_transaction = Transaction(
            id=transaction_id,
            account_id=account_id,
            category_id=category_id,
            amount=1000.00,
            date=date.today(),
        )

        repo.update(updated_transaction)
        returned_transaction = repo.get(transaction_id)
        assert isinstance(returned_transaction, Transaction)
        assert returned_transaction == updated_transaction


def test_transaction_delete():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)

        accessor = CsvFileAccessor(
            file_name="transactions.csv",
            headers=transaction_headers,
            base_path=tmp_path,
        )

        repo = TransactionRepository(accessor=accessor)

        account_id = uuid4()
        transaction_id = uuid4()
        category_id = uuid4()

        transaction = Transaction(
            id=transaction_id,
            account_id=account_id,
            category_id=category_id,
            amount=2000.00,
            date=date.today(),
        )

        repo.create(transaction)

        file_path = tmp_path / "transactions.csv"
        assert file_path.exists()

        repo.delete(transaction_id)
        assert repo.get(transaction_id) == None
