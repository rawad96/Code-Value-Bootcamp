import sys

integer_number = int(input("please enter a number: "))

print(f'The number is: {integer_number}')
print(f'The type of the number is: {type(integer_number)}')
print(f'The size of the number in bytes is: {sys.getsizeof(integer_number)}')



print(f'The number squared is: {integer_number ** 2}')
print(f'The number as a float is: {float(integer_number)}')
print(f'The number as a string is: {str(integer_number)}')
print(f'Is the number greater than 0? {integer_number > 0}')