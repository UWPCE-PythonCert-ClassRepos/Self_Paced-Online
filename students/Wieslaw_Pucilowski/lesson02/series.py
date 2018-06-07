__author__="Wieslaw Pucilowski"

def fibonacci(n):
	"""
	Fibonacci function return the nth value in the fibonacci series (starting with zero index)
	"""
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
	
def lucas(n):
	"""
	Lucas series
	"""
	if n == 0:
		return 2
	elif n == 1:
		return 1
	else:
		return lucas(n-1) + lucas(n-2)

# TODO finish sum_series() mind not to use functions defined above, instead create new one based on common formula: sum_series(n) = sum_series(n-1) + sum_series(n-2)

def sum_series(n,x=0, y=1):
	# fibonacci 0, 1, 1
	# lucas		2, 1, 3
	# x, y are two first elements of the series default 0,1 => fibonacci, then 2,1 => lucas, else other series
	if n == 0:
		return x
	elif n == 1:
		return y
	else:
		return sum_series(n-1,x,y) + sum_series(n-2,x,y)


def main():
	print("testing Fibonacci series...")
	n = input("Please enter n integer for Fibonacci: ")
	n=int(n)
	print('fibonacci(n) = fibonacci(n-2)+fibonacci(n-1)')
	print('Fibonacci for ',n,' should be fibonacci(',n-2,') + fibonacci(',n-1,') :', fibonacci(n-2),' + ',fibonacci(n-1),': and fibonacci(',n,') returns: ', fibonacci(n))
	print('Fibonacci sequence for:',n)
	for i in range(n):
		print('For n='+str(i),'fibonacci(n)=', fibonacci(i))
	# assert testing fibonacci(n) for first 10 elements, if fails then AssertionError is raised
	fib10 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
	for i in range(10):
		assert fibonacci(i) == fib10[i]
	
	print()
	print("Testing Lucas sequence...")
	n = input("Please enter n integer for Lucas: ")
	n=int(n)
	print('Lucas sequence for:',n)
	for i in range(n):
		print('For n='+str(i),'lucas(n)=', lucas(i))
		
	# assert test lucas(n) for first 10 elements, if fails then AssertionError is raised
	luc10 = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
	for i in range(10):
		assert lucas(i) == luc10[i]
	
	print("Testing sum_series() against lucas() and fiboncacci()...")
	n = input("Please enter n: ")
	n=int(n)
	print('sun_series(n) sequence for first:',n, 'elemetns')
	for i in range(n):
		print(sum_series(i))
	print('sun_series(n,2,1) sequence for first:',n, 'elemetns')
	for i in range(n):
		print(sum_series(i,2,1))
	# assert testing - if failed an AssertionError is raised
	# testing for first n elements if sum_series(n) with default args gives the same results as fibonacci(n)
	# and sum_series(n,2,1) gives the same results are lucas(n)
	for i in range(n):
		assert sum_series(i) == fibonacci(i)
	for i in range(n):
		assert sum_series(i,2,1) == lucas(i)
	


if __name__ == "__main__":
	main()