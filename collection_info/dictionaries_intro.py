# Dictionaries

# data_eng_37 = {
#     "course_name": "Data Engineering 37",
#     "client": "Home Office",
#     "trainer": {
#         "name": "David Harvey",
#         "energy_levels": "low"
#     }
# }
#
# print(data_eng_37, type(data_eng_37))
#
# print(data_eng_37["client"])  # DICTIONARY NAME [ KEY ]
#
# data_eng_37["trainees"] = ["Munir", "Darnell", "Abhi", "Ahmed"]
#
# print(data_eng_37)
#
# print(data_eng_37["trainer"]["energy_levels"])

# print(data_eng_37.get("missing_key"))  # Return None
# print(data_eng_37["missing_key"])  # Fail noisily with error

# print(bool(data_eng_37.get("is this key here")))
# data_eng_37.update({"course_length": "8 weeks"})
# print(data_eng_37)

# Create a dictionary on favorite game


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

# print(game["rating"]["IGN"])
# print(game.get("missing_key"))
game.update({"playtime": "1500 Hours"})
# print(game)
#
# print(game.keys())  # returns as list
# print(game.values())  # returns as list
# print(game.items())  # returns as tuple
#
# print(game["rating"]["IGN"])

print(f"Harry's favourite game is {game['name']} ({game['released']}). He has played it for {game['playtime']} and is rated {game['rating']}")
