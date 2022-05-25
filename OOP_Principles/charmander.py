from pokemon import Pokemon
from move import Move


class Charmander(Pokemon):
    def __init__(self):
        super().__init__(
            "Charmander",
            "Fire",
            hp=15,
            attack=9,
            defense=5
        )
        self.moves.append(Move("Scratch", "Normal", 10))
        self.moves.append(Move("Growl", "Normal", 0))


class Pikachu(Pokemon):
    def __init__(self):
        super().__init__(
            "Pikachu",
            "Electric",
            hp=6,
            attack=6,
            defense=6
        )
        self.moves.append(Move("Thundershock", "Electric", 20))
        self.moves.append(Move("Tail Whip", "Normal", 0))


if __name__ == "__main__":
    char = Charmander()
    # print(char.type)
    # print(char.attack)
    # for move in char.moves:
    #     print(f"{move.name} ({move.type}): {move.power}")

    # result = char.use_move("Scratch")
    # print(result, type(result))
    # power, move_type = char.use_move("Scratch")
    # print(power, type(power))
    # print(move_type, type(move_type))
    print(char.moves)
    for move in char.moves:
        print(move)
