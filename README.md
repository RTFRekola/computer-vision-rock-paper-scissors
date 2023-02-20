# Computer Vision RPS

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

## Milestone 1: Set up the environment

This consists of getting the Git and GitHub going. 

## Milestone 2: Create the computer vision system

Four different sets of images are recorded with webcam and stored in teachablemachine.withgoogle.com. A set of 20 images show the regular view of a user sitting at his computer. Three sets of 100 images each show the user with a hand signal of either rock, paper or scissors. These sets are used in the web service to train a model for rock-paper-scissors. This model is saved as two files, keras_model.h5 and labels.txt, and imported into the project folder. 

## Milestone 3: Install the dependencies

A conda environment, p38, is created with python version 3.8. Python libraries opencv-python, tensorflow, and ipykernel are installed to meet the dependencies of the project. Using a pre-existing code, the functionality of the model is tested. 

## Milestone 4: Create a Rock-Paper-Scissors game

A manual version of the game is created. It randomly selects computer choice and asks verbally the user to provide his. Once this is done the comparison is made and either declared a tie or the winner is announced. 

## Milestone 5: Use the camera to play Rock-Paper-Scissors
