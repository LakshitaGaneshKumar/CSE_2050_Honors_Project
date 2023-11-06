import unittest
from GamePlay import GamePlay
from Contestant import Contestant

class TestGamePlay(unittest.TestCase):
    def setUp(self):
        """Test Initialization"""
        for i in range(100):
            self.game = GamePlay(i)
            self.assertEqual(self.game.get_num_contestants(), i)
        
        self.game = GamePlay(16)

    def test_add_contestant(self):
        """Test Create Players"""
        n = 16
        self.players = []

        for i in range(n):
            self.game.add_contestant(f"{i}")
            self.players.append(f"{i}")

        self.assertEqual(len(self.players), len(self.game.get_contestants()))
        
        for contestant in self.game.get_contestants():
            assert contestant.get_name() in self.players

    def test_create_perfect_matches(self):
        """Test Create Matches"""
        n = 16
        for i in range(n):
            self.game.add_contestant(f"{i}")

        self.game.create_perfect_matches()

        for contestant in self.game.get_contestants():
            self.assertEqual(self.game.get_perfect_matches()[contestant], contestant.get_perfect_match())
            self.assertEqual(len(contestant.get_invalid_matches()), n-1)
            assert contestant.get_perfect_match() not in contestant.get_invalid_matches()

unittest.main()