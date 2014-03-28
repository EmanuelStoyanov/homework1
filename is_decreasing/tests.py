import unittest
from solution import is_decreasing


class IsIncreasingTest(unittest.TestCase):
    """docstring for IsIncreasingTest"""
    def test_one(self):
        self.assertTrue(is_decreasing([5, 4, 3, 2, 1]))

    def test_two(self):
        self.assertTrue(is_decreasing([100, 50, 20]))

    def test_three(self):
        self.assertFalse(is_decreasing([1, 2, 3]))

    def test_four(self):
        self.assertFalse(is_decreasing([1, 1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
