num = input("Please enter a number:\n")
check = input("What do you want to divide by?\n")

num_int = int(num)
check_int = int(check)

# if num_int % 4 == 0:
#     print("Number is a multiple of 4")
# elif num_int % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

if num_int % check_int == 0:
    print(f"{num_int} is divisible by {check_int}")
else:
    print(f"{num_int} is not divisible by {check_int}")
