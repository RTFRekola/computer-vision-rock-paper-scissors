import random

def get_computer_choice():
    rps_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(rps_list)
    return computer_choice

def get_user_choice():
    user_choice = input("Rock, paper or scissors? ")
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice==user_choice:
        print("It is a tie!")
    elif computer_choice=="rock" and user_choice=="scissors" or computer_choice=="scissors" and user_choice=="paper" or computer_choice=="paper" and user_choice=="rock":
        print("You lost")
    else:
        print("You won!")
    # end if

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)

play()
