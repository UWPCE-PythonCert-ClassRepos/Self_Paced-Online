'''
elmar_m / 22e88@mailbox.org
Lesson02:  Fibonacci Series Exercise
-------------------------------
File: series.py
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
        # print('value 0 in Fibonacci series: 0')
        return 0
    elif n == 1:
        # print('value 1 in Fibonacci series: 1')
        return 1
    elif n > 1:
        startvalues = [0, 1]
        counter = 0
        while counter <= n - 2:
            a = startvalues[0]
            b = startvalues[1]
            c = a + b
            # print(c)
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
            # print(c)
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
        print('Fibonacci series requested...')
        if n == 0:
            print('value 0 in Fibonacci series: 0')
            return 0
        elif n == 1:
            print('value 1 in Fibonacci series: 1')
            return 1
        else:
            calculate(n, x, y)
    elif x == 2 and y == 1:
        print('Lucas series requested...') 
        if n == 0:
            print('value 0 in Lucas series: 2')
            return 2
        elif n == 1:
            print('value 1 in Lucas series: 1')
            return 1 
        else:
            calculate(n, x, y)
    else:
        calculate(n, x, y)


def calculate(n, x, y):
    '''
    returns the n'th value of a series of natural numbers, 
    calculated using x and y as start values according to the
    formula which is also used to create Fibonacci or Lucas series.
    '''
    startvalues = [x, y]
    counter = 0
    while counter <= n - 2:
        a = startvalues[0]
        b = startvalues[1]
        c = a + b
        print(c)
        startvalues[0] = b
        startvalues[1] = c
        counter += 1
    return c


if __name__ == '__main__':
    print('i wanna be a module, please import me!')
