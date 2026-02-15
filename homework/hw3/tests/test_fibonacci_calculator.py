from solution.fibonacci_calculator import (
    fibonacci_calculator,
    fibonacci_calculator_with_cache,
)
import pytest


def test_fibonacci_calculator() -> None:
    assert fibonacci_calculator(limit=1) == 0
    assert fibonacci_calculator(limit=2) == 1
    assert fibonacci_calculator(limit=3) == 1
    assert fibonacci_calculator(limit=10) == 34
    assert fibonacci_calculator(limit=200) == 173402521172797813159685037284371942044301


def test_fibonacci_calculator_with_cache() -> None:
    assert fibonacci_calculator_with_cache(limit=1) == 0
    assert fibonacci_calculator_with_cache(limit=2) == 1
    assert fibonacci_calculator_with_cache(limit=3) == 1
    assert fibonacci_calculator_with_cache(limit=10) == 34
    assert (
        fibonacci_calculator_with_cache(limit=200)
        == 173402521172797813159685037284371942044301
    )


def test_fibonacci_calculator_with_invalid_limit() -> None:
    with pytest.raises(ValueError, match="Limit can't be less than 1!!!"):
        assert fibonacci_calculator(limit=0)


def test_fibonacci_calculator_with_cache_invalid() -> None:
    with pytest.raises(ValueError, match="Limit can't be less than 1!!!"):
        assert fibonacci_calculator_with_cache(limit=0)
