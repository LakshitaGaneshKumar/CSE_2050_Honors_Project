# Imports
from Contestant import Contestant

class GamePlay():
    def __init__(self, num_contestants):
        self._num_contestants = num_contestants

    def create_players(self):
        # Get user input for contestant objects
        print("Create Your Players (input first and last name of each contestant)")

        # Create new set to store all Contestant objects in play
        self.contestants = []

        # Repeatedly prompt user for a contestant name, create new Contestant object, and add it to the contestants set
        for i in range(1, self._num_contestants + 1):
            name = input(f"Contestant {i}: ")
            self.contestants.append(Contestant(name))

        for contestant in self.contestants:
            print(contestant.get_name())