import unittest
from solution import is_increasing


class IsIncreasingTest(unittest.TestCase):
    """docstring for IsIncreasingTest"""
    def test_one(self):
        self.assertTrue(is_increasing([1, 2, 3, 4, 5]))

    def test_two(self):
        self.assertTrue(is_increasing([1]))

    def test_three(self):
        self.assertFalse(is_increasing([5, 6, -10]))


if __name__ == '__main__':
    unittest.main()
