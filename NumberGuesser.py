__author__ = 'william'

import random


def init():
    try:
        range = input("New game!! \nWelcome! Input your range of values:\n>>> ")
        randomNumber = random.randrange(int(range[0]), int(range[2]))
    except Exception:
        print("You entered the wrong format. start-finish is the correct format.")
        init()

    while True:
        try:
            guess = int(input("Guess the number!\n>>> "))
        except Exception:
            print("You did not enter a number!")
            continue

        if guess < int(range[0]) or guess > int(range[2]):
            print("The range is from " + range)
            continue
        if guess == randomNumber:
            print("Correct! Your answer was ", randomNumber)
            break
        elif guess < randomNumber: print("Higher!")
        else: print("Lower!")

    newGame = input("Nice job, would you like to play again? Enter 'yes' or 'no'\n>>>")
    while True:
        if newGame == "yes":
            init()
            break;
        elif newGame == "no": exit()
        else: newGame = input("You entered the wrong input. Type 'yes' or 'no'!\n>>>")


if __name__ == "__main__": init()