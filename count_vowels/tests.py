import unittest
from solution import count_vowels


class CountVowelsTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(2, count_vowels("Python"))

    def test_two(self):
        self.assertEqual(8, count_vowels("Theistareykjarbunga"))

    def test_three(self):
        self.assertEqual(0, count_vowels("grrrrgh!"))

    def test_four(self):
        self.assertEqual(22, count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))

    def test_five(self):
        self.assertEqual(8, count_vowels("A nice day to code!")) 

if __name__ == '__main__':
    unittest.main()
