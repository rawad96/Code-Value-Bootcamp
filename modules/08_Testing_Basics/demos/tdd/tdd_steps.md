# TDD ( Test Driven Developemnt ) Steps 

1. Define the interface of the function you want to implement. In our case, it is `fibonacci(n: int) -> int`.
2. At first the function should raise `NotImplementedError` to indicate that it is not implemented yet.
3. Write a test for the function. The test should check the expected behavior of the function. For example, we can check that `fibonacci(0) == 0`, `fibonacci(1) == 1`, `fibonacci(2) == 1`, `fibonacci(3) == 2`, and so on. You may write all the tests, including edge cases.
4. Run `pytest` and that the test fails.
5. Implement the function to make the test pass.
