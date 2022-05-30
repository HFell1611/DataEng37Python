def fibonacci():
    num = int(input("How many numbers do you want to generate?:\n"))
    i = 0
    fib = [1, 1]
    while i < (num - 1):
        fib.append(fib[i] + fib[i - 1])
        i += 1


print(fibonacci())