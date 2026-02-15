from solution.return_decimal import binary_to_decimal
import pytest


def test_binary_to_decimal():
    binary_string = "0101"

    assert binary_to_decimal(binary_string) == 5


def test_binary_to_decimal_with_invalid_digit():
    with pytest.raises(ValueError, match="Digits must be 0 or 1"):
        assert binary_to_decimal("0102")


def test_binary_to_decimal_with_short_binary_string():
    with pytest.raises(
        ValueError, match="Binary string must contain at least 2 digits"
    ):
        assert binary_to_decimal("0")
