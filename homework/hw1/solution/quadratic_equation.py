import math


def quadratic_equation(a: int, b: int, c: int) -> str:
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise ValueError("Invalid input!")
    negative_b = -b
    radicand = b**2 - 4 * a * c
    if radicand < 0:
        return "No solution!"
    sqrt = math.sqrt(radicand)
    denominator = 2 * a

    x1 = (negative_b - sqrt) / denominator
    x2 = (negative_b + sqrt) / denominator

    return f"x1 = {x1:.2f}, x2 = {x2:.2f}"


if __name__ == "__main__":
    print(quadratic_equation(a=-1, b=3, c=4))
