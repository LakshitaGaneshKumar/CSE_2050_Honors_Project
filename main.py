# import PySimpleGUI as sg
# #https://realpython.com/pysimplegui-python/

# sg.Window(title="Hello World", layout=[[]], margins=(1000, 1000)).read()

# Imports
from Contestant import Contestant
from GamePlay import GamePlay
import os

# Constants
NUM_CONTESTANTS = None
MIN_CONTESTANTS = 4
MAX_CONTESTANTS = 16

# Welcome Message
os.system('clear')
print("Welcome to Are You The One!")

# Prompt User for Number of Contestants
# This will be implemented as buttons in the GUI
while(NUM_CONTESTANTS is None or NUM_CONTESTANTS % 2 != 0 or NUM_CONTESTANTS < MIN_CONTESTANTS or NUM_CONTESTANTS > MAX_CONTESTANTS):
    NUM_CONTESTANTS = int(input("Choose your number of contestants (enter an even number between 4-16): "))

# Start new game play with given number of contestant
os.system('clear')
print(f'Get ready to play "Are You The One?" With {NUM_CONTESTANTS} Contestants!')
game = GamePlay(NUM_CONTESTANTS)

# Create Contestant Objects
print("Create Your Players (input first and last name of each contestant):")
for i in range(1, NUM_CONTESTANTS + 1):
    name = input(f"Contestant {i}: ")
    game.add_contestant(name)

# Randomly choose perfect pairs
game.create_matches()

# Track number of weeks played
game.increment_weeks()
os.system('clear')
print(f"Welcome to Week {game.get_weeks_played()}. Will you find all the matches?")

# Randomly pair up contestants

# Check if all matches are found

# Display match results (2 matches found, no matches found, all matches found)

# Get user input for truth booth
    # Is the match at the truth booth a valid match
    # Update contestant objects accordingly

# Pair contestants to people they haven't been paired before
    # Randomly choose from possible matches attribute

# Repeat process of checking if all matches are found, displaying results, and going to the truth booth