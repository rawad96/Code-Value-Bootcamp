def generate_pyramid(height: int) -> str:
    if(height <= 0):
        raise ValueError("Height must be at least 1.")
    elif(height > 9):
        raise ValueError("Height cannot exceed 9.")
    else:
        pyramid = ""
        for i in range(1, height + 1):
            spaces = ' ' * (height - i)
            ascending = ""
            descending = ""
            for up in range(1, i + 1):
                ascending += str(up)
            for down in range(i - 1, 0, -1):
                descending += str(down)
            pyramid += spaces + ascending + descending + "\n"
    return pyramid


if __name__ == "__main__":
    print(generate_pyramid(5))