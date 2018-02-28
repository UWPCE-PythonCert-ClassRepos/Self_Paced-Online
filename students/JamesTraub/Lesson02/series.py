# Create a new module series.py in the lesson02 folder in your student folder.
# In it, add a function called fibonacci.
# The function should have one parameter, n.
# The function should return the nth value in the fibonacci series (starting with zero index)
# Ensure that your function has a well-formed docstring
# Note that the fibinacci series is naturally recursive – the value is defined by previous values:

# fib(n) = fib(n-2) + fib(n-1)


def fibinacci(n):
	fibi = [0,1]
	if n == 0:
		print(fibi[0])
		return(0)
	elif n == 1:
		print(fibi[1])
		return(1)
	else:
		for i in range(n):
			small_fib = fibi[i]
			range_plus1 = i + 1
			big_fib = fibi[range_plus1]
			next_fib = small_fib + big_fib
			fibi.append(next_fib)
		fib_minus2 = (n-2)
		fib_minus1 = (n-1)
		fib_nth = fibi[fib_minus2] + fibi[fib_minus1]
		print(fib_nth)


fibinacci(2)