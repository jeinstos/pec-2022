import random
import time

random.seed(time.time())

valid_choices = ["rock", "paper", "scissors"]

print(">>> rock, paper, scissors game <<<")
print()

while True:
    user_choice = input("choose your weapon: ")
    user_choice = user_choice.lower()

    if user_choice not in valid_choices:
        print("error: invalid choice: '" + user_choice + "'")
        continue
    
    computer_choice = random.choice(valid_choices)
    print("computer choice: " + computer_choice)
    
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
        print("YOU WON!")
        print()
    elif (user_choice == "rock" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "rock"):
        print("YOU LOST!")
        print()
    else:
        print("TIE :(")
        print()
