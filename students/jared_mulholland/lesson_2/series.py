"""
Problem 3: fibonacci, lucas, sum_series

"""

def fibonacci(n):
    """return the nth value in a fibonacci series (starting with 0 index)"""
    if n == 0:
        return(0)
    elif n == 1:
        return(1)
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """return the nth value in a lucas series (starting with 0 index). Lucas series begins with 2,1,3,..."""
    if n == 0:
        return(2)
    elif n == 1:
        return(1)
    else: 
        return lucas(n-1) + lucas(n-2)

def sum_series(n, x = 0, y = 1):
    """return sum of n-1 and n-2 numbers in a sequence. This function allows the user to get a result similar to a lucas 
    or fibonacci sequence but at any starting point"""
    if n == 0:
        return(x)
    elif n == 1:
        return(y)
    else:
        return (sum_series((n-1), x, y) + sum_series((n-2), x, y))


assert fibonacci(5) == 5
assert lucas(5) == 5
assert sum_series(5, x = 0, y = 1) == 5
    
    