"""
Demo - Decorators
"""
from functools import wraps


def log_function_params(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"function {func.__name__} is called with "
              f"arguments {args} and kw arguments {kwargs}")
        _result = func(*args, **kwargs)
        print(f'result is {_result}')
        return _result

    return wrapper


def repeat(times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            inner_result = None
            for _ in range(times):
                inner_result = func(*args, **kwargs)
            return inner_result
        return wrapper
    return decorator_repeat


@log_function_params
def add(a: int, b: int) -> int:
    print('I am here')
    return a + b


if __name__ == '__main__':
    result = add(1,2)
    print(result)
    print(add.__name__)
