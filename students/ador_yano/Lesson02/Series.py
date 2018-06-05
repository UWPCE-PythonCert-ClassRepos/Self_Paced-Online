# Series.py: implements Fibonacci Series Exercise for Lesson 2 Assignment

intro = '''UWPCE Python Programming: Lesson 2 Assignment
Fibonacci Series Exercise: fibonnaci and lucas functions to return nth value of
each series, generalized series function with three parameters
1. fib(n) - series starts with 0 and 1, returns nth value from zero index
2. lucas(n) - series starts with 2 and 1, returns nth value from zero index
3. sum_series(n, a, b) - optional arguments a and b default to 0 and 1, can be set to other values
    returns nth value
'''
print(intro)

def fib(n):
    """ Return nth value in Fibonacci series """
    if n < 0:                           # check for negative numbers
        print("Invalid argument")
    elif n == 0:                        # first value (zero index) in Fibonacci is 0
        return 0
    elif n == 1:                        # second value in Fibonacci is 1
        return 1
    else:
        return fib(n-2) + fib(n-1)      # nth value is the sum of the previous two values in the series

def lucas(n):
    """ Return nth value in Lucas series """
    if n < 0:                           # check for negative numbers
        print("Invalid argument")
    elif n == 0:                        # first value (zero index) in Lucas is 2
        return 2
    elif n == 1:                        # second value in Lucas is 1
        return 1
    else:
        return lucas(n-2) + lucas(n-1)  # nth value is the sum of the previous two values in the series

def sum_series(n,a=0,b=1):
    """ Return nth value in generalized series seeded by a and b parameters """
    if n < 0:                           # check for negative numbers
        print("Invalid argument")
    elif n == 0:                        # first value (zero index) set by a parameter
        return a
    elif n == 1:
        return b                        # second value set by b parameters
    else:
        return sum_series(n-2,a,b) + sum_series(n-1,a,b) # nth value is the sum of the previous two values in the series

def tests():
    assert fib(9) == 34
    assert lucas(9) == 76
    assert sum_series(9) == 34
    assert sum_series(9,2,1) == 76
    assert sum_series(5,3,8) == 49
