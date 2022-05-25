class Pokemon:
    def __init__(self, name, type, hp, attack, defense):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self. lvl = 1
        self.moves = []

    def receive_attack(self, power, is_supper_effective=False):
        if is_supper_effective:
            self.hp -= (power - self.defense) * 2
        else:
            self.hp -= (power - self.defense)

    def lvl_up(self, levels=1):
        self.lvl += levels
        self.hp += levels * 3
        self.attack += levels * 2
        self.defense += levels

    def use_move(self, move_name) -> (int, str):
        # Pseudocode
        # Iterate through the moveset
        for move in self.moves:
            # Check if move_name matches the move name
            if move_name == move.name:
                # If so, use the move
                print(f"{self.name} used {move.name}!")
                return move.power + self.attack, move.type
        # Otherwise keep going
