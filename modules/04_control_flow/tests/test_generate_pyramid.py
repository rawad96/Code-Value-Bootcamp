from solution.generate_pyramid import generate_pyramid
import pytest

def test_generate_pyramid():
    expected_for_height_4 = (
    "   1\n"
    "  121\n"
    " 12321\n"
    "1234321\n"
)
    assert generate_pyramid(4) == expected_for_height_4

def test_generate_pyramid_height_under_1():
    with pytest.raises(ValueError, match="Height must be at least 1."):
        generate_pyramid(0)

def test_generate_pyramid_height_over_9():
    with pytest.raises(ValueError, match="Height cannot exceed 9."):
        generate_pyramid(10)