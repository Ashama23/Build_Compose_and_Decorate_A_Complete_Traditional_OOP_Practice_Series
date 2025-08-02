from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

try:
    shape = Shape()
except TypeError as e:
    print(f"Error creating instance of Shape: {e}")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

my_rectangle = Rectangle(10, 5)
rectangle_area = my_rectangle.area()

print(f"The width of the rectangle is: {my_rectangle.width}")
print(f"The height of the rectangle is: {my_rectangle.height}")
print(f"The area of the rectangle is: {rectangle_area}")
print(f"\nIs Rectangle a subclass of Shape? {issubclass(Rectangle, Shape)}")