def fibonacci(n):
    """Calculate the nth number of the Fibonacci Series."""
    return sum_series(n)




def lucas(n):
    """Calculate the nth number of the Lucas Series."""
    return sum_series(n,2,1)




def sum_series(n, a=0, b=1):
    """Calculate the nth number of a fibonacci style series.
    
    Parameters:
        first: This is the position of the series to return.
        second (optional. default=0): This is the first seed vaalue to add.
        third (optional, default=1); This is the second seed value to add.
    """
    c=0
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(n-1):
            c=a+b
            a=b
            b=c
        return c




#Block of tests for previous functions.

#Verifies Fibonacci sequence. f(0), f(1), and f(2) tests each branch of the if-else tree.
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(5) == 5

#Verifies Lucas series. f(0), f(1), and f(2) tests each branch of the if-else tree.
assert lucas(0) == 2
assert lucas(1) == 1
assert lucas(2) == 3
assert lucas(5) == 11

#Tests the generic sum_series function throu fibonacci and lucas series.
#These 2 blocks test one input, and 3 inputs into the function.
assert sum_series(0) == fibonacci(0)
assert sum_series(1) == fibonacci(1)
assert sum_series(2) == fibonacci(2)
assert sum_series(5) == fibonacci(5)

assert sum_series(0,2,1) == lucas(0)
assert sum_series(1,2,1) == lucas(1)
assert sum_series(2,2,1) == lucas(2)
assert sum_series(5,2,1) == lucas(5)