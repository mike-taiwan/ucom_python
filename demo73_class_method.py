class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


r1 = Rectangle(3, 4)
r2 = Rectangle(5, 6)
print r1.width, r1.height, r1.calculate_area()
print r2.width, r2.height, r2.calculate_area()