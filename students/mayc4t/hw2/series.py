
# #######################################################################


def fibonacci(n):
    """ Returns the nth value in the fibonacci series. """
    # Note to myself
    # The function should have one parameter, n.
    # The function should return the nth value in the fibonacci series (starting with zero index)
    # Ensure that your function has a well-formed docstring
    # Note that the fibinacci series is naturally recursive – the value is defined by previous values:
    #
    # fib(n) = fib(n-2) + fib(n-1)
    fib_nm2 = 0
    fib_nm1 = 1

    if n == 0:
        return 0
    if n == 1:
        return 1

    fib_n = None
    for i in range(n - 1):
        fib_n = fib_nm1 + fib_nm2
        fib_nm2 = fib_nm1
        fib_nm1 = fib_n
    return fib_n


def fibonacci_recursive(n):
    """ Returns the nth value in the fibonacci seriesx using recursive. """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# #######################################################################
def lucas(n):
    """ Return the nth value in the lucas number series """
# Note to myself.
# The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1.
# The resulting series looks like this:
# 2, 1, 3, 4, 7, 11, 18, 29, ...

    luc_nm2 = 2
    luc_nm1 = 1

    luc = None
    if n == 0:
        return 2
    if n == 1:
        return 1
    for i in range(n - 1):
        luc_n = luc_nm2 + luc_nm1
        luc_nm2 = luc_nm1
        luc_nm1 = luc_n
    return luc_n


def lucas_recursive(n):
    """ Return the nth value in the lucas number series using recursive method """
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas_recursive(n-1) + lucas_recursive(n-2)


# #######################################################################
def sum_series(n, nm2=0, nm1=1):
    """ Return the nth in the series
    Number of parameters: 3
        1st parameter: 
            - Required.
            - Used to which element in the series to print
        2nd and 3rd parameter:
            - Optional
            - Default value ( 0,1) return Fibonacci number
            - Other value (2, 1) return Lucas number
    """
    if n == 0:
        return nm2
    if n == 1:
        return nm1
    else:
        for i in range(n-1):
            num = nm2 + nm1
            nm2 = nm1
            nm1 = num
        return num


# #######################################################################
# TEST VALUES

# Iterative
for i in range(10):
    print('fib(%s) = %s' % (i, fibonacci(i)))

# Recursive
for i in range(10):
    print('fib_recursive(%s) = %s' % (i, fibonacci_recursive(i)))

for i in range(10):
    print('sss---(%s) = %s' % (i, sum_series(i)))


# lucas Iterative
for i in range(10):
    print('lucas(%s) = %s' % (i, lucas(i)))

for i in range(10):
    print('lucas_recursive(%s) = %s' % (i, lucas_recursive(i)))

for i in range(10):
    print('sss (%s) = %s' % (i, sum_series(i, 2, 1)))
