temperature_in_celsius = input("please enter a temperature in Celsius:")
temperature_in_float = float(temperature_in_celsius)
temeperature_in_fahrenheit = (temperature_in_float * 9/5) + 32
temperature_in_Kelvin = temperature_in_float + 273.15

print(f'The temperature in Celsius is: {temperature_in_float}')
print(f'The temperature in Fahrenheit is: {temeperature_in_fahrenheit}')
print(f'The temperature in Kelvin is: {temperature_in_Kelvin}')
