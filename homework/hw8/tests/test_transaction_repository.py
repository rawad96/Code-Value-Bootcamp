import tempfile
from pathlib import Path
from decimal import Decimal
from uuid import uuid4
from datetime import date

from solution.models.account import Account
from solution.models.transaction import Transaction
from solution.models.category import Category, CategoryType

from solution.repository.account_repository import AccountRepository
from solution.repository.csv_accessor import CsvFileAccessor
from solution.repository.category_repository import CategoryRepository
from solution.repository.transaction_repositort import TransactionRepository

from constants.headers import account_headers, transaction_headers, category_headers


def test_creat_transaction():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)

        accounts_accessor = CsvFileAccessor(
            file_name="accounts.csv",
            headers=account_headers,
            base_path=tmp_path,
        )

        transaction_accessor = CsvFileAccessor(
            file_name="transactions.csv",
            headers=transaction_headers,
            base_path=tmp_path,
        )

        category_accessor = CsvFileAccessor(
            file_name="categories.csv",
            headers=category_headers,
            base_path=tmp_path,
        )

        account_repo = AccountRepository(accessor=accounts_accessor)
        transaction_repo = TransactionRepository(accessor=transaction_accessor)
        category_repo = CategoryRepository(accessor=category_accessor)

        account_uuid = uuid4()
        transaction_uuid = uuid4()
        category_uuid = uuid4()

        account = Account(
            id=account_uuid, name="Main Account", opening_balance=Decimal("1000.50")
        )

        category = Category(id=category_uuid, name="salary", type=CategoryType.INCOME)

        transaction = Transaction(
            id=transaction_uuid,
            account_id=account_uuid,
            category_id=category_uuid,
            amount=2000.00,
            date=date.today(),
        )

        account_repo.create(account)
        category_repo.create(category)
        transaction_repo.create(transaction)

        returned_category = category_repo.get(category_uuid)
        returned_transaction = transaction_repo.get(transaction_uuid)

        assert isinstance(returned_category, Category)
        assert returned_category == category

        assert isinstance(returned_transaction, Transaction)
        assert returned_transaction == transaction
