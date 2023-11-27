from Contestant import Contestant
import unittest

class TestContestant(unittest.TestCase):
    def setUp(self):
        """Sets up two Contestant objects for further testing"""
        self.person = Contestant("Jane Doe")
        self.person2 = Contestant("John Doe")

        self.invalid1 = Contestant("Invalid1")
        self.invalid2 = Contestant("Invalid2")
        self.invalid3 = Contestant("Invalid3")

    def test_name(self):
        """Test set and get name methods"""
        self.assertEqual(self.person.get_name(), "Jane Doe") 
        self.assertEqual(self.person2.get_name(), "John Doe") 

        self.person.set_name("Jane Doe 2")
        self.person2.set_name("John Doe 2")

        self.assertEqual(self.person.get_name(), "Jane Doe 2") 
        self.assertEqual(self.person2.get_name(), "John Doe 2") 
    
    def test_found_match(self):
        """Test set and get found match methods"""
        # Perfect matches are not found in the beginning, so check if found_match is False
        self.assertEqual(self.person.get_found_match(), False)
        self.assertEqual(self.person2.get_found_match(), False)

        self.person.set_found_match(True)
        self.person2.set_found_match(True)

        self.assertEqual(self.person.get_found_match(), True)
        self.assertEqual(self.person2.get_found_match(), True)
        self.assertNotEqual(self.person.get_found_match(), False)
        self.assertNotEqual(self.person2.get_found_match(), False)

    def test_perfect_match(self):
        """Test set and get perfect match methods"""
        self.assertEqual(self.person.get_perfect_match(), None)
        self.assertEqual(self.person2.get_perfect_match(), None)

        self.person.set_perfect_match(self.person2)
        self.person2.set_perfect_match(self.person)
        
        self.assertEqual(self.person.get_perfect_match(), self.person2)
        self.assertEqual(self.person2.get_perfect_match(), self.person)
    
    def test_invalid_matches(self):
        """Test set and get invalid matches methods"""
        self.assertEqual(self.person.get_invalid_matches(), set())
        self.assertEqual(self.person2.get_invalid_matches(), set())

        self.person.set_invalid_match(self.invalid1)
        self.person.set_invalid_match(self.invalid2)
        self.person.set_invalid_match(self.invalid3)

        self.person2.set_invalid_match(self.invalid1)
        self.person2.set_invalid_match(self.invalid2)
        self.person2.set_invalid_match(self.invalid3)

        self.assertEqual(self.person.get_invalid_matches(), {self.invalid1, self.invalid2, self.invalid3})
        self.assertEqual(self.person2.get_invalid_matches(), {self.invalid1, self.invalid2, self.invalid3})

    def test_current_partner(self):
        """Test set and get current partner methods"""
        self.assertEqual(self.person.get_current_partner(), None)
        self.assertEqual(self.person2.get_current_partner(), None)

        self.person.set_current_partner(self.person2)
        self.person2.set_current_partner(self.person)

        self.assertEqual(self.person.get_current_partner(), self.person2)
        self.assertEqual(self.person2.get_current_partner(), self.person)

    def test_known_invalid_matches(self):
        """Test set and get known invalid matches methods"""
        self.assertEqual(self.person.get_known_invalid_matches(), set())
        self.assertEqual(self.person2.get_known_invalid_matches(), set())

        self.person.set_known_invalid_match(self.person2)
        self.person2.set_known_invalid_match(self.person)

        self.assertEqual(self.person.get_known_invalid_matches(), {self.person2})
        self.assertEqual(self.person2.get_known_invalid_matches(), {self.person})

    # def test_possible_matches(self):
    #     """Test set and get possible matches methods"""
    #     self.assertEqual(self.person.get_possible_matches(), set())
    #     self.assertEqual(self.person2.get_possible_matches(), set())

    #     self.person.set_possible_match(self.person2)
    #     self.person2.set_possible_match(self.person)

    #     self.assertEqual(self.person.get_possible_matches(), {self.person2})
    #     self.assertEqual(self.person2.get_possible_matches(), {self.person})

unittest.main()