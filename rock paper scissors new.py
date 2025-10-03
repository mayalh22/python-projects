#Maya Hazarika
#Rock Paper Scissors project
#This program allows a user to input a decision, and play against a random choice from the computer.


import random

while True:
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input, please try again.")
        continue  # go back to the start of the loop

    choice = random.randint(1, 3)

    if choice == 1:
        compchoice = "scissors"
    elif choice == 2:
        compchoice = "paper"
    else:
        compchoice = "rock"

    print("The computer chose", compchoice)

    if user_choice == compchoice:
        print("It's a tie! Try again.")
    elif (user_choice == "rock" and compchoice == "scissors") or \
         (user_choice == "paper" and compchoice == "rock") or \
         (user_choice == "scissors" and compchoice == "paper"):
        print("Congrats, you win!")
    else:
        print("The computer won")
