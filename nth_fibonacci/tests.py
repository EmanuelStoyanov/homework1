from solution import nth_fibonacci
import unittest


class FibonacciTest(unittest.TestCase):
	""" Testing nth Fibonacci number """
	def test_first_fibonacci(self): 
		self.assertEqual(1, nth_fibonacci(1))
	def test_second_fibonacci(self):	
		self.assertEqual(1, nth_fibonacci(2))
	def test_third_fibonacci(self):	
		self.assertEqual(2, nth_fibonacci(3))
	def test_tenth_fibonacci(self):	
		self.assertEqual(55, nth_fibonacci(10))


if __name__ == '__main__':
	unittest.main()
