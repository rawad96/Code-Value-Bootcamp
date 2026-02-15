def add_subtract_multiply_operators(
    operator: str, firs_number: int, second_number: int
) -> int:
    if operator == "add":
        return firs_number + second_number
    elif operator == "subtract":
        return second_number - firs_number
    elif operator == "multiply":
        return firs_number * second_number
    raise ValueError(
        "Invalid operator!!\nValid operators are: add, subtract, divide and multiply."
    )


def divide_operator(firs_number: int, second_number: int) -> float:
    if second_number == 0:
        raise ZeroDivisionError("Can't devide by zero!!")
    return firs_number / second_number


def print_help_instructions() -> None:
    help_message = """
Welcome to the calculator! 
You can type operations in the following form.
Examples:

  - "add 2 to 5"
  - "subtract 2 from 5"
  - "multiply 2 by 5"
  - "divide 10 by 5"

Other commands:

  - "help"               → Show this help message
  - "exit"               → Exit the calculator
"""
    print(help_message)


def extract_and_calculate(expression: str) -> str:
    extract_operator_and_numbers = expression.split(" ")
    operator = extract_operator_and_numbers[0]
    if operator == "divide":
        try:
            answer = divide_operator(
                firs_number=int(extract_operator_and_numbers[1]),
                second_number=int(extract_operator_and_numbers[3]),
            )
        except ValueError:
            print("Invalid Numbers!!!")
            return "Invalid Numbers!!!"
        except ZeroDivisionError as error:
            print(error)
            return "Can't devide by zero!!"
        print(f"The answer is {answer}")
        return f"The answer is {answer}"
    else:
        try:
            answer = add_subtract_multiply_operators(
                operator=extract_operator_and_numbers[0],
                firs_number=int(extract_operator_and_numbers[1]),
                second_number=int(extract_operator_and_numbers[3]),
            )
        except ValueError as error:
            print(error)
            return ""
        print(f"The answer is {answer}")
        return f"The answer is {answer}"


def calculator() -> None:
    while True:
        input_expression = input(
            "Please enter an operation in the following way: (e.g., add 5 to 2, divide 4 by 2) --- for exit write exit, for help write help: "
        )
        if input_expression == "exit":
            break
        elif input_expression == "help":
            print_help_instructions()
            continue
        extract_and_calculate(input_expression)


if __name__ == "__main__":
    calculator()
