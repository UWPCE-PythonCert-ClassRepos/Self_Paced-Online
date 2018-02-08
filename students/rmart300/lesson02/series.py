"""
def fibonnaci(n)
The Fibonacci Series is a numeric series starting with the integers 0 and 1.
In this series, the next integer is determined by summing the previous two.
This gives us:
0, 1, 1, 2, 3, 5, 8, 13, ...


The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:
2, 1, 3, 4, 7, 11, 18, 29, ...
In your series.py module, add a new function, lucas, that returns the nth value in the lucas numbers series.
Ensure that your function has a well-formed docstring.
"""


def fibonacci(n):
    """return the nth value in the fibonacci series fib(n) = fib(n-2) + fib(n-1)"""
    if n > 2: 
        return fibonacci(n-2) + fibonacci(n-1)   
    elif n == 2:
        return fibonacci(n-1)
    else:
        return n

def lucas(n):
    """return the nth value in the lucas series"""
    if n >= 2:
         return lucas(n-2) + lucas(n-1)
    if n == 1:
         return 1
    if n == 0:
         return 2

if __name__ == '__main__': 
    for i in range(10):
         print('the ' + str(i) + ' value of fibonnaci series is: ' + str(fibonacci(i)))

    for i in range(10):
         print('the ' + str(i) + ' value of lucas series is: ' + str(lucas(i)))
