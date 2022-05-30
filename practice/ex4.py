num = input("Please enter a number:\n")
num_int = int(num)
div = 2
divisors = []

while div < num_int:
    if num_int % div == 0:
        divisors.append(div)
    div += 1

print(divisors)
