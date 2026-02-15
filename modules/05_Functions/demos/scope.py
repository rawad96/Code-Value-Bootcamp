"""
Demo - Function Scope
"""


CONSTANT = 1
x = "i am global"


def foo():
    y = "i am local to foo"
    global x
    x = "Do not use global variables!"

    def helper_function():
        z = "i am local to inner"
        nonlocal y
        y = "I don't feel so good"

        print("i am inner function ")
        print(x)

    helper_function()
    print(y)
    return helper_function


helper = foo()
print(type(helper))
helper()
