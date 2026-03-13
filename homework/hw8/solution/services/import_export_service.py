import zipfile
import csv
import shutil
import tempfile
from pathlib import Path

from types import MappingProxyType

DATA_FOLDER = Path("data")

ID = "id"
NAME = "name"
AMOUNT = "amount"
IS_DELETED = "is_deleted"
OPENING_BALANCE = "opening_balance"
ACCOUNT_ID = "account_id"
TYPE = "type"
FROM_ACCOUNT_ID = "from_account_id"
TO_ACCOUNT_ID = "to_account_id"
DATE = "date"
DESCRIPTION = "description"
CATEGORY_ID = "category_id"

REQUIRED_FILES = MappingProxyType(
    {
        "accounts.csv": (ID, NAME, OPENING_BALANCE, IS_DELETED),
        "categories.csv": (ID, NAME, TYPE, IS_DELETED),
        "transactions.csv": (
            ID,
            ACCOUNT_ID,
            CATEGORY_ID,
            AMOUNT,
            DATE,
            IS_DELETED,
        ),
        "transfers.csv": (
            ID,
            FROM_ACCOUNT_ID,
            TO_ACCOUNT_ID,
            AMOUNT,
            DATE,
            DESCRIPTION,
            IS_DELETED,
        ),
    }
)


class DataPortabilityService:

    def export_data(self) -> str:
        export_path = DATA_FOLDER / "backup.zip"

        with zipfile.ZipFile(export_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in DATA_FOLDER.glob("*.csv"):
                zipf.write(file, arcname=file.name)

        return str(export_path)

    def import_data(self, zip_path: str) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with zipfile.ZipFile(zip_path, "r") as zipf:
                zipf.extractall(tmp)

            extracted = Path(tmp)

            self._validate_files(extracted)

            for file in REQUIRED_FILES:
                shutil.copy(extracted / file, DATA_FOLDER / file)

    def _check_files_exist(self, folder: Path) -> None:
        for file in REQUIRED_FILES.keys():
            path = folder / file
            if not path.exists():
                raise ValueError(f"Missing file: {file}")

    def _check_file_columns(self, folder: Path) -> None:
        for file, columns in REQUIRED_FILES.items():
            path = folder / file
            self._check_single_file_columns(file, path, columns)

    def _check_single_file_columns(
        self, file: str, path: Path, columns: tuple[str, ...]
    ) -> None:
        with open(path, newline="") as fi:
            reader = csv.DictReader(fi)
            if reader.fieldnames is None:
                raise ValueError(f"{file} has no header row")
            for column in columns:
                if column not in reader.fieldnames:
                    raise ValueError(f"{file} missing column: {column}")

    def _validate_files(self, folder: Path) -> None:
        self._check_files_exist(folder)
        self._check_file_columns(folder)
