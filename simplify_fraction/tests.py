import unittest
import solution


class TestSimplifyFraction(unittest.TestCase):
    def test_one(self):
        self.assertEqual((1, 3), solution.simplify_fraction((3, 9)))

    def test_two(self):
        self.assertEqual((1, 7), solution.simplify_fraction((1, 7)))

    def test_three(self):
        self.assertEqual((2, 5), solution.simplify_fraction((4, 10)))

    def test_four(self):
        self.assertEqual((3, 22), solution.simplify_fraction((63, 462)))




if __name__ == '__main__':
    unittest.main()
