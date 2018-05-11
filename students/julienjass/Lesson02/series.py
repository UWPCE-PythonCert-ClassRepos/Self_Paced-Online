def fibonacci(n):
    """computing the nth Fibonacci number"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


def lucas(n):
    """computing the nth Lucas number"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)


def sum_series(n, a=0, b=1):
    """computing the nth in Fibonacci series with default a, b arguments
    and nth number in Lucas series if a, b arguments are set to 2 and 1"""
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n-2,a,b) + sum_series(n-1,a,b)

#testing output of Fibonacci function

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(6) == 8


#testing output of Lucas function
assert lucas(0) == 7
assert lucas(5) == 7
assert lucas(8) == 29

#testing output of sum_series with default a,b arguments
assert sum_series(5) == 3
assert sum_series(8) == 13

#testing output of sum_series function with values 2,1 assigned to a,b arguments
assert sum_series(5,2,1) == 7
assert sum_series(8,2,1) == 29
