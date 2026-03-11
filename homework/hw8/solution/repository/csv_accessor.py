from pathlib import Path
from typing import List, Dict
import csv

WRITE_MODE = "w"
READ_MODE = "r"

ENCODING = "utf-8"


class CsvFileAccessor:
    def __init__(
        self, file_name: str, headers: List[str], base_path: str = "data"
    ) -> None:
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

        self.file_path = self.base_path / file_name
        self.headers = headers

        self._ensure_file_exists()

    def read_all(self) -> List[Dict[str, str]]:
        """Read all rows from the CSV file and return them as a list of dictionaries."""
        with self.file_path.open(mode="r", newline="", encoding=ENCODING) as file:
            reader = csv.DictReader(file)
            return list(reader)

    def write_all(self, rows: List[Dict[str, str]]) -> None:
        """Overwrite the CSV file with the provided rows."""
        with self.file_path.open(mode="w", newline="", encoding=ENCODING) as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(rows)

    def append_row(self, row: Dict[str, str]) -> None:
        """Append row to the CSV file."""
        with self.file_path.open(mode="a", newline="", encoding=ENCODING) as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writerow(row)

    def clear(self) -> None:
        """Remove all data rows and keep the headers."""
        with self.file_path.open(mode="w", newline="", encoding=ENCODING) as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()

    def _ensure_file_exists(self) -> None:
        """Creat the csv file with headers if it's not exist."""
        if not self.file_path.exists():
            with self.file_path.open(
                mode=WRITE_MODE, newline="", encoding=ENCODING
            ) as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()
