import random

options = ["rock", "paper", "scissors"]

get_user_choice = input("Choose rock, paper or scissors: ")

get_computer_choice = random.choice(options)

print(f"Computer chose {get_computer_choice}.")


def get_winner():

    if get_computer_choice == "rock":
        if get_user_choice == "scissors":
            print ("Computer wins!")
        elif get_user_choice == "paper":
            print("You win!")
        else:
            print("It's a draw.")

    elif get_computer_choice == "paper":
        if get_user_choice == "scissors":
            print ("You win!")
        elif get_user_choice == "rock":
            print("Computer wins!")
        else:
            print("It's a draw.")

    elif get_computer_choice == "scissors":
        if get_user_choice == "rock":
            print ("You win!")
        elif get_user_choice == "paper":
            print("Computer wins!")
        else:
            print("It's a draw.")

get_winner()