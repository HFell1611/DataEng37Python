# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
#     print("There has not been found")
#     print(errmsg)
#     raise
#
# print(file, type(file))
# #orders = file.readlines()

# with open("order.txt") as file:
#     raw_orders = file.readlines()
#     orders = map(lambda x: x.replace("\n", ""), raw_orders)
#
# print(file.closed)

# print(list(orders))


# file.close()

# What if we want our order without the new line chars


# with open("order.txt") as file:
#     orders = file.read().split('\n')
#
# print(orders, type(orders))
# # orders_list = orders.split('\n')
# # print(orders_list)
# print(file)

colours = ["red\n", "yellow\n", "green\n"]

with open("order.txt", "a") as file:
    file.write("New string to write\n")
    file.writelines(colours)

# Create a drinks menu text file
# Create a drinks orders text file
# Write a function that will take in a drink order
# If that order exists in the menu, write it to the orders
# Otherwise, raise an error
