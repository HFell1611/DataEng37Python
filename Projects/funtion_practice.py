print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1


# A1a:

list = []
def q1a(num: int):
    for i in range(1, num + 1):
        if num % i == 0:
            list.append(i)
    print(list)


q1a(12)


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function


# A1b:
def q1b(num1: int, num2: int):
    if num1 % num2 == 0 or num2 % num1 == 0:
        print("True")
    else:
        print("False")


q1b(8, 9)


# -------------------------------------------------------------------------------------- #


print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


# A2a:
def q2a(letter: str):
    print(alphabet.index(letter))


q2a("h")

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14


# A2b:
id_num = []


def q2b(name: str):
    full_id = ""
    for i in range(0, len(name)):
        char = name.lower()[i]
        str(id_num.append(alphabet.index(char)))
    for num in id_num:
        full_id += str(num)

    return full_id


print(q2b("Harry"))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)


# A2c:
id_num2 = []


def q2c(name: str):
    full_id2 = ""
    total_num = int()
    for i in range(0, len(name)):
        char = name.lower()[i]
        str(id_num2.append(alphabet.index(char)))
    for num in id_num2:
        full_id2 += str(num)
        total_num += num
    id2_int = int(full_id2)
    pw = id2_int - total_num

    return pw


print(q2c("Harry"))


# -------------------------------------------------------------------------------------- #


print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.


# A3a:
def q3a(num: int):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False


print(q3a(9))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit


# A3b:
def q3b(num: int):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False


print(q3b(2))

# -------------------------------------------------------------------------------------- #