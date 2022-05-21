# alphabet = ["A", "B", "C", "D", "E"]
#
# for letter in alphabet:
#     print("The next letter is: ")
#     print(letter.lower())
#     if letter == "D":
#         print("Get out")
#     else:
#         print("Hooray!")

# letter = alphabet[0]
# print(letter.lower())


# nest = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
#
# for sublist in nest:
#     print(sublist)
#     for number in sublist:
#         print(number)
#
# #
#
# hi = "Hello World!"
#
# print(hi)
# for c in hi:
#     print(c)

game = {
    "name": "Borderlands 2",
    "platform": {
        "PC": True,
        "X-Box": True,
        "PlayStation": True,
        "Nintendo": False
    },
    "rating": {
        "IGN": 9,
        "Metacritic": 89
    },
    "released": "18/09/12"
}

# for g in game["platform"]:  # Take the first thing in game as g, then do something to it
#     print(g)
#
#
# for key, value in game.items():
# print(f"The {key} is {value}")

#

for i in range(5):
    print(f"This is line number: {i + 1}")

for i, key in enumerate(game):
    print(f"Key number {i + 1} is {key}")
