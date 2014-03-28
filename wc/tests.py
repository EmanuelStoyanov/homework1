import solution
import unittest
import sys

class WCTest(unittest.TestCase):

    def test_count_chars(self):
        sys.argv.append('chars')
        sys.argv.append('story.txt')
        self.assertEqual(1031, solution.main())

    def test_count_words(self):
        sys.argv[1] = 'words'
        sys.argv.append('story.txt')
        self.assertEqual(164, solution.main())

    def test_count_lines(self):
        sys.argv[1] = 'lines'
        sys.argv.append('story.txt')
        self.assertEqual(5, solution.main())


if __name__ == '__main__':
    unittest.main()