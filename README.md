## Project Description

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

## Installation Instructions

When preparing to run this code for the first time, do the following:

- create a directory for the code; e.g. in Linux terminal mkdir hangman
- copy files camera.rps, , keras_model.h5, labels.txt, requirements.txt into the directory you just created

## Usage Instructions

- go to the directory where you installed the code
- run the file camera_rps.py; e.g. in Linux terminal python3 camera_rps.py

## License Information

Copyright 2023, Rami Rekola

Copying and distribution of these files, with or without modification, are permitted in any medium without royalty, provided the copyright notice and this notice are preserved. These files are offered as-is, without any warranty.

## Project History

### Create the Computer Vision System

Four different sets of images are recorded with webcam and stored in teachablemachine.withgoogle.com. A set of 20 images show the regular view of a user sitting at his computer. Three sets of 100 images each show the user with a hand signal of either rock, paper or scissors. These sets are used in the web service to train a model for rock-paper-scissors. This model is saved as two files, keras_model.h5 and labels.txt, and imported into the project folder. 

### Install the Dependencies

A conda environment, p38, is created with python version 3.8. Python libraries opencv-python, tensorflow, and ipykernel are installed to meet the dependencies of the project. Using a pre-existing code, the functionality of the model is tested. 

### Create a Rock-Paper-Scissors Game

A manual version of the game is created. It randomly selects computer choice and asks verbally the user to provide his. Once this is done the comparison is made and either declared a tie or the winner is announced. 

### Use the Camera to Play Rock-Paper-Scissors

The user choice is acquired via computer vision model instead of asking it verbally. This is done in a loop that continues for three seconds, after which it declares the user's choice in the terminal. This is compared to the computer selection and once either the compute or the user have three wins, the winner is announced. 

![computer-vision-rock-paper-scissors](1.jpg?raw=true "Nothing")
![computer-vision-rock-paper-scissors](36.jpg?raw=true "Rock")
![computer-vision-rock-paper-scissors](26.jpg?raw=true "Paper")
![computer-vision-rock-paper-scissors](51.jpg?raw=true "Scissors")

A further improvement is made with a version of the code where most of the functionality has been placed in a class. The only part of code outside of the class is the line that instantiates the class and the line that runs the function play_game in the class. Play_game runs functions get_computer_choice and get_user_choice to acquire the computer's choice (as a random selection) and user's choice as analysed from image data retrieved from the user showing the appropriate hand signal to the webcam. The matching is done in another function, called get_prediction. Finally the winner is chosen in function get_winner. The game is played until either player has three wins. This is implemented by a for loop in the play_game - running until three wins - and while loop in get_user_choice - running a loop for three seconds at a time for image analysis. 
