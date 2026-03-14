from pathlib import Path
import csv

WRITE_MODE = "w"
READ_MODE = "r"

ENCODING = "utf-8"


class CsvFileAccessor:
    def __init__(
        self, file_name: str, headers: list[str], base_path: str = "data"
    ) -> None:
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

        self.file_path = self.base_path / file_name
        self.headers = headers

        self._ensure_file_exists()

    def read_all(self) -> list[dict[str, str]]:
        """Returns all rows as list of dicts."""
        with self.file_path.open(mode="r", newline="", encoding=ENCODING) as file:
            reader = csv.DictReader(file)
            return list(reader)

    def write_all(self, rows: list[dict[str, str]]) -> None:
        """Overwrites file with given rows."""
        with self.file_path.open(mode="w", newline="", encoding=ENCODING) as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(rows)

    def append_row(self, row: dict[str, str]) -> None:
        """Adds one row to file."""
        with self.file_path.open(mode="a", newline="", encoding=ENCODING) as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writerow(row)

    def clear(self) -> None:
        """Clears data and keeps headers."""
        with self.file_path.open(mode="w", newline="", encoding=ENCODING) as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()

    def _ensure_file_exists(self) -> None:
        """Creates file with headers if missing."""
        if not self.file_path.exists():
            with self.file_path.open(
                mode=WRITE_MODE, newline="", encoding=ENCODING
            ) as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()
