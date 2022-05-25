class Square:
    def __init__(self, length):
        self.length = length

    def get_area(self):
        area = self.length ** 2
        return f"The area is {area}"

    def get_perimeter(self):
        perimeter = 4 * self.length
        return f"The perimeter is {perimeter}"

    def __repr__(self):
        return f"Info(area={self.get_area()},perimeter={self.get_perimeter()})"

    def __str__(self):
        return f"{self.get_area()} and {self.get_perimeter()}"


if __name__ == "__main__":
    square = Square(5)
    print(square)
    print(square.get_area())
