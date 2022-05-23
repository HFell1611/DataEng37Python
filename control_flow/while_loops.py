# x = 0
#
# while x < 10:
#     print(f"While loop running: {x + 1}")
#     if x == 4:
#         print("Yay! 5!")
#         break
#     x += 1
#
# print("While loop finished")

keep_asking = True

while keep_asking:
    age = input("Whats is your age?\n")
    if age.isdigit():
        age_int = int(age)
        keep_asking = False
    else:
        print("Please enter a valid number in digits")

print(f"Your age is {age_int}")
