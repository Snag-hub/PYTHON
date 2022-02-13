# Write a python script to create a class Rectangle with data member’s length, width and methods area, perimeter which can compute the area and perimeter of rectangle.


class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length*self.width


newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())
