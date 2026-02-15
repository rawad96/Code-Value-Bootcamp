from solution.simple_calculator import extract_and_calculate


def test_extract_and_calculate() -> None:
    add_expression = "add 5 to 3"
    subtract_expression = "subtract 2 from 4"
    multiply_expression = "multiply 5 by 6"
    division_expression = "divide 4 by 2"

    assert extract_and_calculate(add_expression) == "The answer is 8"
    assert extract_and_calculate(subtract_expression) == "The answer is 2"
    assert extract_and_calculate(multiply_expression) == "The answer is 30"
    assert extract_and_calculate(division_expression) == "The answer is 2.0"


def test_extract_and_calculate_with_invalid_input() -> None:

    invalid_number = "divide one to 3"
    division_by_zero = "divide 4 by 0"

    assert extract_and_calculate(invalid_number) == "Invalid Numbers!!!"
    assert extract_and_calculate(division_by_zero) == "Can't devide by zero!!"
