# Write python script using package to calculate area and volume of cube and sphere

import math

radius = float(input('Enter radius of sphere: '))
l = float(input('Please Enter the Length of any Side of a Cube: '))
# sphere
area = 4 * math.pi * radius ** 2
volume = (4/3) * math.pi * radius**3
# cube
sa = 6 * (l * l)
Volume = l * l * l

print('Area = %0.4f.' % (area))
print('Volume = %0.4f.' % (volume))

print("\n Surface Area of Cube = %.2f" % sa)
print(" Volume of cube = %.2f" % Volume)
