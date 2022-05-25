
def fizzbuzz_line(x: int):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x


def fizzbuzz_game():
    for i in range(1, num_int + 1):
        print(fizzbuzz_line(i))


check_num = True
while check_num:
    num = input("Please select a number\n")
    if num.isdigit():
        num_int = int(num)
        check_num = False
        fizzbuzz_game()
    else:
        print("Please enter a valid number")


