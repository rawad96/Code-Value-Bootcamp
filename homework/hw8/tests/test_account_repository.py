import tempfile
from pathlib import Path
from decimal import Decimal
from uuid import UUID, uuid4

from solution.models.account import Account
from solution.repository.account_repository import AccountRepository
from solution.repository.csv_accessor import CsvFileAccessor


def test_account_repository_create():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)

        accessor = CsvFileAccessor(
            file_name="accounts.csv",
            headers=["id", "name", "opening_balance"],
            base_path=tmp_path,
        )

        repo = AccountRepository(accessor=accessor)

        account = Account(
            id=uuid4(), name="Main Account", opening_balance=Decimal("1000.50")
        )

        created_account = repo.create(account)
        with open(tmp_path / "accounts.csv", "r", newline="", encoding="utf-8") as f:
            print(f.read())

        assert isinstance(created_account.id, UUID)

        file_path = tmp_path / "accounts.csv"
        assert file_path.exists()

        rows = accessor.read_all()
        assert len(rows) == 1
        assert rows[0]["id"] == str(account.id)
        assert rows[0]["name"] == "Main Account"
        assert rows[0]["opening_balance"] == "1000.50"
