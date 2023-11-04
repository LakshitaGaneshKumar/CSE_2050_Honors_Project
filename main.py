# import PySimpleGUI as sg
# #https://realpython.com/pysimplegui-python/

# sg.Window(title="Hello World", layout=[[]], margins=(1000, 1000)).read()

# Imports
from Contestant import Contestant

# Constants
NUM_CONTESTANTS = 16

# Welcome Message
print("Welcome to Are You The One!")

# Get user input for contestant objects
print("Pick Your Players (Input first and last name of each contestant)")

# Create new set to store all Contestant objects in play
contestants = set()

# Repeatedly prompt user for a contestant name, create new Contestant object, and add it to the contestants set
for i in range(NUM_CONTESTANTS):
    name = input(f"Contestant {i}: ")
    contestants.add(Contestant(name))


# Contestant Object attributes: 
    # name - name of contestant
    # perfect match - contestant's perfect match
    # found perfect match - True/False if contestant found their perfect match
    # invalid matches - list of every but the contestant and their perfect match
    # current partner - current partner during this week
    # current partner is valid - True or False if current partnet is perfect match or not
    # known invalid matches - list of matches that are known to be invalid in the gameplay
    # possible matches - list of possible matches based on who we know to be an invalid match. (Everyone but the contestant and their invalid matches)
# Contestant object methods: getter and setter methods

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