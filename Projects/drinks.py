def orders():
    with open("drinks_menu.txt") as drinks:
        drinks_list = drinks.read().split('\n')
        order = input("What would you like to order?\n")
        if order.lower() in drinks_list:
            with open("drinks_orders.txt", "a") as drink_orders:
                drink_orders.write(f"{order}\n")
            return f"Added {order} to orders"
        else:
            return "Drink not on menu"


print(orders())
