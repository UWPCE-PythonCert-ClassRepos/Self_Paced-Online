def fibonacci(n):
    """Returns the nth value of a Fibonacci series"""
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
		
def lucas(n):
    """Returns the nth value of a fibonacci series starting at 2,1..."""

    while n >= 0:
        if n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            return lucas(n - 2) + lucas(n - 1)