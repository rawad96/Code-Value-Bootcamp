import tempfile
import os
from solution.repository.csv_accessor import CsvFileAccessor


def test_csv_accessor():
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_name = "test.csv"
        headers = ["id", "name", "opening_balance"]

        accessor = CsvFileAccessor(
            file_name=file_name, headers=headers, base_path=tmpdirname
        )

        assert os.path.exists(os.path.join(tmpdirname, file_name))

        rows = accessor.read_all()
        assert rows == []

        row = {"id": "123", "name": "Test", "opening_balance": "10.5"}
        accessor.append_row(row)

        rows = accessor.read_all()
        assert len(rows) == 1
        assert rows[0]["id"] == "123"
        assert rows[0]["name"] == "Test"
        assert rows[0]["opening_balance"] == "10.5"

        new_rows = [
            {"id": "1", "name": "Alice", "opening_balance": "100"},
            {"id": "2", "name": "Bob", "opening_balance": "200"},
        ]
        accessor.write_all(new_rows)

        rows = accessor.read_all()
        assert len(rows) == 2
        assert rows[0]["name"] == "Alice"
        assert rows[1]["name"] == "Bob"

        accessor.clear()
        rows = accessor.read_all()
        assert rows == []
