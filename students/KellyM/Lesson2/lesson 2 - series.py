def fib(n):
    """ This function calculates a Fibonacci Series, which is a series that
        starts with 0 and 1, then calculates the next number by adding the
        previous two numbers."""
    if n == 1:
        return 1
    elif n==2:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

def lucas(n):
    """This function calculates Lucas Numbers, which are a series that
        starts with 2 and 1, then calculates the next number by adding the
        previous two numbers."""
    if n == 0:
        return 2
    elif n==1:
        return 1
    else:
        return (lucas(n-1) + lucas(n-2))

def sum_series(n, o=0, p=1):
    """This function calculates either the Fibonacci Series or the Lucas
        Numbers, depending on if additional parameters are provided. If no
        optional parameters, the Lucas Numbers will be calculatted,
        otherwise, the Fibonacci Series will be caluslated."""
    if o or p is None:
        return fib(n)
    else:
        return lucas(n)


assert fib(10) == 55
# This assertion tests that the Fibonacci function is working properly.

assert lucas(10) == 123
# This assertion tests that the Lucas Series function is working properly.

assert sum_series(5) == 11
# This assertion tests that the sum_series uses Fibonacci Series function if no other parameters are passed.

assert sum_series(5,6,7) == 5
# This assertion tests that the sum_series uses Lucas Series function if no other parameters are passed.
    
    
    
    
