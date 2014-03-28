import solution
import unittest
import sys

class CatTest(unittest.TestCase):

    def setUp(self):
        sys.argv.append('file.txt')
        self.filename = sys.argv[1]
        self.file = open(self.filename, 'r')
        self.content = self.file.read()

    def test_cat(self):
        self.assertEqual(self.content, solution.main())

    def tearDown(self):
        self.file.close()


if __name__ == '__main__':
    unittest.main()