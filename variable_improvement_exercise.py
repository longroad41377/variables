import math

radius = float(input("please enter the radius of the circle: "))

circumference = 2.0 * math.pi * radius

area = math.pi * radius**2

print("The circumference of this circle is {0:.2f}.".format(circumference))
print("The area of this circle is {0:.2f}.".format(area))
