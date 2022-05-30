player1 = input("Player 1, please pick either rock, paper or scissors\n")
player2 = input("Player 2, please pick either rock, paper or scissors\n")


def game(pl1, pl2):
    if pl1 == pl2:
        return "Its a tie!"
    elif pl1 == "rock":
        if pl2 == "paper":
            return "Player 2 wins!"
        elif pl2 == "scissors":
            return "Player 1 wins!"
    elif pl1 == "paper":
        if pl2 == "rock":
            return "Player 1 wins!"
        elif pl2 == "scissors":
            return "Player 2 wins!"
    elif pl1 == "scissors":
        if pl2 == "rock":
            return "Player 2 wins!"
        elif pl2 == "paper":
            return "Player 1 wins!"
    else:
        return "Entered an incorrect object"


print(game(player1.lower(), player2.lower()))
