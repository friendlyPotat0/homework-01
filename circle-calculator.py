import math

# This program calculates the area and perimeter of a circle

radius = float(input("Enter circle radius: "))
# area: pi*radius^2
area = math.pi * (radius)**2
# perimeter: 2*pi*radius
perimeter = 2 * math.pi * radius

print()
print("%s%f" %("Circle area: ", area))
print("%s%f" %("Circle perimeter: ", perimeter))
