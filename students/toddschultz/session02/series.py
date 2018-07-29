
def fibonacci(n):
	"""
	This function will return the nth number in the numeric set, assuming a 0 index.

	The fibinacci series is naturally recursive – the value is defined by previous values:
	fib(n) = fib(n-2) + fib(n-1)
	"""
	a, b, i, fib = 0, 1, 1, [1,1]
	while i < n:
		fib.append(fib[a] + fib[b])
		a += 1
		b += 1
		i += 1
	return(fib[-1])

def lucas(n):
	"""
	This function will return the nth number in the numeric set, assuming a 0 index.

	The Lucas Numbers are a fibinacci related series of integers that start with the values 2 and 1
	"""
	a, b, i, luc = 0, 1, 1, [2,1]
	while i < n:
		luc.append(luc[a] + luc[b])
		a += 1
		b += 1
		i += 1
	return(luc[-1])

def sum_series(n, a=1, b=1):
	"""
	This funcation will return the nth string based on starting numbers dictated by input parameters, or use default.
	"""
	i = 2
	ss = [a,b]
	while i <= n:
		ss.append(ss[i-1] + ss[i-2])
		i += 1
	return(ss[-1])

#Asserts

assert fibonacci(1) == 1
assert fibonacci(4) == 5
assert fibonacci(10) == 89
assert fibonacci(100) == 573147844013817084101

assert lucas(1) == 1
assert lucas(4) == 7
assert lucas(10) == 123
assert lucas(100) == 792070839848372253127

assert sum_series(4) == 5
assert sum_series(4, 10, 12) == 56
assert sum_series(0, 99) == 1




