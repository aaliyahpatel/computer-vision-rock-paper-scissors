import random

options = ["rock", "paper", "scissors"]

user_choice = input("Choose rock, paper or scissors: ")

computer_choice = random.choice(options)

def get_user_choice():
    return user_choice

def get_computer_choice():
    return computer_choice


def get_winner():

    if computer_choice == "rock":
        if user_choice == "scissors":
            print ("Computer chose rock. Computer wins!")
        elif user_choice == "paper":
            print("Computer chose rock. You win!")
        else:
            print("Computer chose rock. It's a draw.")

    elif computer_choice == "paper":
        if user_choice == "scissors":
            print ("Computer chose paper. You win!")
        elif user_choice == "rock":
            print("Computer chose paper. Computer wins!")
        else:
            print("Computer chose paper. It's a draw.")

    elif computer_choice == "scissors":
        if user_choice == "rock":
            print ("Computer chose scissors. You win!")
        elif user_choice == "paper":
            print("Computer chose scissors. Computer wins!")
        else:
            print("Computer chose scissors. It's a draw.")

def game():
    get_user_choice()
    get_computer_choice()
    get_winner()

game()