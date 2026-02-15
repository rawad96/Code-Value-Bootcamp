rectangle_width = input("PLease enter the width of the rectangle: ")
rectangle_height = input("PLease enter the height of the rectangle: ")

rectangle_width = float(rectangle_width)
rectangle_height = float(rectangle_height)

rectangle_area = rectangle_width * rectangle_height
rectangle_perimeter = 2 * (rectangle_width + rectangle_height)
rectangle_diagonal = (rectangle_width**2 + rectangle_height**2)**0.5

print(f'The area of the rectangle is: {rectangle_area}')
print(f'The perimeter of the rectangle is: {rectangle_perimeter}')
print(f'The diagonal of the rectangle is: {rectangle_diagonal}')