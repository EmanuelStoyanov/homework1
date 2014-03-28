import unittest
import solution


class TestUniqueWordsCount(unittest.TestCase):

    def test_one(self):
        self.assertEqual(3, solution.unique_words_count(["apple", "banana", "apple", "pie"]))

    def test_two(self):
        self.assertEqual(2, solution.unique_words_count(["python", "python", "python", "ruby"]))

    def test_three(self):
        self.assertEqual(1, solution.unique_words_count(["HELLO!"] * 10))

if __name__ == '__main__':
    unittest.main()