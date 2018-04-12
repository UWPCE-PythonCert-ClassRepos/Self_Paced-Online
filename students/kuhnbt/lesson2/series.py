def fibonacci(n):
    """Input: integer n 
    Returns the nth value of the fibonacci sequence (zero-indexed)"""
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):  
    """Input: integer n 
    Returns the nth value of the lucas series (zero-indexed)"""
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

def sum_series(n, param1=0, param2=1):
    """Inputs: integer n, optional starting integers param1 and param2
    Returns the nth value of the series"""
    if n==0:
        return param1
    elif n==1:
        return param2
    else:
        return sum_series(n-2, param1, param2) + sum_series(n-1, param1, param2)


# Testing function implementations by comparing function results
# with known values

assert fibonacci(8) == 21
assert lucas(5) == 11
assert sum_series(10) == 55
assert sum_series(4, 3, 4) == 18