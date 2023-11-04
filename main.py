# import PySimpleGUI as sg
# #https://realpython.com/pysimplegui-python/

# sg.Window(title="Hello World", layout=[[]], margins=(1000, 1000)).read()

# Imports
from Contestant import Contestant
from GamePlay import GamePlay

# Constants
NUM_CONTESTANTS = 1

# Welcome Message
print("Welcome to Are You The One!")

# Prompt User for Number of Contestants
# This will be implemented as buttons in the GUI
while(NUM_CONTESTANTS % 2 != 0 or NUM_CONTESTANTS < 4):
    NUM_CONTESTANTS = int(input("Choose your number of contestants (enter an even number between 4-16): "))
print(f'Get ready to play "Are You The One?" With {NUM_CONTESTANTS} Contestants!')

# Start new game play
game = GamePlay(NUM_CONTESTANTS)

# Create Contestant Objects
game.create_players()


# Randomly choose 8 perfect pairs



# Update person objects w/ their pairs

# Track number of weeks played

# Randomly pair up contestants

# Check if all matches are found

# Display match results (2 matches found, no matches found, all matches found)

# Get user input for truth booth
    # Is the match at the truth booth a valid match
    # Update contestant objects accordingly

# Pair contestants to people they haven't been paired before
    # Randomly choose from possible matches attribute

# Repeat process of checking if all matches are found, displaying results, and going to the truth booth