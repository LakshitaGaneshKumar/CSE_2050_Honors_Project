from Contestant import Contestant

class GameData():
    def __init__(self, num_contestants):
        self._num_contestants = num_contestants
        self._num_pairs = self._num_contestants // 2
        self._contestants = set()
        self._perfect_matches = {}
        self._current_pairs = {}
        self._contestants_to_objects = {}
        self._weeks_played = 0
        self._paired = set()

    def add_contestant(self, contestant):
        """Takes in a contestant name, creates a new Contestant object, and adds it to the set of current contestant"""
        player = Contestant(contestant)
        self._contestants.add(player)
        self._contestants_to_objects[contestant] = player

    def get_contestants(self):
        """Returns the set of all Contestant objects in the current game play"""
        return self._contestants
    
    def get_contestants_to_objects(self):
        """Returns the dictionary of all key:value pairs that map a string representation of a contestant's name to their Contestant object"""
        return self._contestants_to_objects

    def get_num_contestants(self):
        """Returns the number of contestants"""
        return self._num_contestants
    
    def get_num_pairs(self):
        """Returns the number of pairs"""
        return self._num_pairs
    
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

    def update_database(self, contestant, match):
        """Takes in a contestant and their current partner/match and updates the game database"""
        # Update each Contestant object with their current partners
        contestant.set_current_partner(match)
        match.set_current_partner(contestant)

        # Update set of paired contestant
        self._paired.add(contestant)
        self._paired.add(match)

        # Update current pairs dictionary
        self._current_pairs[contestant] = match
        self._current_pairs[match] = contestant

    def pair_known_perfect_matches(self):
        """Pairs up perfect matches that are already found in the game play"""
        for contestant in self._contestants:
            if contestant not in self._paired and contestant.get_found_match():
                # Extract contestant's match
                match = contestant.get_perfect_match()
                
                # Update database
                self.update_database(contestant, match)
    
    def pair_other_matches(self):
        """Pairs up the rest of the contestants who haven't found their perfect match yet"""
        self.contestants_copy = self._contestants.copy()

        for contestant in self._contestants:
            if contestant not in self._paired:
                invalids = contestant.get_known_invalid_matches()
                match = self.contestants_copy.pop()

                # Find a potential match
                while((match in self._paired or match in invalids or match == contestant) and len(self.contestants_copy) > 0):
                    match = self.contestants_copy.pop()

                # Update database
                self.update_database(contestant, match)

    def pair_current_matches(self):
        """Pairs the matches for the current week"""
        self._paired = set()
        self.pair_known_perfect_matches()
        self.pair_other_matches()