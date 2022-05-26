from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, length):
        self.length = length
        super().__init__(
            length,
            length
        )


if __name__ == "__main__":
    square = Square(5)
    print(square.get_area())
    print(square.get_perimeter())
    print(square)
