import unittest
from solution import what_is_my_sign


class WhatIsMySignTest(unittest.TestCase):
    """testing what_is_my_sign"""
    def test_leo(self):
        self.assertEqual("Leo", what_is_my_sign(5, 8))

    def test_aquarius(self):
        self.assertEqual("Aquarius", what_is_my_sign(29, 1))

    def test_cancer(self):
        self.assertEqual("Cancer", what_is_my_sign(30, 6))

    def test_gemini(self):
        self.assertEqual("Gemini", what_is_my_sign(31, 5))

    def test_aquarius2(self):
        self.assertEqual("Aquarius", what_is_my_sign(2, 2))

    def test_taurus(self):
        self.assertEqual("Taurus", what_is_my_sign(8, 5))

    def test_capricorn(self):
        self.assertEqual("Capricorn", what_is_my_sign(9, 1))

if __name__ == '__main__':
    unittest.main()
