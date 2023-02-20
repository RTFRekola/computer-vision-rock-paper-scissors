import cv2
import time
import numpy as np

def get_prediction(model):
    model_index = np.argmax(model)
    if model_index==0:
        choice = "nothing"
    elif model_index==1:
        choice = "rock"
    elif model_index==2:
        choice = "paper"
    else:
        choice = "scissors"
    # end if
    return choice

start_time = time.time()
while time.time()<start_time+3:
    cv2.imshow()
    user_choice = get_prediction(model)
    if user_choice=="rock":
        print("You chose rock.")
    elif user_choice=="paper":
        print("You chose paper.")
    elif user_choice=="scissors":
        print("You chose scissors.")
    else:
        print("You chose nothing.")
    # end if
