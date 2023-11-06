# Imports
from Contestant import Contestant

class GamePlay():
    def __init__(self, num_contestants):
        self._num_contestants = num_contestants
        self._num_pairs = self._num_contestants // 2
        self._contestants = set()
        self._perfect_matches = {}
        self._weeks_played = 0

    def add_contestant(self, contestant):
        """Takes in a contestant name, creates a new Contestant object, and adds it to the set of current contestant"""
        self._contestants.add(Contestant(contestant))

    def get_contestants(self):
        """Returns the set of all Contestant objects in the current game play"""
        return self._contestants
    
    def get_num_contestants(self):
        """Return the number of contestants"""
        return self._num_contestants
    
    def get_num_pairs(self):
        """Return the number of pairs"""
        return self._num_pairs
    
    def get_perfect_matches(self):
        """Return the dictionary of all perfect matches"""
        return self._perfect_matches
    
    def get_weeks_played(self):
        """Return the number of weeks played"""
        return self._weeks_played
    
    def increment_weeks(self):
        """Increment the number of weeks played"""
        self._weeks_played += 1

    def create_matches(self):
        """Generates perfect matches and updates Contestant objects with their perfect match"""
        # Create copy of contestants set
        self.contestants_copy = self._contestants.copy()

        # Update each contestant with their perfect match
        for i in range(self._num_pairs):
            # Pop contestants from the copied set and store them in temporary variables
            contestant1 = self.contestants_copy.pop()
            contestant2 = self.contestants_copy.pop()
            
            # Use temporary variables to update the perfect match attributes of each contestant
            contestant1.set_perfect_match(contestant2)
            contestant2.set_perfect_match(contestant1)

            # Add new key value pairs to perfect matches dictionary 
            self._perfect_matches[contestant1] = contestant2
            self._perfect_matches[contestant2] = contestant1

        # Traverse through each key:value pair in the perfect matches dictionary and update the invalid matches attribute for each Contestant object
        for key in self._perfect_matches:
            for other in self._perfect_matches:
                if other != self._perfect_matches[key]:
                    key.set_invalid_match(other)
                if self._perfect_matches[other] != self._perfect_matches[key]:
                    key.set_invalid_match(self._perfect_matches[other])