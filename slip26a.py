# Write an anonymous function to find area of square and rectangle.

def areaofsquare(a):
    return lambda: a*a

def areaofrectangle(a, b):
    return lambda: a*b

#call an anonymous function
print("Area of square: ", areaofsquare(5))
print("Area of rectangle: ", areaofrectangle(5, 6))


