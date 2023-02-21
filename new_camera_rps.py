import cv2
import time
import random
import numpy as np
from keras.models import load_model
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_computer_choice():
    rps_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(rps_list)
    return computer_choice

def get_user_choice():
    start_time = time.time()
    end_time = start_time + 3
    while time.time()<end_time: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        user_choice = get_prediction(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return user_choice

def get_prediction(model):
    model_index = np.argmax(model)
    if model_index==0:
        choice = "nothing"
    elif model_index==1:
        choice = "rock"
    elif model_index==2:
        choice = "paper"
    elif model_index==3:
        choice = "scissors"
    else:
        choice = "unknown"
    # end if
    return choice

def get_winner(computer_choice, user_choice):
    if computer_choice==user_choice:
        print("It is a tie!")
        winner = ""
    elif computer_choice=="rock" and user_choice=="scissors" or computer_choice=="scissors" and user_choice=="paper" or computer_choice=="paper" and user_choice=="rock":
        print("You lost")
        winner = "computer"
    else:
        print("You won!")
        winner = "user"
    # end if
    return winner

computer_wins = 0  ;  user_wins = 0
for i in range(0,99):
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    if user_choice=="rock":
        print("You chose rock.")
    elif user_choice=="paper":
        print("You chose paper.")
    elif user_choice=="scissors":
        print("You chose scissors.")
    else:
        print("You chose nothing.")
    # end if
    winner = get_winner(computer_choice, user_choice)
    if winner=="computer":
        computer_wins = computer_wins + 1
    elif winner=="user":
        user_wins = user_wins + 1
    # end if
    if computer_wins==3:
        print("Game over, computer is the winner.")
        break
    elif user_wins==3:
        print("Game over, you are the winner.")
        break
    else:
        print("Nobody won, something is not right...")
    # end if
# end for
         
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
