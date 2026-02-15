from solution.count_calls_decorator import greet

def test_count_calls_decorator():
    assert greet.call_count == 0
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"

    assert greet.call_count == 2