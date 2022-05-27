import json


car_date = {
    "make": "Tesla",
    "type": "Electric",
    "faults": 9384,
    "death_trap": True,
    "driver": None
}

# print(car_date["faults"])

# dumps = json.dumps(car_date)
#
# print(dumps, type(dumps))
#
# with open('tesla.json', 'w') as jsonfile:
#     json.dump(car_date, jsonfile)

with open("spartan.json") as jsonfile:
    spartan = json.load(jsonfile)

print(spartan, (type(spartan)))

