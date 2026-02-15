def calculate_statistics(**kwargs) -> dict:
    statistics = {}
    for key, value in kwargs.items():
        if(not all(isinstance(number, (int, float)) for number in value)):
            raise ValueError(f"Value for {key} must be a number")
        if(len(value) == 0):
            statistics[key] = None
        if key not in statistics:
            statistics[key] = {
                'sum': sum(value),
                'average': sum(value) / len(value),
                'min': min(value),
                'max': max(value)
            }
        else:
            continue
    return statistics

if __name__ == '__main__':
    result = calculate_statistics(
        temperatures=[22.5, 24.0, 23.5, 25.0],
        humidity=[60, 65, 62, 68]
    )
    print(result)