# Fibonacci

def fibonacci(n):
    '''Fibonacci - return the nth value in the fibonacci series (starting with zero index) - call with series.fibonacci(n)'''
    if (n<1):
    	return (0)
    if (n == 1):
    	return (1)
    else:
    	return( fibonacci(n-2) + fibonacci(n-1) )

print (fibonacci.__doc__)

def lucas(n):
    '''Lucas - return the nth value in the lucas series - call with series.lucas(n)'''
    if (n<1):
    	return (2)
    if (n == 1):
    	return (1)
    else:
    	return( lucas(n-2) + lucas(n-1) )

print (lucas.__doc__)


def sum_series(n, x=0, y=1):
    """sum_series - return the nth value in the sum series - call with series.sum_series(n,x,y), 
    	x and y are optional starting values (0 and 1 if not specified)

    	"""

    if (n<1):
    	return (x)
    if (n == 1):
    	return (y)
    else:
    	return( sum_series(n-2, x, y) + sum_series(n-1, x, y) )

print (sum_series.__doc__)

if __name__ == "__main__":
    # this will only print if run as a script
    print("running tests")
    assert fibonacci(6) == sum_series(6), "fib and sum_series at n=6 should be the same"

    assert lucas(6) == sum_series(6,2,1), "lucas and sum_series at n=6 should be the same"

    assert sum_series(5,3,2) == 19, "sum_series with (5,3,2) should be 12"

    print("the tests pass")

