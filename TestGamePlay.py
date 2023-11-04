import unittest
from GamePlay import GamePlay

class TestGamePlay(unittest.TestCase):
    def setUp(self):
        """Test Initialization"""
        for i in range(100):
            self.GP = GamePlay(i)
            self.assertEqual(self.GP._num_contestants, i)
   
    # TODO
    def test_create_players(self):
        """Test Create Players"""
        self.GP = GamePlay(6)
        self.GP.create_players()


unittest.main()