def binary_to_decimal(binary_string: str) -> int:
    if len(binary_string) < 2:
        raise ValueError("Binary string must contain at least 2 digits")
    for digit in binary_string:
        if int(digit) > 1 or int(digit) < 0:
            raise ValueError("Digits must be 0 or 1")
    return int(binary_string, 2)


if __name__ == "__main__":
    print(binary_to_decimal("0101"))
