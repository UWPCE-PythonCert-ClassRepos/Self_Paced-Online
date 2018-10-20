#lesson 2, assignment fibonacci series

def fibonacci(n):
	"""
	Return the nth value of the fibonaaci sequence using recursion. The function
	calls it self until it has finished (n=0). This sequence starts with 0 and 1.

	:param n: The number within in the fibonacci sequence you wish to extract.
	"""
	if(n<=1):
		return n
	else:
		return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):
	"""
	Return the nth value of the lucas sequence using recursion. The function
	calls it self until it has finished (n=0). This sequence starts with 2 and 1.

	:param n: The number within in the lucas sequence you wish to extract.
	"""
	if(n==0):
		return 2
	elif(n==1):
		return 1
	else:
		return lucas(n-2) + lucas(n-1)


def sum_series(n, y=0, z=1):
	"""
	Return the nth value of of either the fibonacci or lucas sequence using recursion. The function
	calls it self until it has finished (n=0). The default is fibonacci.

	:param n: The number within in the sequence you wish to extract.
	:param y: The starting number of the sequence (default fibonacci).
	:param z: The second number of the sequence (default fibonacci)
	"""
	if(n==0):
		return y
	elif(n==1):
		return z
	else:
		return sum_series(n-2, y, z) + sum_series(n-1, y, z)


#define the main function
def main():
	"""
	This is the main function that calls the program
	"""

	#test the program
	print("Starting Test:")

	#test the basics
	assert fibonacci(10) == 55
	assert lucas(10) == 123

	#test the default of sum_series
	assert sum_series(5) == 5

	#test the lucas version of sum_series
	assert sum_series(5,2,1) == 11

	#test a random sequence
	assert sum_series(5, 3, 5) == 34

	#finish testing
	print("Test completed successfully :)")


#call the main function
main()
