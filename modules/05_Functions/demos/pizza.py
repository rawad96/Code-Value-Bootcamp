from typing import Callable
from pprint import pprint


def logging_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f'The args are {args}')
        result = func(*args, **kwargs)
        print(f'Result is {result}')
        return result
    return wrapper


@logging_decorator
def add(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    result = add(2, 2)
    pprint(globals())
