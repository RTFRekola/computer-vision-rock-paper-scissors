import cv2
import time
import random
import numpy as np
from keras.models import load_model

class RockPaperScissors:
    '''
    This class is used to determine winner of the rock-paper-scissors game.
    '''
    def __init__(self, user_choice="", computer_choice="", winner=""):
        self.user_choice = user_choice
        self.computer_choice = computer_choice
        self.winner = winner
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    def get_computer_choice(self):
        rps_list = ["rock", "paper", "scissors"]
        self.computer_choice = random.choice(rps_list)
        return self.computer_choice

    def get_user_choice(self):
        start_time = time.time()
        end_time = start_time + 3
        while time.time()<end_time: 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            self.user_choice = self.get_prediction(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        if self.user_choice=="rock":
            print("You chose rock.")
        elif self.user_choice=="paper":
            print("You chose paper.")
        elif self.user_choice=="scissors":
            print("You chose scissors.")
        else:
            print("You chose nothing.")
        # end if
        return self.user_choice

    def get_prediction(self, model):
        model_index = np.argmax(model)
        if model_index==0:
            self.choice = "nothing"
        elif model_index==1:
            self.choice = "rock"
        elif model_index==2:
            self.choice = "paper"
        elif model_index==3:
            self.choice = "scissors"
        else:
            self.choice = "unknown"
        # end if
        return self.choice

    def get_winner(self, computer_choice, user_choice):
        if computer_choice==user_choice:
            print("It is a tie!")
            self.winner = ""
        elif computer_choice=="rock" and user_choice=="scissors" or computer_choice=="scissors" and user_choice=="paper" or computer_choice=="paper" and user_choice=="rock":
            print("You lost")
            self.winner = "computer"
        else:
            print("You won!")
            self.winner = "user"
        # end if
        return self.winner

    def play_game(self):
        computer_wins = 0  ;  user_wins = 0
        for i in range(0,99):
            computer_choice = self.get_computer_choice()
            user_choice = self.get_user_choice()
            winner = self.get_winner(computer_choice, user_choice)
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
                print("Next round...")
            # end if
        # end for
        # After the loop release the cap object
        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

rps = RockPaperScissors()
rps.play_game()
