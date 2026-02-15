"""
Demo - Lambda Expressions
"""
from time import sleep
from typing import Callable


def square(a):
    return a * a


my_list = [1,2,3,4,5]
map_object = map(square, my_list)
squares = list(map_object)

print(map_object)
print(squares)


def sleep_and_call(seconds: int, callback: Callable) -> None:
    sleep(seconds)
    callback()


sleep_and_call(5, lambda: print('Hello'))