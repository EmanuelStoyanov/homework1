import unittest
import solution


class TestNthFibLists(unittest.TestCase):
    def test_one(self):
        self.assertEqual([1], solution.nth_fib_lists([1], [2], 1))

    def test_two(self):
        self.assertEqual([2], solution.nth_fib_lists([1], [2], 2))

    def test_three(self):
        self.assertEqual([1, 2, 1, 3], solution.nth_fib_lists([1, 2], [1, 3], 3))

    def test_four(self):
        self.assertEqual([1, 2, 3, 1, 2, 3], solution.nth_fib_lists([], [1, 2, 3], 4))

    def test_five(self):
        self.assertEqual([], solution.nth_fib_lists([], [], 100))


if __name__ == '__main__':
    unittest.main()
