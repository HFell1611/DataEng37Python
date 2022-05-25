class Move:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

    def __repr__(self):
        return f"Move(name={self.name},type={self.type},power={self.power})"

    def __str__(self):
        return f"{self.name} ({self.type}: {self.power})"


if __name__ == "__main__":
    flamethrower = Move(
        "Flamethrower",
        "Fire",
        power=10
    )

    print(flamethrower)
    print(type(flamethrower))
    print(flamethrower.power)
