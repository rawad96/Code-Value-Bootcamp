from functools import lru_cache

# I provided two solutions to this exercise: one with lru_cache and one without it.


@lru_cache(maxsize=None)
def fibonacci_calculator_with_cache(limit: int) -> int:
    if limit < 1:
        raise ValueError("Limit can't be less than 1!!!")
    if limit == 1:
        return 0
    if limit == 2:
        return 1
    return fibonacci_calculator_with_cache(limit - 1) + fibonacci_calculator_with_cache(
        limit - 2
    )


def fibonacci_calculator(limit: int, fibonacci_number: int = 0, start: int = 0) -> int:
    """
    Docstring for fibonacci_calculator

    :param limit: Description
    :type limit: int
    :param fibonacci_number: Description
    :type fibonacci_number: int
    :param start: Description
    :type start: int
    :return: Description
    :rtype: int

    The function calculates the limit Fibonacci number.
    """
    if limit < 1:
        raise ValueError("Limit can't be less than 1!!!")
    if limit == 1:
        return fibonacci_number
    if fibonacci_number == 0:
        return fibonacci_calculator(limit=limit - 1, fibonacci_number=1, start=0)
    prefix = fibonacci_number
    fibonacci_number += start
    return fibonacci_calculator(
        limit=limit - 1, fibonacci_number=fibonacci_number, start=prefix
    )


LIMIT_FOR_TESTING = 200

if __name__ == "__main__":
    print(fibonacci_calculator(limit=LIMIT_FOR_TESTING))
    print(fibonacci_calculator_with_cache(limit=LIMIT_FOR_TESTING))
