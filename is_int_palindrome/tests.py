import unittest
from solution import is_int_palindrome


class IsIntPalindromeTest(unittest.TestCase):
    def test_one(self):
        self.assertTrue(is_int_palindrome(100001))

    def test_two(self):
        self.assertFalse(is_int_palindrome(42))

    def test_three(self):
        self.assertTrue(is_int_palindrome(100001))

    def test_four(self):
        self.assertTrue(is_int_palindrome(999))

    def test_five(self):
        self.assertFalse(is_int_palindrome(123))

if __name__ == '__main__':
    unittest.main()
