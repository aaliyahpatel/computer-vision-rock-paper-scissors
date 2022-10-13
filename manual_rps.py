import random

options = ["rock", "paper", "scissors"]

get_user_choice = input("Choose rock, paper or scissors: ")

get_computer_choice = random.choice(options)

print(get_computer_choice)