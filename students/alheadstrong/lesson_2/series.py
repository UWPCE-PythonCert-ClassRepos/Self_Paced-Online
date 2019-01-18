'''Author: Alex Filson
Updated: 1.18.19
Fibonacci Exercise for Lesson 2
Py210, Online Self-Paced
'''

def fibonacci(n):
    '''Return the nth number in fibonacci sequenc.e'''
    if n == 0 or n == 1:
        return(n)
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

def lucas(n):
    '''Return the nth number in the lucas sequence.'''
    if n == 0:
        return(2)
    if n == 1:
        return(1)
    else:
        return(lucas(n-1)+lucas(n-2))

def sum_series(n, n0 = 0, n1 = 1):
    '''Return the nth value in a series based on n = (n-1)+(n-2).

    :param n - nth value in sequence that fn will return
    :param n0 - 0th value, default 0
    :param n1 - 1th value, default 1
    '''
    if n == 0:
        return(n0)
    if n == 1:
        return(n1)
    else:
        return sum_series(n-1,n0 = n0,n1 = n1)+sum_series(n-2,n0 = n0,n1 = n1)


#Assert statements to test code

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(7) == 13

assert lucas(0) == 2
assert lucas(1) == 1
assert lucas(7) == 29

assert sum_series(7) == 13
assert sum_series(28) == fibonacci(28)
assert sum_series(2,n0 = 4) == 5
assert sum_series(5,n1 = 2) == 10
assert sum_series(3,n0 =5, n1 = 20) == 45