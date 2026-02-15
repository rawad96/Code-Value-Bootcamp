from solution.calculate_statistics import calculate_statistics
import pytest

def test_calculate_statistics():
    calculate_statistics_result = calculate_statistics(
        temperatures=[22.5, 24.0, 23.5, 25.0],
        humidity=[60, 65, 62, 68]
    )
    expected_result = {
        'temperatures': {'sum': 95.0, 'average': 23.75, 'min': 22.5, 'max': 25.0}, 'humidity': {'sum': 255, 'average': 63.75, 'min': 60, 'max': 68}
    }
    assert calculate_statistics_result == expected_result

def test_calculate_statistics_with_non_numeric_value():
    with pytest.raises(ValueError, match="Value for temperatures must be a number"):
        calculate_statistics(
            temperatures=[22.5, 24.0, '23.5', 25.0],
            humidity=[60, 65, 62, 68]
        )

def test_calculate_statistics_with_empty_list():
    calculate_statistics_result = calculate_statistics(
        temperatures=[],
        humidity=[60, 65, 62, 68]
    )
    expected_result = {
        'temperatures': None, 'humidity': {'sum': 255, 'average': 63.75, 'min': 60, 'max': 68}
    }
    assert calculate_statistics_result == expected_result