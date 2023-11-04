class Contestant():
    def __init__(self, name):
        """Initialize a Contestant Object"""
        self._name = name
        self._found_match = False
        self._perfect_match = None
        self._invalid_matches = set()
        self._current_partner = None
        self._known_invalid_matches = set()
        self._possible_matches = set()

    def set_name(self, name): 
        """Sets a new value for name"""
        self._name = name

    def get_name(self): 
        """Returns name"""
        return self._name

    def set_found_match(self, found_match):
        """Takes in a boolean for if the perfect match has been found and updates the found match attribute"""
        self._found_match = found_match

    def get_found_match(self): 
        """Returns if the contestant's perfect match has been found"""
        return self._found_match

    def set_perfect_match(self, perfect_match):
        """Takes in a Contestant object and sets it equal to the current Contestant's perfect match"""
        self._perfect_match = perfect_match

    def get_perfect_match(self):
        """Returns contestant's perfect match"""
        return self._perfect_match
    
    def set_invalid_match(self, invalid_match): 
        """Takes in a Contestant object as an invalid match and adds it to the list of invalid matches"""
        self._invalid_matches.add(invalid_match)

    def get_invalid_matches(self):
        """Returns the set of invalid matches"""
        return self._invalid_matches

    def set_current_partner(self, current_partner): 
        """Takes in a Contestant object and sets it equal to the current Contestant's current partner"""
        self._current_partner = current_partner

    def get_current_partner(self):
        """Returns contestant's current partner"""
        return self._current_partner

    def set_known_invalid_match(self, invalid_match): 
        """Takes in a Contestant object and adds it to the set of known invalid matches"""
        self._known_invalid_matches.add(invalid_match)

    def get_known_invalid_matches(self): 
        """Returns the set of known invalid matches"""
        return self._known_invalid_matches

    def set_possible_match(self, possible_match): 
        """Takes in a Contestant object and adds it to the set of possible matches, which includes every contestant who is not known to be an invalid match"""
        self._possible_matches.add(possible_match)

    def get_possible_matches(self): 
        """Returns the set of possible matches"""
        return self._possible_matches