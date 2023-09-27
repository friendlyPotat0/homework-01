import math

# This program calculates the perimeter of a right-angled triangle when given its base and height

base = float(input("Enter triangle base: "))
height = float(input("Enter triangle height: "))
# area: (base*height)/2
area = (base * height) / 2
# hypotenuse: sqrt(base**2+height**2)
# perimeter: hypotenuse+2*base
hypotenuse = math.sqrt(base ** 2 + height ** 2)
perimeter = base + height + hypotenuse

print()
print("%s%f" %("Triangle area: ", area))
print("%s%f" %("Triangle perimeter: ", perimeter))
