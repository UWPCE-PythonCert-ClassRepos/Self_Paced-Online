"""
def fibonnaci(n)
The Fibonacci Series is a numeric series starting with the integers 0 and 1.
In this series, the next integer is determined by summing the previous two.
This gives us:
0, 1, 1, 2, 3, 5, 8, 13, ...

def lucas(n)
The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:
2, 1, 3, 4, 7, 11, 18, 29, ...
In your series.py module, add a new function, lucas, that returns the nth value in the lucas numbers series.
Ensure that your function has a well-formed docstring.

def sum_series(n,x=0,y=1)
The required parameter will determine which element in the fibonacci or lucas series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced, thereby driving wheer fibonacci or lucas series is used.  Fibonacci is used by default if x and y are not provided

"""

def sum_series(n,x=0,y=1):
    """return the nth value of fibonacci (x=0,y=1) or lucas (x=2,y=1) series"""
    if x not in (0,2) or y != 1:
        print("function not found for x=" + str(x) + " and y=" + str(y))
    else:
        if n == 0:
            return x
        elif n == 1:
            return y
        else:
            return sum_series(n-2,x,y) + sum_series(n-1,x,y)

def fibonacci(n):
    """return the nth value in the fibonacci series fib(n) = fib(n-2) + fib(n-1)"""
    if n >= 2: 
        return sum_series(n)
    else:
        return n

def lucas(n):
    """return the nth value in the lucas series"""
    if n >= 2:
         return sum_series(n,2,1)
    elif n == 1:
         return 1
    elif n == 0:
         return 2

if __name__ == '__main__': 
    for i in range(10):
         print('the n=' + str(i) + ' value of fibonnaci series is: ' + str(fibonacci(i)))

    for i in range(10):
         print('the n=' + str(i) + ' value of lucas series is: ' + str(lucas(i)))

    x = 0
    y = 1
    for i in range(10):
         print('the n=' + str(i) + ' value of sum series if x = 0 and y = 1 is: ' + str(sum_series(i,x,y)))

    x = 2
    for i in range(10):
         print('the n=' + str(i) + ' value of sum series if x = 0 and y = 2 is: ' + str(sum_series(i,x,y)))

    sum_series(0,4,3)
