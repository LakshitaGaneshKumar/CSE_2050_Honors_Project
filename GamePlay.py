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

    def create_matches(self):
        """Generates perfect matches and updates Contestant objects with their perfect match"""
        for i in range(self._num_pairs):
            contestant1 = self._contestants.pop()
            contestant2 = self._contestants.pop()

            contestant1.set_perfect_match(contestant2)
            contestant2.set_perfect_match(contestant1)

            self._perfect_matches[contestant1] = contestant2

    def increment_weeks(self):
        """Increment the number of weeks played"""
        self._weeks_played += 1