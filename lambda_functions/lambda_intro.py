def add_plus_one(num1, num2):
    return num1 + num2 + 1


print(add_plus_one(3, 7))

# Lambda (or anonymous) functions

addition = lambda num1, num2: num1 + num2 + 1

print(addition(5, 8))

# map

savings = [234.00, 555.00, 647.25, 839.00]
# bonus = savings with 10% added on
bonus = []
for saving in savings:
    bonus.append(saving * 1.1)
print(bonus)


def apply_bonus(saving):
    return saving * 1.1


bonus_map = list(map(apply_bonus, savings))
print(bonus_map)

bonus_lambda = list(map(lambda x: x * 1.1, savings))
print(bonus_lambda)
squared_bonus = map(lambda x: x ** 2, bonus_lambda)
print(list(squared_bonus))

# total = sum(bonus_lambda)
# print(total)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use map and lambda to create a list of each number squared plus 3

alt_nums = list(map(lambda x: (x ** 2) + 3, numbers))
# print(alt_nums)
evens = filter(lambda x: x % 2 == 0, alt_nums)
print(list(evens))

jobs = ["Data Analyst", "C# Developer", "Data Engineer", "DevOps Engineer", "Data Architect"]
# Using map and filter with lambdas
# Produce a list of the data-based roles without the word data in there

keep_data = filter(lambda x: "Data" in x, jobs)
# print(list(keep_data))

#no_data = map(lambda x:  x[5:], keep_data)
no_data = map(lambda x:  x.replace("Data ", ""), keep_data)
print(list(no_data))
