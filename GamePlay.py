from GameData import GameData
import os

class GamePlay():
    def __init__(self):
        """Initialize a new Game play object"""
        # Create Constants
        self.NUM_CONTESTANTS = None
        self.MIN_CONTESTANTS = 6
        self.MAX_CONTESTANTS = 16

    def new_game(self):
        # Welcome Message
        os.system('clear')
        print("Welcome to Are You The One!")

        # Prompt User for Number of Contestants
        # This will be implemented as buttons in the GUI
        while(self.NUM_CONTESTANTS is None or self.NUM_CONTESTANTS % 2 != 0 or self.NUM_CONTESTANTS < self.MIN_CONTESTANTS or self.NUM_CONTESTANTS > self.MAX_CONTESTANTS):
            self.NUM_CONTESTANTS = int(input(f"Choose your number of contestants (enter an even number between {self.MIN_CONTESTANTS}-{self.MAX_CONTESTANTS}): "))

        # Create new game database with given number of contestant
        os.system('clear')
        print(f'Get ready to play "Are You The One?" With {self.NUM_CONTESTANTS} Contestants!')
        self.game = GameData(self.NUM_CONTESTANTS)

        # Create Contestant Objects
        print("Create Your Players (input names of each contestant):")
        for i in range(1, self.NUM_CONTESTANTS + 1):
            name = input(f"Contestant {i}: ")
            self.game.add_contestant(name)

        # Randomly choose perfect pairs
        self.game.create_perfect_matches()

        self.simulate_week()

    def display_current_pairs(self):
        """Displays current week's pairs"""
        displayed = []
        current_pairs = self.game.get_current_pairs()
        self.num_perfect_pairs_found = 0
        print("\nHere's this week's line-up of couples:")
        for key in current_pairs:
            if key not in displayed:
                # Print contestant's name and their match
                print(f"{key.get_name()} and {current_pairs[key].get_name()}")

                # Track how many perfect matches have been found
                if key.get_perfect_match() == current_pairs[key]:
                    self.num_perfect_pairs_found += 1

                # Update the list of contestants who have been displayed on screen already
                displayed.append(key)
                displayed.append(current_pairs[key])

    def display_perfect_matches(self):
        """Displays the perfect matches for testing purposes"""
        displayed = []
        perfect_pairs = self.game.get_perfect_matches()
        print("\nPerfect Matches:")
        for key in perfect_pairs:
            if key not in displayed:
                print(f"{key.get_name()} and {perfect_pairs[key].get_name()}")
                displayed.append(key)
                displayed.append(perfect_pairs[key])

    def simulate_week(self):
        """Simulate one week of the game play"""
        # Track number of weeks played
        self.game.increment_weeks()
        os.system('clear')
        print(f"Welcome to Week {self.game.get_weeks_played()}.")

        # Pair up matches for the current week
        self.game.pair_current_matches()

        # Display current pairs
        self.display_current_pairs()
        self.display_perfect_matches()

        # Check if all perfect matches have been found
        if self.num_perfect_pairs_found == self.NUM_CONTESTANTS // 2:
            weeks = self.game.get_weeks_played()

            # Grammatical check
            if weeks == 1: 
                string = "week"
            else: 
                string = "weeks"

            print(f"All perfect matches have been found! You helped all contestants find their true love in {self.game.get_weeks_played()} {string}.")
            replay = input("Would you like to play again? (Y/N): ")
            
            if replay == "Y": 
                self.__init__()
                self.new_game()
            else: 
                os.system('clear')
                print('\nThanks for playing "Are You The One?".')
        else:
            print(f"Number of Perfect Matches Found: {self.num_perfect_pairs_found}")

        