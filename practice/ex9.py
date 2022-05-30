import random

rand = random.randint(1, 9)
guess = 0
c = 0

while guess != rand and guess != "exit":
    guess = input("Enter a number between 1 and 9\n")

    if guess.lower() == "exit":
        print("Leaving game")
        break
    c += 1
    guess = int(guess)
    if guess < rand:
        print("Too low\n")
    elif guess > rand:
        print("Too high\n")
    else:
        print("Right!")
        print(f"It took you {c} guesses")
