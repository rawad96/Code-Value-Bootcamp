from solution.quadratic_equation import quadratic_equation
import pytest


def test_quadratic_equation():
    assert quadratic_equation(a=1, b=-3, c=2) == "x1 = 1.00, x2 = 2.00"
    assert quadratic_equation(a=-1, b=3, c=4) == "x1 = 4.00, x2 = -1.00"
    assert quadratic_equation(a=1, b=0, c=1) == "No solution!"


def test_quadratic_equation_with_invalid_input():
    with pytest.raises(ValueError, match="Invalid input!"):
        assert quadratic_equation(a="1", b=-3, c=2)
