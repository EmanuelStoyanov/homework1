import solution
import unittest
import sys

class Cat2Test(unittest.TestCase):

    def setUp(self):
        sys.argv.append('file.txt')
        self.filename1 = sys.argv[1]
        self.f = open(self.filename1, 'r')


        sys.argv.append('file2.txt')
        self.filename2 = sys.argv[2]
        self.f2 = open(self.filename2, 'r')

        self.content = []
        
        self.file_in = self.f.read()
        self.content.append(self.file_in)
        self.file_in = self.f2.read()
        self.content.append(self.file_in)

    def test_cat2(self):
        self.assertEqual('\n'.join(self.content), solution.main())

    def tearDown(self):
        self.f.close()
        self.f2.close()


if __name__ == '__main__':
    unittest.main()
