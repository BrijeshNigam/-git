# It is a game where plauer select one of three options. Then computer system make a random 
# selsction. The winner is determined by the rules of Rock, Paper, Scissors.

# Winning Rules:
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock

import random

print ("Welcome to Rock, Paper, Scissors Game!")
print("Winning Rules: \nRock beats Scissors \nScissors beats Paper \nPaper beats Rock")


choose = input("Enter your choice (rock, paper, scissors): ").lower()

while true:

    print("Chooise on option: Rock, Paper, Scissors")

    try: 
        choose = int(input("Enter your Choice: "))
    except ValueError:
        print("Enter a valid choice \n")
        continue

    while choose < 1 or choose > 3:
        choose = int(input("please Enter a valid choice: "))

        user_choice = choices[choose -1]

        print("Computer choice is:" , user_choice)
        print("Now it's computer turn to choose an option...")

        # Computer makes a random choice
        computer_choice = random.randint(1, 3)
        computer_choices = choices[computer_choice - 1]

        print("Computer choice is: ", computer_choices)
        print("User choise is: "), computer_choices=


