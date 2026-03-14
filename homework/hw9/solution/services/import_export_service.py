import zipfile
import csv
import shutil
import tempfile
from pathlib import Path

from types import MappingProxyType

from constants.headers import TablesHeaders

DATA_FOLDER = Path("data")

REQUIRED_FILES = MappingProxyType(
    {
        "accounts.csv": (
            TablesHeaders.ID.value,
            TablesHeaders.NAME.value,
            TablesHeaders.OPENING_BALANCE.value,
            TablesHeaders.IS_DELETED.value,
        ),
        "categories.csv": (
            TablesHeaders.ID.value,
            TablesHeaders.NAME.value,
            TablesHeaders.TYPE.value,
            TablesHeaders.IS_DELETED.value,
        ),
        "transactions.csv": (
            TablesHeaders.ID.value,
            TablesHeaders.ACCOUNT_ID.value,
            TablesHeaders.CATEGORY_ID.value,
            TablesHeaders.AMOUNT.value,
            TablesHeaders.DATE.value,
            TablesHeaders.IS_DELETED.value,
        ),
        "transfers.csv": (
            TablesHeaders.ID.value,
            TablesHeaders.FROM_ACCOUNT_ID.value,
            TablesHeaders.TO_ACCOUNT_ID.value,
            TablesHeaders.AMOUNT.value,
            TablesHeaders.DATE.value,
            TablesHeaders.DESCRIPTION.value,
            TablesHeaders.IS_DELETED.value,
        ),
    }
)


class DataPortabilityService:

    def export_data(self) -> str:
        """Zips all CSV data and returns path to zip."""
        export_path = DATA_FOLDER / "backup.zip"

        with zipfile.ZipFile(export_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in DATA_FOLDER.glob("*.csv"):
                zipf.write(file, arcname=file.name)

        return str(export_path)

    def import_data(self, zip_path: str) -> None:
        """Extracts zip and replaces data with zip contents."""
        with tempfile.TemporaryDirectory() as tmp:
            with zipfile.ZipFile(zip_path, "r") as zipf:
                zipf.extractall(tmp)

            extracted = Path(tmp)

            self._validate_files(extracted)

            for file in REQUIRED_FILES:
                shutil.copy(extracted / file, DATA_FOLDER / file)

    def _check_files_exist(self, folder: Path) -> None:
        """Raises if any required CSV is missing."""
        for file in REQUIRED_FILES.keys():
            path = folder / file
            if not path.exists():
                raise ValueError(f"Missing file: {file}")

    def _check_file_columns(self, folder: Path) -> None:
        """Raises if any file has wrong columns."""
        for file, columns in REQUIRED_FILES.items():
            path = folder / file
            self._check_single_file_columns(file, path, columns)

    def _check_single_file_columns(
        self, file: str, path: Path, columns: tuple[str, ...]
    ) -> None:
        """Raises if file missing any of given columns."""
        with open(path, newline="") as fi:
            reader = csv.DictReader(fi)
            if reader.fieldnames is None:
                raise ValueError(f"{file} has no header row")
            for column in columns:
                if column not in reader.fieldnames:
                    raise ValueError(f"{file} missing column: {column}")

    def _validate_files(self, folder: Path) -> None:
        """Checks files exist and have right columns."""
        self._check_files_exist(folder)
        self._check_file_columns(folder)
