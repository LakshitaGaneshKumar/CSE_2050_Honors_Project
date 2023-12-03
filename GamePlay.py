from GameData import GameData
import os
import time

class GamePlay():
    def __init__(self, num_contestants=16):
        """Initialize a new Game play object"""
        self.NUM_CONTESTANTS = num_contestants

    def new_game(self):
        # Welcome Message
        os.system('clear')
        print("Welcome to Are You The One!")

        # Create new game database
        print(f'Get ready to play "Are You The One?" With {self.NUM_CONTESTANTS} Contestants!')
        self.game = GameData(self.NUM_CONTESTANTS)

        time.sleep(1)

        # Create Contestant Objects
        print("Create Your Players (input names of each contestant):")
        for i in range(1, self.NUM_CONTESTANTS + 1):
            name = input(f"Contestant {i}: ")
            self.game.add_contestant(name)

        # Randomly choose perfect pairs
        self.game.create_perfect_matches()
        
        # Start simulating weeks
        self.simulate_week()

    def display_current_pairs(self):
        """Displays current week's pairs"""
        displayed = []
        current_pairs = self.game.get_current_pairs()
        self.num_perfect_pairs_found = 0

        time.sleep(1)

        print("\nHere's this week's line-up of couples:")
        for key in current_pairs:
            time.sleep(0.2)
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
        print("\nPerfect Matches for Testing Purposes:")
        for key in perfect_pairs:
            if key not in displayed:
                print(f"{key.get_name()} and {perfect_pairs[key].get_name()}")
                displayed.append(key)
                displayed.append(perfect_pairs[key])

    def simulate_week(self):
        """Simulate one week of the game play"""
        # Track number of weeks played
        self.game.update_possible_matches()
        self.game.increment_weeks()
        # os.system('clear')
        time.sleep(1)

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

        # Else, if not all matches are found, prompt user to send a couple to the truth booth, and continue simulating weeks
        else:
            print(f"Number of Perfect Matches Found: {self.num_perfect_pairs_found}")
            self.truth_booth()

    def truth_booth(self):
        """Prompts user to send a couple to the truth booth and updates game database accordingly"""
        # User will input a couple in the format "contestant and match", which is then split into a list format
        couple = input(f"Choose a couple to send to the Truth Booth: ")
        couple_as_list = couple.split()

        # Extract data on the given couple
        contestants_to_objects = self.game.get_contestants_to_objects()
        contestant = contestants_to_objects[couple_as_list[0]]
        partner = contestants_to_objects[couple_as_list[2]]

        # Check if they are a perfect match or not
        if contestant.get_perfect_match() == partner:
            contestant.set_found_match(True)
            partner.set_found_match(True)

            # Update the invalid matches of the rest of the players
            for person in self.game.get_contestants():
                if person != contestant and person != partner:
                    person.set_known_invalid_match(contestant)
                    person.set_known_invalid_match(partner)
            
            self.game.update_possible_matches()

            print(f"{contestant.get_name()} and {partner.get_name()} are a perfect match! They will always be paired together now.")
        else:
            contestant.set_known_invalid_match(partner)
            partner.set_known_invalid_match(contestant)

            self.game.update_possible_matches()

            print(f"{contestant.get_name()} and {partner.get_name()} are not a perfect match. They will never be paired together again.")

        time.sleep(1)
        
        self.simulate_week()