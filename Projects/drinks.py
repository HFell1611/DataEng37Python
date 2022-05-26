def orders():
    with open("drinks_menu.txt") as drinks:
        drinks_list = drinks.read().split('\n')
        order = input("What would you like to order?\n")
        if order.lower() in drinks_list:
            with open("drinks_orders.txt", "w") as drink_orders:
                drink_orders.write(order)
        else:
            return "Drink not on menu"


orders()
