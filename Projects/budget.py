class Budget:
    def __init__(self):
        self.food = 0
        self.clothing = 0
        self.entertainment = 0

    def add_funds(self, category, funds_add):
        if category.lower() == "food":
            self.food += funds_add
            return self.food
        elif category.lower() == "clothing":
            self.clothing += funds_add
        elif category.lower() == "entertainment":
            self.entertainment += funds_add
        else:
            return "Invalid category"

    def sub_funds(self, category, funds_sub):
        if category.lower() == "food":
            self.food -= funds_sub
        elif category.lower() == "clothing":
            self.clothing -= funds_sub
        elif category.lower() == "entertainment":
            self.entertainment -= funds_sub
        else:
            return "Invalid category"

    def move_funds(self, category1, category2, funds):
        # Food check
        if category1.lower() == "food":
            if self.food - funds <= 0:
                return "Funds will be below 0"
            self.food -= funds
            if category2.lower() == "clothing":
                self.clothing += funds
            elif category2.lower() == "entertainment":
                self.entertainment += funds
            else:
                return "Invalid category 2"
        # Clothing check
        elif category1.lower() == "clothing":
            if self.clothing - funds <= 0:
                return "Funds will be below 0"
            self.clothing -= funds
            if category2.lower() == "food":
                self.food += funds
            elif category2.lower() == "entertainment":
                self.entertainment += funds
            else:
                return "Invalid category 2"
        # Entertainment check
        elif category1.lower() == "entertainment":
            if self.entertainment - funds <= 0:
                return "Funds will be below 0"
            self.entertainment -= funds
            if category2.lower() == "food":
                self.food += funds
            elif category2.lower() == "clothing":
                self.clothing += funds
            else:
                return "Invalid category 2"
        else:
            return "Invalid category 1"

    def __repr__(self):
        return f"Budget(food={self.food},clothing={self.clothing},entertainment={self.entertainment})"

    def __str__(self):
        return f"Food total = £{self.food}, Clothing total = £{self.clothing}," \
               f" Entertainment total = £{self.entertainment}"


if __name__ == "__main__":
    fund = Budget()
    print(fund.add_funds("food", 1000))
    fund.move_funds("food", "clothing", 500)
    print(fund)
