import tempfile
import os
from typing import Any
from solution.repository.csv_accessor import CsvFileAccessor
from constants.headers import csv_accessor_headers, CSVHeaders


def test_file_created() -> None:
    """Checks file is created with headers."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        accessor = CsvFileAccessor(
            file_name="test.csv", headers=csv_accessor_headers, base_path=tmpdirname
        )
        assert os.path.exists(accessor.file_path)
        rows = accessor.read_all()
        assert rows == []


def test_append_row() -> None:
    """Checks append adds one row."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        accessor = CsvFileAccessor(
            file_name="test.csv", headers=csv_accessor_headers, base_path=tmpdirname
        )
        row: dict[str, Any] = {
            CSVHeaders.ID.value: "123",
            CSVHeaders.NAME.value: "Test",
            CSVHeaders.OPENING_BALANCE.value: "10.5",
            CSVHeaders.IS_DELETED.value: "false",
        }
        accessor.append_row(row)

        rows = accessor.read_all()
        assert len(rows) == 1
        assert rows[0][CSVHeaders.ID.value] == "123"
        assert rows[0][CSVHeaders.NAME.value] == "Test"
        assert rows[0][CSVHeaders.OPENING_BALANCE.value] == "10.5"
        assert rows[0][CSVHeaders.IS_DELETED.value] == "false"


def test_write_all() -> None:
    """Test overwriting CSV file with multiple rows including is_deleted."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        accessor = CsvFileAccessor(
            file_name="test.csv", headers=csv_accessor_headers, base_path=tmpdirname
        )
        new_rows: list[dict[str, Any]] = [
            {
                CSVHeaders.ID.value: "1",
                CSVHeaders.NAME.value: "Alice",
                CSVHeaders.OPENING_BALANCE.value: "100",
                CSVHeaders.IS_DELETED.value: "false",
            },
            {
                CSVHeaders.ID.value: "2",
                CSVHeaders.NAME.value: "Bob",
                CSVHeaders.OPENING_BALANCE.value: "200",
                CSVHeaders.IS_DELETED.value: "false",
            },
        ]
        accessor.write_all(new_rows)

        rows = accessor.read_all()
        assert len(rows) == 2
        assert rows[0][CSVHeaders.NAME.value] == "Alice"
        assert rows[0][CSVHeaders.IS_DELETED.value] == "false"
        assert rows[1][CSVHeaders.NAME.value] == "Bob"
        assert rows[1][CSVHeaders.IS_DELETED.value] == "false"


def test_clear() -> None:
    """Checks clear keeps only headers."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        accessor = CsvFileAccessor(
            file_name="test.csv", headers=csv_accessor_headers, base_path=tmpdirname
        )
        accessor.write_all(
            [
                {
                    CSVHeaders.ID.value: "1",
                    CSVHeaders.NAME.value: "Alice",
                    CSVHeaders.OPENING_BALANCE.value: "100",
                    CSVHeaders.IS_DELETED.value: "false",
                },
                {
                    CSVHeaders.ID.value: "2",
                    CSVHeaders.NAME.value: "Bob",
                    CSVHeaders.OPENING_BALANCE.value: "200",
                    CSVHeaders.IS_DELETED.value: "true",
                },
            ]
        )
        accessor.clear()
        rows = accessor.read_all()
        assert rows == []
