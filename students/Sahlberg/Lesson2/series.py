"""Ian Sahlberg
Python 210
12/22/2018
Assignment 2 Fibonacci series"""


def fibonacci(n):
    """Returns the nth value of the Fobinacci series"""
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
    #I could just use sum_series(n) within this function to achieve the same results

#print(fibonacci(3))

def lucas(n):
    """Returns the nth value of a Fibonacci series starting at 2,1..."""
    #while n >= 0:
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)
    # I could just use sum_series(n,2,1) within this function to achieve the same results

#print(lucas(5))

def sum_series(n, first_in_series = 0, second_in_series = 1):
    """Returns the nth value of a Fibonacci series given the first two starting parameters, defaults at 0,1,..."""
    if n == 0:
        return first_in_series
    elif n == 1:
        return second_in_series
    else:
        return sum_series(n - 2,first_in_series,second_in_series) + sum_series(n - 1,first_in_series,second_in_series)


# Test calls

print("Test function Fibonacci():")
print("result:", fibonacci(5))
print("Test function lucas():")
print("result:",lucas(5))
print("Test function sum_series as a Fibonacci sequence")
print("result:",sum_series(4,0,1))
print("Test function sum_series as a user defined sequence")
print("result:",sum_series(8,4,5))
