import cv2
from keras.models import load_model
import numpy as np
import random
import time

def countdown_counter(self):
        countdown = 3
        print("\nPrepare to show me your chosen gesture in...")
        while countdown > 0:
            print(f"{countdown}")
            cv2.waitKey(1000)
            countdown -= 1
        print("\nShow your hand NOW!")


def get_camera(self):
        end_time = time.time() + 1
        while time.time() < end_time:
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return normalized_image

def get_prediction(self):
    self.data[0] = self.get_camera()
    prediction = self.model.predict(self.data)
    return prediction

def classify_output(self):
    prediction = self.get_prediction()
    max_index = np.argmax (prediction)
    if max_index == 0:
        print("Rock")
        user_prediction = "Rock"
    elif max_index == 1:
        print("Paper")
        user_prediction = "Paper"
    elif max_index == 2:
        print ("Scissors")
        user_prediction = "Scissors"
    else:
        print("Nothing")
        user_prediction = "Nothing"

    print(f"The machine predicted that the user gesture was {self.user_prediction}")
    return self.user_prediction









