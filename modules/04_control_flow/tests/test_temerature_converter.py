from solution.temperature_converter import convert_temperature
import pytest

def test_convert_temperature():
    assert convert_temperature(value=0, from_unit="C", to_unit="F") == 32
    assert convert_temperature(value=100, from_unit="C", to_unit="K") == 373.15
    assert convert_temperature(value=32, from_unit="F", to_unit="C") == 0
    assert convert_temperature(value=0, from_unit="K", to_unit="C") == -273.15

def test_invalid_conversion():
    with pytest.raises(ValueError, match="Invalid unit"):
        convert_temperature(value=100, from_unit="E", to_unit="C")

def test_kelvine_under_0():
    with pytest.raises(ValueError, match="Temperature below absolute zero"):
        convert_temperature(value=-100, from_unit="K", to_unit="C")
        