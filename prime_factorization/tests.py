import unittest
from solution import prime_factorization


class PrimeFactorizationTest(unittest.TestCase):
    """testing prime_factorization"""
    def test_one(self):
        self.assertEqual([(2, 1), (5, 1)], prime_factorization(10))

    def test_two(self):
        self.assertEqual([(2, 1), (7, 1)], prime_factorization(14))

    def test_three(self):
        self.assertEqual([(2, 2), (89, 1)], prime_factorization(356))

    def test_four(self):
        self.assertEqual([(89, 1)], prime_factorization(89))

    def test_five(self):
        self.assertEqual([(2, 3), (5, 3)], prime_factorization(1000))

if __name__ == '__main__':
    unittest.main()
