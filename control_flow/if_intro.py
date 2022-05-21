# age = 16
# has_ticket = True
#
# if age >= 16 and has_ticket:
#     print("You can watch this film")
# elif age < 16 and has_ticket:
#     print("You are too young to watch this film")
# else:
#     print("You need to be at least 16 and have a ticket")
#
# print("This will always run")

# film_rating = "U"
# U, PG, 12/12A, 15, 18
#
# if film_rating.upper() == "U":
#     print("Can be watched by anyone")
# elif film_rating.upper() == "PG":
#     print("Parental guidance is advised for younger viewers")
# elif film_rating == "12" or film_rating.lower() == "12a":
#     print("You have to be at least 12 to watch this film")
# elif film_rating == "15":
#     print("You have to be at least 15 to watch this film")
# elif film_rating == "18":
#     print("You have to be at least 18 to watch this film")
# else:
#     print("Invalid film rating")

age = 17
has_ticket = True

if has_ticket:
    if age >= 15:
        print("You can see this film")
    else:
        print("Come back when you're older punk")
else:
    print("You need a ticket - go buy one!")