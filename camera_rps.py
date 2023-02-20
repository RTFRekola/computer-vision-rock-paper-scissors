import cv2
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
