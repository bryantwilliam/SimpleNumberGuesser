__author__ = 'william'

import random


def init():
    try:
        range = list(input("New game!! \nWelcome! Input your range of values:\n>>> ").split("-"))
        randomNumber = random.randrange(int(range[0]), int(range[1]))
    except ValueError:
        print("You entered the wrong format. start-finish is the correct format.")
        init()

    while True:
        try:
            guess = int(input("Guess the number!\n>>> "))
        except ValueError:
            print("You did not enter a number!")
            continue
        min, max = range[0], range[1]
        if guess < int(min) or guess > int(max):
            print("The range is from " + min + " to " + max)
            continue
        if guess == randomNumber:
            print("Correct! Your answer was ", randomNumber)
            break
        elif guess < randomNumber: 
            print("Higher!")
        else: 
            print("Lower!")

    newGame = input("Nice job, would you like to play again? Enter 'yes' or 'no'\n>>>")
    while True:
        if newGame.lower() == "yes":
            init()
            break
        elif newGame.lower() == "no": 
            exit()
        else: 
            newGame = input("You entered the wrong input. Type 'yes' or 'no'!\n>>>")


if __name__ == "__main__": 
    init()
