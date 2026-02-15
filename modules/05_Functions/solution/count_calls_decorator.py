from functools import wraps

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Alice"))  # Output: "Hello, Alice!"
    print(greet("Bob"))    # Output: "Hello, Bob!"
    print(f'the number of calls to {greet.__name__} is {greet.call_count}')  # Output: 2
