string = str(input("Enter a word:\n"))
reverse = string[::-1]

if string == reverse:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")

