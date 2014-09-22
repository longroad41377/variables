import math

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * radius * math.pi
area = math.pi * radius**2

print("The curcumference of the circle is {:.2f}".format(circumference))
print("The area of the circle is {:.2f}".format(area))
