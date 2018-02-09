'''
File: series.py
elmar_m / 22e88@mailbox.org
Lesson02:  Fibonacci Series Exercise
------------------------------------
Python module containing functions to generate Fibonacci and Lucas series 
of integers and return their n'th value. 
Instead of Fibonacci or Lucas series start values (0 and 1 resp. 2 and 1)
arbitrary start values can be given also, resulting in series calculated
accordingly.
'''


def fib(n):
    '''
    returns the n'th value of the Fibonacci series of natural numbers.
    'n' is required to be a positive integer. 
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        startvalues = [0, 1]
        counter = 0
        while counter <= n - 2:
            a = startvalues[0]
            b = startvalues[1]
            c = a + b
            startvalues[0] = b
            startvalues[1] = c
            counter += 1
        return c
    else:
        print('This function requires a positive integer')


def lucas(n):
    '''
    returns the n'th value of the Lucas series of natural numbers.
    'n' is required to be a positive integer. 
    '''
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        startvalues = [2, 1]
        counter = 0
        while counter <= n - 2:
            a = startvalues[0]
            b = startvalues[1]
            c = a + b
            startvalues[0] = b
            startvalues[1] = c
            counter += 1
        return c
    else:
        print('This function requires a positive integer')
        

def sum_series(n, x=0, y=1):
    '''
    returns the n'th value of the Fibonacci series (default), of 
    the Lucas series or of a series of numbers calculated accordingly,
    starting with two given arbitrary numbers.
    Arguments:
    n: mandatory. The n'th value of the series will be returned.
    x: first start value. Defaults to '0' if not given.
    y: second start value. Defaults to '1' if not given. 
    Arguments have to be positive integers. 
    '''
    if x == 0 and y == 1:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return calculate(n, x, y)
    elif x == 2 and y == 1:
        if n == 0:
            return 2
        elif n == 1:
            return 1 
        else:
            return calculate(n, x, y)
    else:
        return calculate(n, x, y)


def calculate(n, x=0, y=1):
    '''
    returns the n'th value of a series of natural numbers, 
    calculated using x and y as start values according to the
    formula which is also used to create Fibonacci or Lucas series.
    Defaults to Fibonacci series if x and y are not 
    explicitly given. 
    Caveat:
    This function is meant to be called by sum_series().  
    If called directly there would be an UnboundLocalError when n == 0 or
    n == 1. This scenario is only handled correctly when called by sum_series().  
    '''
    startvalues = [x, y]
    counter = 0
    while counter <= n - 2:
        a = startvalues[0]
        b = startvalues[1]
        c = a + b
        startvalues[0] = b
        startvalues[1] = c
        counter += 1 
    return c

'''
assert statements ensure that functions work in a specified way. They are 
executed immediately when a module is imported and throw AssertionError if
their expression does not result to "True". So the following statements
ensure that the calculated results are correct. 
'''
fib_results = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
for i in range(0, 20):
    assert fib(i) == fib_results[i]     
    assert sum_series(i) == fib_results[i]
    assert sum_series(i, 0, 1) == fib_results[i]

lucas_results = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2207, 3571, 5778, 9349, 15127]
for i in range(0, 20):
    assert lucas(i) == lucas_results[i]     
    assert sum_series(i, 2, 1) == lucas_results[i]

# assert calculate(0, 0, 1) == 0
# assert calculate(1, 0, 1) == 1

assert calculate(2, 0, 1) == 1
assert calculate(9, 0, 1) == 34
assert calculate(9, 2, 1) == 76


if __name__ == '__main__':
    print('i wanna be a module, please import me!')
