import cv2
from keras.models import load_model
import numpy as np
import random
import time

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def countdown_counter():
    countdown = 3
    print("\n Show your chosen gesture in...")
    while countdown > 0:
        print(f'{countdown}')
        cv2.waitKey(1000)
        countdown -= 1
    print('\nShow your gesture NOW!')


def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])


def get_camera():
    end_time = time.time() + 1
    while time.time() < end_time:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return normalized_image

def get_prediction():
        data[0] = get_camera()
        prediction = model.predict(data)
        return prediction

def get_user_choice():
    while True:
        prediction = get_prediction()
        max_index = np.argmax (prediction)
        if max_index == 0:
            user_choice = "Rock"

        elif max_index == 1:
            user_choice =  "Paper"
            
        elif max_index == 2:
            user_choice = "Scissors"
            
        else:
            user_choice =  "Nothing"
        
        if user_choice != "Nothing":
            break
        else:
            print("Please show a valid choice!")

    print(f"Machine predicted you chose: {user_choice}")
        
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == "Rock":
        if user_choice == "Rock":
            return "Tie"
        elif user_choice == "Paper":
            return "You"
        else:
            return "Computer"

    if computer_choice == "Paper":
        if user_choice == "Rock":
            return "Computer"
        elif user_choice == "Paper":
            return "Tie"
        else:
            return "You"

    if computer_choice == "Scissors":
        if user_choice == "Rock":
            return "You"
        elif user_choice == "Paper":
            return "Computer"
        else:
            return "Tie"
        





def play_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1

  while True:
        computer_choice = get_computer_choice()
        get_camera()
        countdown_counter()
        user_choice = get_user_choice()
        winner = get_winner(computer_choice, user_choice)

        print(f"The computer chose: {computer_choice}.")

        

        if winner == "Tie":
            print(f"Round: {rounds}: No winner")
        else:
            print(f"Round {rounds}:The winner is {winner}!")

            if winner == "Computer":
                computer_wins += 1
            if winner == "You":
                user_wins += 1

        print(f"Current score: Computer {computer_wins} - {user_wins} You.\n")

        if computer_wins == 3:
            print(f"Computer wins! Computer beat you by {computer_wins}-{user_wins}.")
            break

        if user_wins == 3:
            print(f"You win! You beat the Computer by {user_wins}-{computer_wins}")
            break

        rounds += 1

play_game()







