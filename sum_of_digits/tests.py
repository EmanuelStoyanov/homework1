import unittest

import solution


class TestSumOfDigits(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution.sum_of_digits(1325132435356), 43)

    def test_two(self):
        self.assertEqual(solution.sum_of_digits(123), 6)

    def test_three(self):
        self.assertEqual(solution.sum_of_digits(6), 6)

    def test_four(self):
        self.assertEqual(solution.sum_of_digits(-10), 1)

if __name__ == '__main__':
    unittest.main()
