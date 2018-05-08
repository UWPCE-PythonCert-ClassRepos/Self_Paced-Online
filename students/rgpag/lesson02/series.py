def fibonacci(n):
	"""fibonacci(n) - return "n"th value of the fibonacci series"""
	'''fibL1=1
	fibL2=0
	if n<0:
		print("please enter positive int value")

	elif n==0:
		return 0

	elif n==1:
		return 1

	else:
		for i in range(n-1):
			fibC=fibL1+fibL2
			fibL2=fibL1
			fibL1=fibC
		return fibC
		'''
	return sum_series(n)

def lucas(n):
	"""lucas(n) - return "n"th value of the lucas series"""
	'''
	lucL1=1
	lucL2=2
	if n<0:
		print("please enter positive int value")

	elif n==0:
		return 2

	elif n==1:
		return 1

	else:
		for i in range(n-1):
			lucC=lucL1+lucL2
			lucL2=lucL1
			lucL1=lucC
		return lucC
	'''
	return sum_series(n,2,1)

def sum_series(n,v1=0,v2=1):
	"""sum series(n,v1=0,v2=1) - return "n"th value of sum series having v1 and v2 as first and second values"""
	L1=v2
	L2=v1
	if n<0:
		print("please enter positive int value")

	elif n==0:
		return v1

	elif n==1:
		return v2

	else:
		for i in range(n-1):
			C=L1+L2
			L2=L1
			L1=C
		return C


#assert statements for testing
assert sum_series(10)+sum_series(11)==sum_series(12) #test sum_series is a series of sums
assert fibonacci(5)==5 #test fibonacci(5) returns 5th element of fibonacci sequence
assert lucas(5)==11 #test lucas(5) returns 5th element of lucas series
assert sum_series(5) == 5 #test sum_series(5) returns 5th element of fibonacci sequence
assert sum_series(5,2,1) == 11 #test sum_series(5,2,1) returns 5th element of lucas series