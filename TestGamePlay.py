import unittest
from GamePlay import GamePlay
from Contestant import Contestant

class TestGamePlay(unittest.TestCase):
    def setUp(self):
        """Test Initialization"""
        for i in range(100):
            self.GP = GamePlay(i)
            self.assertEqual(self.GP._num_contestants, i)
        self.GP = GamePlay(6)
   
    def test_add_contestant(self):
        """Test Create Players"""
        n = 100
        self.players = []

        for i in range(n):
            self.GP.add_contestant(f"{i}")
            self.players.append(f"{i}")

        self.assertEqual(len(self.players), len(self.GP._contestants))
        
        for contestant in self.GP._contestants:
            assert contestant.get_name() in self.players

unittest.main()