from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self):
        super().__init__(
            width=8,
            height=8
        )

    def get_area(self):
        area = self.width ** 2
        return f"The area is {area}"

    def get_perimeter(self):
        perimeter = 4 * self.width
        return f"The perimeter is {perimeter}"

    def __repr__(self):
        return f"Info(area={self.get_area()},perimeter={self.get_perimeter()})"

    def __str__(self):
        return f"{self.get_area()} and {self.get_perimeter()}"


if __name__ == "__main__":
    square = Square()
    print(square.get_area())
    print(square.get_perimeter())
    print(square)
