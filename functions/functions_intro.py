# print()
# input()
# type()


# DRY - DON'T REPEAT YOURSELF

# Function definition
# def greeting(name="...you!"):
#     return "Hello " + name
#     print("This will never run")
#
# print(greeting())
# print(greeting("David"))

# Call the function
# greeting("Konrad")
# name = "Konrad"
# print ("Hello " + name)
# greeting("Harry")
# greeting("Dan")

# result = greeting("David")
# print(result)
#
# greeting("a")

# def add_plus_one(int1, int2):
#     return int1 + int2
#
# print(add_plus_one(4, 6))

# print("one", "two", 54345, {})
#
# def multiargs(*args):
#     print(args, type(args))
#     for arg in args:
#         print(arg)
#
# multiargs(1, 2, 3)

# Define the function 'product'
# It should accept any number of arguments
# And return the result from multiplying them all together

# def product(*nums):
#     # print(nums, type(nums))
#     result = 1
#     if len(nums) == 0:
#         return None
#     for num in nums:
#         result *= num
#     return result
#
#
# print(product(1, 2, 3))
# print(product())

# If product is called with no arguments, return None

# def kwargs_demo(**kwargs):
#     print(kwargs, type(kwargs))
#
#
# print(kwargs_demo(a="one", b="two"))

def calculate_tip(list_of_meals, total_cost, tip_pc):
    """ Prints a list of meals followed by info on total with and without tip. """
    print("You had:")
    for meal in list_of_meals:
        print(f"- {meal}")
    print(f"Your total is: {total_cost:.2f}")
    print(f"With a {tip_pc:.0%} tip, the total is {total_cost * (1 + tip_pc):.2f}")


calculate_tip(
    list_of_meals=["Pizza", "Burger", "Hot Dog"],
    tip_pc=0.15,
    total_cost=24
)
#
#
# def calculate_total_cost(**meal_price):
#     return sum(meal_price.values())
#
#
# print(calculate_total_cost(
#     pizza=8.50,
#     burger=9.00,
#     hotdog=9.20
# ))

# def greeting(name: str):
#     print("Hello " + name)
#
#
# greeting("Harry")
#
#
# def division(denom: int, num: int) -> float:
#     return denom / num
#
#
# a = division(12, 6)

# Good Functions
# - Name them clearly, lowercase_with_underscores
# - Use clear argument names
# - Functions that don't RETURN something return None
# - Keep them small
# - Use comments
# - Consider type hints

# def fizzbuzz_line(num: int):
#     if num % 15 == 0:
#         return "FizzBuzz"
#     if num % 5 == 0:
#         return "Buzz"
#     if num % 3 == 0:
#         return "Fizz"
#     return str(num)
#
#
# def fizzbuzz_game():
#     for i in range(1, 101):
#         print(fizzbuzz_line(i))
#
# fizzbuzz_game()

# Package fizzbuzz into functions