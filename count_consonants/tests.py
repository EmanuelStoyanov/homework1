import unittest
from solution import count_consonants


class CountConsonantsTest(unittest.TestCase):
    """testing count_consonants"""
    def test_one(self):
        self.assertEqual(4, count_consonants("Python"))

    def test_with_the_volcano_name(self):
        self.assertEqual(11, count_consonants("Theistareykjarbunga"))

    def test_three(self):
        self.assertEqual(7, count_consonants("grrrrgh!"))

    def test_four(self):
        self.assertEqual(44, count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

    def test_five(self):
        self.assertEqual(6, count_consonants("A nice day to code!"))

if __name__ == '__main__':
    unittest.main()
