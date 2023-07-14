#Wordle Game in Python
#Windows 10 Home
#Visual Studio Code

import os
import random

os.system("cls")

GREEN = "\u001b[42m"
YELLOW = "\u001b[43m"
RESET = "\u001b[0m"

print("WORDLE!")

correct_guess = random.choice(["ZEBRA", "FLUTE", "HOUSE", "SWIFT", "PHOTO", "PHONE", "RADIO", "TRUCK", "WORDS", "NIGHT", "ROBOT", "HUMAN", "GHOST", "SLANG", "KOALA", "CHAIR", "PLACE", "PLANT", "TABLE", "HELLO", "WORLD",
                               "INDIA", "TEXAS", "HAPPY", "SMILE", "CANDY", "COUCH", "EMAIL", "YOUNG", "THERE", "RANGE", "BRUSH", "LARRY", "BINGO", "SHAKE", "EARTH", "PANDA", "TIGER", "BLACK", "WHITE", "GREEN", "SHELF", 
                               "LEARN", "CREAM", "RANCH", "CLOCK", "WATCH", "GUARD", "SMOKE", "CROWN", "TARDY", "EARLY", "SLOTH", "SNAIL", "CHINA", "JAPAN", "PIANO", "GRADE", "CLASS", "HOTEL", "STOVE", "SPACE", "MONEY"])

for _ in range(6):
    guess = input("Enter Guess.> ").upper()

    #Check each letter
    for i in range(0, 5):
        if guess[i] == correct_guess[i]:
            print(f"{GREEN}{guess[i]}{RESET}", end="")
        elif guess[i] in correct_guess:
            print(f"{YELLOW}{guess[i]}{RESET}", end="")
        else:
            print(guess[i], end="")
                
    print()
    
    #Check if the guess is correct
    if guess == correct_guess:
        print("You Win!")
        exit()
        
print("You Lose!")
print("The correct word was {}".format(correct_guess))
    
