import unittest
import solution
import sys

class TestSum(unittest.TestCase):

    def setUp(self):
        sys.argv.append('numbers.txt')

    def test_sum(self):
        self.assertEqual(47372, solution.main())

if __name__ == '__main__':
    unittest.main()