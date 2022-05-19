# h = "Hello World!"
#
# double = "Double Quotes"
# single = 'Single Quotes'
#
# print(double, single)
#
# #  failure = "I said "oh no!""
# double_in_single = 'I said "Oh No!"'
#
# both = 'I said "Oh No!" David\'s in trouble!'
# print(both)
#
# string_block = """
# Everything in here
# is part of the string
#
# Up until
# The last 3 quotes
# """
#
# print(string_block)

# STRING INDEXING AND SLICING

# h = "Hello World!"
#
# print(h[3:-4])
# print(h[7])
#
# print(h[:-4])
# print(h[3:])
#
# print(h[1:-1:3])
# print(h[4::2])
# print(h[::-1])

# Methods
# https://docs.python.org/3/library/stdtypes.html#string-methods
h = "Hello World!"
i = "      Hello World    "
k = "hello World. greetings. something else. yes"

# print(type(h))
# print(h.lower())
# print(h.upper())
# print(h.capitalize())
# print(i.strip())
# print(h.count('o'))
# print(h.replace('o', 'ooooo').capitalize())

# string_list = k.split(". ")
# print(string_list)
#
# new_sentence = ". ".join(string_list)
# print(new_sentence)


# Concatenation

a = "Mr"
b = "Blue"
c = "Sky"

print(a + ' ' + b + ' ' + c)

d = "Mambo"
e = "Number"
f = 5

# print(d + ' ' + e + ' ' + str(f))


# F-String (Formatted)

print(f"The next song is: {d} {e} {f}")

name = "Lassie"
years = 7
height = 60.2

print(f"{name.upper()} is {years * 7} yars old in dog years and {height:.0f} cm tall.")

score = 16
max_score = 26
print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:%}")
print(f"You scored {score/max_score:.2%}")