class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_area(self):
        return self.length * self.width

rectangle_1 = Rectangle(5, 3)
rectangle_2 = Rectangle(10, 4)
print("Rectangle 1 perimeter:", rectangle_1.calculate_perimeter())
print("Rectangle 1 area:", rectangle_1.calculate_area())

print("Rectangle 2 perimeter:", rectangle_2.calculate_perimeter())
print("Rectangle 2 area:", rectangle_2.calculate_area())