class Budget:
    def __init__(self):
        self.food = 0
        self.clothing = 0
        self.entertainment = 0

    def add_food(self, food_add):
        self.food += food_add

    def sub_food(self, food_sub):
        self.food -= food_sub

    def add_clothing(self, clothing_add):
        self.clothing += clothing_add

    def sub_clothing(self, clothing_sub):
        self.clothing -= clothing_sub

    def add_entertainment(self, entertainment_add):
        self.entertainment += entertainment_add

    def sub_entertainment(self, entertainment_sub):
        self.entertainment -= entertainment_sub



