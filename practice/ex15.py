def rev(x):
    y = x.split()
    y.reverse()
    return " ".join(y)


print(rev(input("Please enter a sentence:\n")))
