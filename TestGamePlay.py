import unittest
from GamePlay import GamePlay
from Contestant import Contestant

class TestGamePlay(unittest.TestCase):
    def setUp(self):
        """Test Initialization"""
        for i in range(100):
            self.game = GamePlay(i)
            self.assertEqual(self.game.get_num_contestants(), i)
        
        # Manually create sixteen contestants
        self.num_contestants = 16
        self.game = GamePlay(self.num_contestants)
        self.contestants = [Contestant("Bob"), Contestant("Ryan"), Contestant("Dylan"), Contestant("Emma"), Contestant("Lucy"), Contestant("Tori"), 
                            Contestant("Luke"), Contestant("Evan"), Contestant("Eve"), Contestant("Lana"), Contestant("Ari"), Contestant("Grace"),
                            Contestant("Bob2"), Contestant("Ryan2"), Contestant("Dylan2"), Contestant("Emma2")]
        
        # Manually pair them up and add them to the game play
        for i in range(len(self.contestants)):
            self.game._contestants.add(self.contestants[i])
            if i % 2 == 0:
                self.contestants[i].set_perfect_match(self.contestants[i+1])
            else:
                self.contestants[i].set_perfect_match(self.contestants[i-1])

    def test_add_contestant(self):
        """Test Create Players"""
        n = 16
        self.players = []
        self.game1 = GamePlay(n)

        for i in range(n):
            self.game1.add_contestant(f"{i}")
            self.players.append(f"{i}")

        self.assertEqual(len(self.players), len(self.game1.get_contestants()))
        
        for contestant in self.game1.get_contestants():
            assert contestant.get_name() in self.players

    def test_create_perfect_matches(self):
        """Test Create Perfect Matches"""
        n = 16
        self.game2 = GamePlay(n)
        for i in range(n):
            self.game2.add_contestant(f"{i}")

        self.game2.create_perfect_matches()

        for contestant in self.game2.get_contestants():
            self.assertEqual(self.game2.get_perfect_matches()[contestant], contestant.get_perfect_match())
            self.assertEqual(len(contestant.get_invalid_matches()), n-1)
            assert contestant.get_perfect_match() not in contestant.get_invalid_matches()

    def test_create_known_matches(self):
        """Test Create Known Matches"""
        self.contestants[0].set_found_match(True)
        self.contestants[1].set_found_match(True)

        self.game.pair_known_perfect_matches()

        self.assertEqual(self.contestants[0].get_current_partner(), self.contestants[0].get_perfect_match())
        self.assertEqual(self.contestants[1].get_current_partner(), self.contestants[1].get_perfect_match())
        
        for i in range(2, self.num_contestants):
            self.assertEqual(self.contestants[i].get_current_partner(), None)

unittest.main()