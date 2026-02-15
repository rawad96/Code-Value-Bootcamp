import __main__


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    conversion_units = ["C", "F", "K"]
    if from_unit not in conversion_units or to_unit not in conversion_units:
        raise ValueError("Invalid unit")
    elif from_unit == "K" and value < 0:
        raise ValueError("Temperature below absolute zero")
    elif(from_unit == to_unit):
        return value
    elif(from_unit == "C" and to_unit == "F"):
        return (value * 9/5) + 32
    elif(from_unit == "F" and to_unit == "C"):
        return (value - 32) * 5/9
    elif(from_unit == "C" and to_unit == "K"):
        return value + 273.15
    elif(from_unit == "K" and to_unit == "C"):
        return value - 273.15

    
if __name__ == "__main__":
    print(f'{convert_temperature(value=0, from_unit="C", to_unit="F")}')
    print(f'{convert_temperature(value=100, from_unit="C", to_unit="K")}')
    print(f'{convert_temperature(value=32, from_unit="F", to_unit="C")}')
    print(f'{convert_temperature(value=0, from_unit="K", to_unit="C")}')
    print(f'{convert_temperature(value=0, from_unit="E", to_unit="C")}')

