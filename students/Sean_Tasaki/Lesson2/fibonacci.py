def fibonacci(n):
	"""Return the nth value in the fibonacci sequence (starting with zero index.
    """
	if n == 1:
		return 1
	if n == 0:
		return 0
	if n < 0:
		print("Invalid data")
	else:
		return fibonacci(n - 2) + fibonacci(n - 1)

def lucas(n):
	"""Return the nth value in the Lucas numbers series (starting with zero index.
	"""
	if n == 1:
		return 1
	if n == 0:
		return 2
	if n < 0:
		print("Invalid data")     
	else:
		return lucas(n - 2) + lucas(n - 1)

def sum_series(n, index0 = 0, index1 = 1):
	"""Return the nth value in a series. The default parameter values set to calculate
	fobonacci series. Calling with optional arguments index0 = 2 and index1 = 1
	will calculate lucas series.
	"""
	# Calculates fibonacci series
	if (index0 == 0 and index1 == 1):
		if n == 1:
			return 1
		if n == 0:
			return 0
			if n < 0:
				print("Invalid data")
		else:
			return fibonacci(n - 2) + fibonacci(n - 1)
    # Calculates lucas series
	elif (index0 == 2 and index1 == 1):
		if n == 1:
			return 1
		if n == 0:
			return 2
		if n < 0:
			print("Invalid data")     
		else:
			return lucas(n - 2) + lucas(n - 1)	

# Test the fibonacci function.
assert fibonacci(2) == 1
assert fibonacci(6) == 8
assert fibonacci(7) == 13

# Test the lucas function
assert lucas(2) == 3
assert lucas(6) == 18
assert lucas(7) == 29

# Test sum_series with default parameters
assert sum_series(2) == 1
assert sum_series(6) == 8
assert sum_series(7) == 13

# Test sum_series as a Fibonacci sequence
assert sum_series(2, 0, 1) == 1
assert sum_series(6, 0, 1) == 8
assert sum_series(7, 0, 1) == 13

# Test sum_series as a Lucas sequence
assert sum_series(2, 2, 1) == 3
assert sum_series(6, 2, 1) == 18
assert sum_series(7, 2, 1) == 29
