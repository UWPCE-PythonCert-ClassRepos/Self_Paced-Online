def fibonacci(n):
	return sum_series(n)

def lucas(n):
	return sum_series(n, 2, 1)

def sum_series(n, arg1 = 0, arg2 = 1):
	"""
	Provide fibonacci and lucas functionaalites
	The fuction has 3 arguments
	:param: n - nth vale in series
	:param: arg1 - identify fibonacci or lucas
	:param: arg2 - identify fibonacci or lucas
	"""
	# inonacci calculation
	if arg1 == 0 and arg2 == 1:
		if n  <= 1:
			return n
	# lucas calculation
	elif arg1 == 2 and arg2 == 1:
		if n == 0:
			return 2
		elif n == 1:
			return 1
	return sum_series(n-1, arg1,arg2) + sum_series(n-2, arg1, arg2)


if __name__ == "__main__":
	# fibonacci function test
	# test case: n = 0
	rtn = fibonacci(0)
	assert( rtn == 0)
	#test case: n = 1
	rtn = fibonacci(1)
	assert( rtn == 1)
	# tesy case: n = 6
	rtn = fibonacci(6)
	assert( rtn == 8)
	# test lucas function
	# test case: n = 0
	rtn = lucas(0)
	assert( rtn == 2)
	# test case n = 1
	rtn = lucas(1)
	assert( rtn == 1)
	#test case n=2
	rtn = lucas(2)
	assert( rtn == 3)
	#test case n = 5
	rtn = lucas(5)
	assert ( rtn == 11)


