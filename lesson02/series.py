#!/usr/bin/env Python3
import unittest

print("The following is a tool to determine either the sum of any Fibonacci/Lucas Series \n"
"or determine the value of a Fibonacci/Lucas Series at a specific index. \n"
"To determine the value of a specific term in a Fibonacci/Lucas Series, type '1'. \n"
"To compute the total sum of a Fibonacci/Lucas Series, type '2'.")
print('\n')
r = int(input("Your response:"))

def fib(n):
''' This function defines the computation for determining the value at
	a specific index in the Fibonacci the series.'''
	a = 0
	b = 1
	series = [a, b]
	if n == 1:
		print("The value of term", n, "in the Fibonacci Series is:", series[a])
	if n == 2:
	 	print("The value of term", n, "in the Fibonacci Series is:", series[b])
	# series = [a, b]
	for i in range(n-2):
		c = a + b
		series.append(c)
		a = b
		b = c

	print("The value of term", n, "in the Fibonacci Series is:", series[n-1])

def lucas(n):
''' This function defines the computation for determining the value at
	a specific index in the lucas series. '''
	a = 2
	b = 1
	series = [a, b]
	if n == 1:
		print("The value of term", n, "in the Lucas Series is:", series[a])	
	if n == 2:
		print("The value of term", n, "in the Lucas Series is:", series[b])
	# series = [a, b]
	for i in range(n-2):
		c = a + b
		series.append(c)
		a = b
		b = c

	print("The value of term", n, "in the Lucas Series is:", series[n-1])
		
def sumIt(n, a, b):
''' This function defines the computation for the summation of all terms
	in a series, given the first two terms. '''
	series = [a, b]
	if n == 1:
		print("The value of the first term is:", a)
	if n == 2:
		print("The sum of the first two terms is:", sum(series))
	for i in range(n-2):
		c = a + b 
		series.append(c)
		a = b 
		b = c 
		ss = sum(series)
	print("The value of term:", n, "is:", ss)


if r == 1:
	n = int(input("Enter the value of the term you wish to know:"))
	fib(n)
	lucas(n)

if r == 2:
	n = int(input("Enter the value of the term you wish to know:"))
	a = int(input("Enter the starting value of the first term:"))
	b = int(input("Enter the starting value of the second term:"))
	sumIt(n, a, b)

# Below are unit tests that are not working as intended.
# Test results return Assertion Errors.

# class TestFibbonaci(unittest.TestCase):

# 	def test_fib(self):
# 		""" Test for fibonacci series function. """
# 		result = Fibbonaci.fib(9)
# 		self.assertEqual(result, 21)

# 	def test_lucas(self):
# 		""" Test for lucas series function. """
# 		testLucas = Fibbonaci.lucas(13)
# 		self.assertEqual(testLucas, 123)

# 	def test_sumIt(self):
# 		""" Test for summation of series given first two terms.  """
# 		result = Fibbonaci.sumIt(8, 2, 1)
# 		self.assertEqual(result, 29)

# if __name__ == '__main__':
# 	unittest.main()

		