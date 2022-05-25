class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        area = self.height * self.width
        return f"The area is {area}"

    def get_perimeter(self):
        perimeter = 2 * (self.height + self.width)
        return f"The perimeter is {perimeter}"

    def __repr__(self):
        return f"Info(area={self.get_area()},perimeter={self.get_perimeter()})"

    def __str__(self):
        return f"{self.get_area()} and {self.get_perimeter()}"


if __name__ == "__main__":
    rect = Rectangle(5, 8)
    print(rect)
    print(rect.get_area())

