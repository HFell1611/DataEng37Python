def prime(num):
    for i in range(2, num - 1):
        if num % i != 0:
            continue
        elif num % i == 0:
            return f"{num} is not prime"
    return f"{num} is a prime"


print(prime(int(input("Please enter a number:\n"))))
