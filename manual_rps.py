import random

def get_computer_choice():
    rps_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(rps_list)
    return computer_choice

def get_user_choice():
    user_choice = ("Rock, paper or scissors? ")
    return user_choice

