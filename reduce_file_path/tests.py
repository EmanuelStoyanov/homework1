import unittest
import solution


class TestReduceFilePath(unittest.TestCase):
    def test_one(self):
        self.assertEqual("/", solution.reduce_file_path("/"))

    def test_two(self):
        self.assertEqual("/", solution.reduce_file_path("/srv/../"))

    def test_three(self):
        self.assertEqual("/srv/www/htdocs/wtf", solution.reduce_file_path("/srv/www/htdocs/wtf/"))

    def test_four(self):
        self.assertEqual("/srv/www/htdocs/wtf", solution.reduce_file_path("/srv/www/htdocs/wtf"))

    def test_five(self):
        self.assertEqual("/srv", solution.reduce_file_path("/srv/./././././"))

    def test_six(self):
        self.assertEqual("/etc/wtf", solution.reduce_file_path("/etc//wtf/"))

    def test_seven(self):
        self.assertEqual("/", solution.reduce_file_path("/etc/../etc/../etc/../"))

    def test_eight(self):
        self.assertEqual("/", solution.reduce_file_path("//////////////"))

    def test_nine(self):
        self.assertEqual("/", solution.reduce_file_path("/../"))




if __name__ == '__main__':
    unittest.main()
