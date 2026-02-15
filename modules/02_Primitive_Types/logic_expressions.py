a = int(input("please enter the first number: "))
b = int(input("please enter the second number: "))
c = int(input("please enter the third number: "))

print(f'Is a equal to c? {a == c}')
print(f'Is a less than b? {a < b}')
print(f'Is b greater than or equal to a? {b >= a}')
print(f'Is a not equal to b? {a != b}')
print(f'Are both conditions true a < b and b > c? {a < b and b > c}')
print(f'Is at least one condition true a > b or a == c? {a > b or a == c}')
print(f'Is it not true that a equals b? {not (a == b)}')

first_string = input("please enter the first string: ")
second_string = input("please enter the second string: ")

print(f'Are the strings equal? {first_string == second_string}')
print(f'Are the strings equal when comparing lowercase versions? {first_string.lower() == second_string.lower()}')
print(f'What is the length of the first word? {len(first_string)}')



