# LEGB

# Local - in a function
# Enclosed - in a function in a function
# Global - anywhere
# Built-In - comes in python
"""Local
x = 10

l = lambda x: x * 2

print(l(2))
print(x * 2)
"""

"""Enclosed
x = 5


def outer(x):
    def inner():
        print(x)
    inner()


outer("hello")


def fizzbuzz():
    while True:
        n = input("End Number?\n")
        if n.isdigit():
            n = int(n)
            break

    def fizzbuzz_run():
        for i in range(1, n + 1):
            if i % 15 == 0:
                print("FizzBuzz")
            else:
                print(i)
    fizzbuzz_run()


fizzbuzz()
"""

glob = "This is in the global scope"


def local_function():
    def inner_function():
        print(__name__)
    inner_function()


def type(x):
    return "I dunno, probably a string"


print(type(5))
