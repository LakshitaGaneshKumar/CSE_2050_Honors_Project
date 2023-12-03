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
            self.game._contestants.append(self.contestants[i])
            if i % 2 == 0:
                self.contestants[i].set_perfect_match(self.contestants[i+1])
            else:
                self.contestants[i].set_perfect_match(self.contestants[i-1])
        
        print("Set up works")

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

        print("adding works")

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
        
        print("Create mathces works")

    def test_update_possible_matches(self):
        """Test Update Possible Matches"""
        self.game._weeks_played = 0
        self.game.update_possible_matches()

        for contestant in self.contestants:
            copy = self.contestants.copy()
            copy.remove(contestant)
            self.assertEqual(contestant.get_possible_matches(), copy)
    
        self.game._weeks_played = 1

        self.contestants[0].set_found_match(True)
        self.contestants[1].set_found_match(True)

        self.contestants[4].set_known_invalid_match(self.contestants[2])
        self.contestants[4].set_known_invalid_match(self.contestants[6])
        self.contestants[4].set_known_invalid_match(self.contestants[7])

        copy_for_4 = self.contestants.copy()
        copy_for_4.remove(self.contestants[2])
        copy_for_4.remove(self.contestants[6])
        copy_for_4.remove(self.contestants[7])

        self.contestants[3].set_known_invalid_match(self.contestants[4])
        self.contestants[3].set_known_invalid_match(self.contestants[5])
        self.contestants[3].set_known_invalid_match(self.contestants[6])

        copy_for_3 = self.contestants.copy()
        copy_for_3.remove(self.contestants[4])
        copy_for_3.remove(self.contestants[5])
        copy_for_3.remove(self.contestants[6])

        self.contestants[5].set_known_invalid_match(self.contestants[3])
        self.contestants[5].set_known_invalid_match(self.contestants[6])
        self.contestants[5].set_known_invalid_match(self.contestants[7])

        copy_for_5 = self.contestants.copy()
        copy_for_5.remove(self.contestants[3])
        copy_for_5.remove(self.contestants[6])
        copy_for_5.remove(self.contestants[7])

        self.game.update_possible_matches()

        self.assertEqual(self.contestants[0].get_possible_matches(), [self.contestants[1]])
        self.assertEqual(self.contestants[1].get_possible_matches(), [self.contestants[0]])

        self.assertEqual(self.contestants[4].get_possible_matches(), copy_for_4)
        self.assertEqual(self.contestants[3].get_possible_matches(), copy_for_3)
        self.assertEqual(self.contestants[5].get_possible_matches(), copy_for_5)

        print("this works")

    def test_pair_current_matches1(self):
        """Tests Create Current Matches where all contestants ahve found their perfect match"""
        for contestant in self.contestants:
            contestant.set_found_match(True)

        self.game.pair_current_matches()

        for contestant in self.contestants:
            self.assertEqual(contestant.get_current_partner(), contestant.get_perfect_match())

    def test_pair_current_matches2(self):
        """Test create current matches where only some of the contestants have found their perfect match"""
       
        self.game._weeks_played = 1

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

        self.game.update_possible_matches()
        self.game.pair_current_matches()

        self.assertEqual(self.contestants[0].get_current_partner(), self.contestants[1])
        self.assertEqual(self.contestants[1].get_current_partner(), self.contestants[0])

        self.assertNotEqual(self.contestants[4].get_current_partner(), self.contestants[4])
        self.assertNotEqual(self.contestants[4].get_current_partner(), self.contestants[2])
        self.assertNotEqual(self.contestants[4].get_current_partner(), self.contestants[6])
        self.assertNotEqual(self.contestants[4].get_current_partner(), self.contestants[7])

        self.assertNotEqual(self.contestants[3].get_current_partner(), self.contestants[3])
        self.assertNotEqual(self.contestants[3].get_current_partner(), self.contestants[4])
        self.assertNotEqual(self.contestants[3].get_current_partner(), self.contestants[5])
        self.assertNotEqual(self.contestants[3].get_current_partner(), self.contestants[6])

        self.assertNotEqual(self.contestants[5].get_current_partner(), self.contestants[5])
        self.assertNotEqual(self.contestants[5].get_current_partner(), self.contestants[3])
        self.assertNotEqual(self.contestants[5].get_current_partner(), self.contestants[6])
        self.assertNotEqual(self.contestants[5].get_current_partner(), self.contestants[7]) 

        print("pair current matches works")

unittest.main()