"""
Demo - Arbitrary Arguments and Keyword Arguments
"""
from typing import Any


def calculate_average(*numbers: int) -> float:
    return sum(numbers) / len(numbers)


def log_all_arguments(*args) -> None:
    for argument in args:
        print(argument)


def configure(**kwargs) -> None:
    for key, value in options.items():
        print(f"{key} set to {value}")


if __name__ == '__main__':
    # log_all_arguments('ilya', 'adam', 'sara', 'bhaa', 34)
    configure({
        'ip': '1.1.1.1',
        'ilya': 'ilya',
        'somthing_else': 2
    })


