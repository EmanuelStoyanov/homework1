import unittest
import solution


class TestIsAnBn(unittest.TestCase):
    def test_one(self):
        self.assertTrue(solution.is_an_bn(""))

    def test_two(self):
        self.assertTrue(not solution.is_an_bn("rado"))

    def test_three(self):
        self.assertTrue(not solution.is_an_bn("aaabb"))

    def test_four(self):
        self.assertTrue(solution.is_an_bn("aaabbb"))

    def test_five(self):
        self.assertTrue(not solution.is_an_bn("aabbaabb"))

    def test_six(self):
        self.assertTrue(not solution.is_an_bn("bbbaaa"))

    def test_seven(self):
        self.assertTrue(solution.is_an_bn("aaaaabbbbb"))


if __name__ == '__main__':
    unittest.main()
