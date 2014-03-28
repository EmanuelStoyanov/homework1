import unittest
from solution import count_substrings


class CountSubstringsTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(2, count_substrings("This is a test string", "is"))
    def test_two(self):
        self.assertEqual(2, count_substrings("babababa", "baba"))
    def test_three(self):
        self.assertEqual(4, count_substrings("Python is an awesome language to program in!", "o"))
    def test_four(self):
        self.assertEqual(0, count_substrings("We have nothing in common!", "really?"))
    def test_five(self):
        self.assertEqual(2, count_substrings("This is this and that is this", "this"))

if __name__ == '__main__':
    unittest.main()
