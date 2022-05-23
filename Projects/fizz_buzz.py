# Fizz Buzz

check_input = True
check_num = True

while check_input:
    run = input("Which program do you want to run?: for/while\n")
    if run.lower() == "for":
        while check_num:
            num = input("What number do you want to run to?\n")
            if num.isdigit():
                num_int = int(num)
                for x in range(1, num_int + 1):
                    if x % 3 == 0 and x % 5 == 0:
                        print("FizzBuzz")
                    elif x % 3 == 0:
                        print("Fizz")
                    elif x % 5 == 0:
                        print("Buzz")
                    else:
                        print(x)
            else:
                print("Please enter a valid number")

    elif run.lower() == "while":
        while check_num:
            num = input("What number do you want to run to?\n")
            if num.isdigit():
                num_int = int(num)
                x = 1
                while x < num_int + 1:
                    if x % 3 == 0 and x % 5 == 0:
                        print("FizzBuzz")
                    elif x % 3 == 0:
                        print("Fizz")
                    elif x % 5 == 0:
                        print("Buzz")
                    else:
                        print(x)
                    x += 1
            else:
                print("Please enter a valid number")
    else:
        print("Please input either for or while.")
