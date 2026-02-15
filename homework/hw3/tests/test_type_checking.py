from solution.type_checking import (
    format_data,
)
import pytest


def test_format_data_valid() -> None:
    first_result = format_data(
        "Alice", 30, {"key": "value"}, other_info="Additional info"
    )
    second_result = format_data("Bob", 25, {"key": "data"})
    assert (
        first_result
        == "Name: Alice, Age: 30, Data: value, Other Info : Additional info"
    )
    assert second_result == "Name: Bob, Age: 25, Data: data"


def test_format_data_with_wrong_type() -> None:
    with pytest.raises(TypeError):
        format_data(123, 30, {"key": "value"})
