import unittest
from solution import biggest_difference


class BiggestDifferenceTest(unittest.TestCase):
    """docstring for BiggestDifferenceTest"""
    def test_one(self):
        self.assertEqual(-1, biggest_difference([1, 2]))

    def test_two(self):
        self.assertEqual(-4, biggest_difference([1, 2, 3, 4, 5]))

    def test_three(self):
        self.assertEqual(-9, biggest_difference([-10, -9, -1]))

    def test_four(self):
        self.assertEqual(-99, biggest_difference(range(100)))

if __name__ == '__main__':
    unittest.main()
