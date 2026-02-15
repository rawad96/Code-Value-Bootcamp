"""
Demo - Decorator Order Matters
"""


def uppercase_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


def greet_decorator(func):
    def wrapper():
        return f"Greeting: {func()}"
    return wrapper


@uppercase_decorator
@greet_decorator
def get_text():
    return 'hello'


print(get_text())
