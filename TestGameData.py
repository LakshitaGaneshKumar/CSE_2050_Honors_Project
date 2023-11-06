import unittest
from GameData import GameData
from Contestant import Contestant

class TestGameData(unittest.TestCase):
    def setUp(self):
        """Test Initialization"""
        for i in range(100):
            self.game = GameData(i)
            self.assertEqual(self.game.get_num_contestants(), i)
        
        # Manually create sixteen contestants
        self.num_contestants = 16
        self.game = GameData(self.num_contestants)
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
        self.game1 = GameData(n)

        for i in range(n):
            self.game1.add_contestant(f"{i}")
            self.players.append(f"{i}")

        self.assertEqual(len(self.players), len(self.game1.get_contestants()))
        
        for contestant in self.game1.get_contestants():
            assert contestant.get_name() in self.players

    def test_create_perfect_matches(self):
        """Test Create Perfect Matches"""
        n = 16
        self.game2 = GameData(n)
        for i in range(n):
            self.game2.add_contestant(f"{i}")

        self.game2.create_perfect_matches()

        for contestant in self.game2.get_contestants():
            self.assertEqual(self.game2.get_perfect_matches()[contestant], contestant.get_perfect_match())
            self.assertEqual(len(contestant.get_invalid_matches()), n-1)
            assert contestant.get_perfect_match() not in contestant.get_invalid_matches()

    def test_pair_current_matches(self):
        """Test Create Known Matches"""
        n = 10000000

        self.contestants[0].set_found_match(True)
        self.contestants[1].set_found_match(True)

        self.contestants[4].set_known_invalid_match(self.contestants[2])
        self.contestants[4].set_known_invalid_match(self.contestants[6])
        self.contestants[4].set_known_invalid_match(self.contestants[7])

        self.contestants[3].set_known_invalid_match(self.contestants[4])
        self.contestants[3].set_known_invalid_match(self.contestants[5])
        self.contestants[3].set_known_invalid_match(self.contestants[6])

        self.contestants[5].set_known_invalid_match(self.contestants[3])
        self.contestants[5].set_known_invalid_match(self.contestants[6])
        self.contestants[5].set_known_invalid_match(self.contestants[7])

        for i in range(n):
            self.game.pair_current_matches()

            self.assertEqual(self.contestants[0].get_current_partner(), self.contestants[0].get_perfect_match())
            self.assertEqual(self.contestants[1].get_current_partner(), self.contestants[1].get_perfect_match())

            self.assertNotEqual(self.contestants[4].get_current_partner(), self.contestants[2])
            self.assertNotEqual(self.contestants[4].get_current_partner(), self.contestants[6])
            self.assertNotEqual(self.contestants[4].get_current_partner(), self.contestants[7])

            self.assertNotEqual(self.contestants[3].get_current_partner(), self.contestants[4])
            self.assertNotEqual(self.contestants[3].get_current_partner(), self.contestants[5])
            self.assertNotEqual(self.contestants[3].get_current_partner(), self.contestants[6])

            self.assertNotEqual(self.contestants[5].get_current_partner(), self.contestants[3])
            self.assertNotEqual(self.contestants[5].get_current_partner(), self.contestants[6])
            self.assertNotEqual(self.contestants[5].get_current_partner(), self.contestants[7])

unittest.main()