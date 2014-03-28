import unittest
import solution


class TestPrepareMeal(unittest.TestCase):
    def test_one(self):
        self.assertEqual("eggs", solution.prepare_meal(5))

    def test_two(self):
        self.assertEqual("spam", solution.prepare_meal(3))

    def test_three(self):
        self.assertEqual("spam spam spam", solution.prepare_meal(27))

    def test_four(self):
        self.assertEqual("spam and eggs", solution.prepare_meal(15))

    def test_five(self):
        self.assertEqual("spam spam and eggs", solution.prepare_meal(45))

    def test_six(self):
        self.assertEqual("", solution.prepare_meal(7))


if __name__ == '__main__':
    unittest.main()