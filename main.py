# Based on its radius, we are going to do calculations of a sphere which include its diameter, circumference, surface area, and volume:

from math import pi

# Input the radius of a sphere (floating point number)
radiusString = input("What is the radius of a sphere? ")
radius = float(radiusString)

# First, compute the diameter of the sphere using the formula:
# Diameter = radius * 2
diameter = radius * 2

# Second, compute the circumference of the sphere using the formula:
# Circumference = Diameter * π	(pi; approx. 3.1416)
circumference = diameter * pi

# Third, compute the surface area of the sphere using the formula:
# Surface area = 4 * π * (radius squared)	(r2)
surfaceArea = 4 * pi * (radius ** 2)

# Lastly, compute the volume of the sphere using the formula:
# Volume = (4/3) * π * (radius cubed)	(r3)
volume = (4/3) * pi * (radius ** 3)

# Print the diameter, circumference, surface area, and volume
print("The sphere's diameter is " + str(diameter) + ".")
print("The sphere's circumference is " + str(circumference) + ".")
print("The sphere's surface area is " + str(surfaceArea) + ".")
print("The sphere's volume is " + str(volume) + ".")