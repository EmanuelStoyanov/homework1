import unittest
from solution import prime_number_of_divisors


class PrimeNumberOfDivisorsTest(unittest.TestCase):
    def test_one(self):
        self.assertTrue(prime_number_of_divisors(7))
    def test_two(self):
        self.assertFalse(prime_number_of_divisors(8))
    def test_three(self):
        self.assertTrue(prime_number_of_divisors(9))

if __name__ == '__main__':
      unittest.main()  
        
