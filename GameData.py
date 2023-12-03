from Contestant import Contestant
import random

class GameData():
    def __init__(self, num_contestants):
        self._num_contestants = num_contestants
        self._contestants = []
        self._perfect_matches = {}
        self._current_pairs = {}
        self._contestants_to_objects = {}
        self._weeks_played = 0
        self._paired = set()

    def add_contestant(self, contestant):
        """
        Adds a new contestant to the game
        
        Parameters:
        contestant (String)
        """
        player = Contestant(contestant)
        self._contestants.append(player)

        # Maps the string representation of the contestant's name to its Contestant object representation
        self._contestants_to_objects[contestant] = player

    def get_contestants(self):
        """Returns the list of all Contestant objects in the current game play"""
        return self._contestants
    
    def get_contestants_to_objects(self):
        """Returns the dictionary of all key:value pairs that map a string representation of a contestant's name to its Contestant object"""
        return self._contestants_to_objects

    def get_num_contestants(self):
        """Returns the number of contestants"""
        return self._num_contestants
    
    def get_perfect_matches(self):
        """Returns the dictionary of all perfect matches"""
        return self._perfect_matches
    
    def get_current_pairs(self):
        """Returns the dictionary of all current pairs"""
        return self._current_pairs
        
    def get_weeks_played(self):
        """Returns the number of weeks played"""
        return self._weeks_played
    
    def increment_weeks(self):
        """Increment the number of weeks played"""
        self._weeks_played += 1

    def create_perfect_matches(self):
        """Generates perfect matches and updates Contestant objects with their perfect match"""
        # Create copy of contestants set as a list and shuffle that list
        random.shuffle(self._contestants)

        # Update each contestant with their perfect match
        for i in range(0, self._num_contestants, 2):
            # Store contestants in temporary variables
            contestant1 = self._contestants[i]
            contestant2 = self._contestants[i+1]
            
            # Use temporary variables to update the perfect match attribute of each contestant
            contestant1.set_perfect_match(contestant2)
            contestant2.set_perfect_match(contestant1)

            # Add new key:value pairs to perfect matches dictionary 
            self._perfect_matches[contestant1] = contestant2
            self._perfect_matches[contestant2] = contestant1

        # Traverse through each key:value pair in the perfect matches dictionary and update the invalid matches attribute for each Contestant object
        for key in self._perfect_matches:
            for other in self._perfect_matches:
                if other != self._perfect_matches[key]:
                    key.set_invalid_match(other)
                if self._perfect_matches[other] != self._perfect_matches[key]:
                    key.set_invalid_match(self._perfect_matches[other])
            # print(f"{key.get_name()}'s Invalids: {key.get_invalid_matches()}")

    def update_possible_matches(self):
        """Updates the possible matches for each contestant based on current game knowledge"""
        for contestant in self._contestants:
            # Create empty list
            possible_matches = []

            # If this is the first week of the game, everyone is a possible match except the contestant themselves
            if self._weeks_played == 0:
                for other in self._contestants:
                    if other != contestant:
                        possible_matches.append(other)

            # If the contestant has already found their match, their perfect match is their only possible match
            elif contestant.get_found_match():
                possible_matches.append(contestant.get_perfect_match())

            # Else, traverse through all contestants and add the ones that are not known to be invalids to the possible matches set
            else:
                invalids = contestant.get_known_invalid_matches()
                for other in self._contestants:
                    if other not in invalids:
                        possible_matches.append(other)

            # Update Contestant's possible matches attribute
            contestant.set_possible_matches(possible_matches)


    def update_database(self, contestant, match):
        """Takes in a contestant and their current partner/match and updates the game database"""
        # Update each Contestant object with their current partners
        contestant.set_current_partner(match)
        match.set_current_partner(contestant)

        # # Update set of paired contestant
        # self._paired.add(contestant)
        # self._paired.add(match)

        # Update current pairs dictionary
        self._current_pairs[contestant] = match
        self._current_pairs[match] = contestant

    def pair_current_matches(self):
        """Pairs the matches for the current week"""
        self._current_pairs = {}
        self._paired = set()

        # Iterate through each contestant
        for contestant in self._contestants:

            # Check if contestant is not paired yet
            if contestant not in self._paired:

                # Check if contestant has found their match already
                if contestant.get_found_match():
                    match = contestant.get_perfect_match()
                    self.update_database(contestant, match)
                    
                    self._paired.add(contestant)
                    self._paired.add(match)
                    # print(f"\npaired: {self._paired}")
                
                # Else, pair them with someone from their possible matches list
                else:
                    possible_matches = contestant.get_possible_matches()
                    # for mat in possible_matches:
                    #     print(mat.get_name())

                    match = random.choice(possible_matches)

                    while(match in self._paired):
                        match = random.choice(possible_matches)
                    # print(match.get_name())
                    
                    self.update_database(contestant, match)

                    self._paired.add(contestant)
                    self._paired.add(match)
                    # print(f"\npaired else: {self._paired}")