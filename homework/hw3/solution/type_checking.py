from functools import wraps
from typing import Any, Optional

SUPPORTED_TYPES = (int, float, str, list, dict, bool, type(None))


def check_isinstance(value: Any, name: str, expected_type: Any) -> None:
    if expected_type not in SUPPORTED_TYPES:
        return
    if not isinstance(value, expected_type):
        raise TypeError(
            f"Argument '{name}' must be of type {expected_type.__name__}, "
            f"but got {type(value).__name__}"
        )


def check_arguments(func: Any, args: tuple, kwargs: dict) -> None:
    annotations = func.__annotations__
    for name, type in annotations.items():
        if name == "return":
            continue  # co_varnames does not include 'return'
        if name in kwargs:
            value = kwargs.get(name)
        else:
            varnames_list = list(func.__code__.co_varnames)
            arg_index = varnames_list.index(name)
            if arg_index < len(args):
                value = args[arg_index]
            else:
                continue

        check_isinstance(value, name, type)


def check_types_decorator(func: Any) -> Any:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        check_arguments(func, args, kwargs)
        return func(*args, **kwargs)

    return wrapper


@check_types_decorator
def format_data(
    name: str, age: int, data: dict, other_info: Optional[Any] = None
) -> str:
    if other_info:
        other_info_str = ", Other Info : "
        other_info_str += str(other_info)
    else:
        other_info_str = ""
    return f"Name: {name}, Age: {age}, Data: {data['key']}{other_info_str}"


AGE_FOR_TESTING1 = 30
AGE_FOR_TESTING2 = 25

if __name__ == "__main__":
    print(
        format_data(
            "Alice", AGE_FOR_TESTING1, {"key": "value"}, other_info="Additional info"
        )
    )
    print(format_data("Bob", AGE_FOR_TESTING2, {"key": "another value"}))
