## Ian Letourneau
## 4/25/2018
## A script that takes parameters and returns values at nth point in either a fibonacci or lucas sequence

def fibonacci(n):
	"""A function to return the nth number in the Fibonacci sequence"""
	if not n:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
	"""A function to return the nth number in the Lucas Numbers"""
	if n == 0:
		return 2
	elif n == 1:
		return 1
	else:
		return lucas(n-1) + lucas(n-2)

def sum_series(n, n0=0, n1=1):
	"""A function that takes an input n, n0, and n1 parameters and returns the nth value based on given parameters.

		:param n0=0: value of zeroth element in the series
		:param n1=1: value of first element in the series

		if default values are unchanged, return fibonacci sequence
		if n0==2 and n1==1, return lucas numbers sequence
		if n0==x and n1==y, return nth number beginning at x and y"""

	if n == 0:
		return n0
	elif n == 1:
		return n1
	else:
		return sum_series(n-1, n0, n1) + sum_series(n-2, n0, n1)



if __name__ == "__main__":
    # run tests on the fibonacci function
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # run tests on the lucas numbers function
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    # run tests on the sum_series function, ensuring default values return fibonacci sequence
    assert sum_series(5) == fibonacci(5)

    # run tests on the sum_series function, ensuring that adding Lucas Number initial values return Lucas Number sequence
    assert sum_series(5, 2, 1) == lucas(5)

    # run tests on the sum_series function, ensuring that adding any two numbers as n0 and n1 will return the nth number of a sequence starting with given values
    assert sum_series(2,25,32) == 57

    print("tests passed")