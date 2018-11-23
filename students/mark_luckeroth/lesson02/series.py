def fibonacci(n):
    """return the n_th value in the fibonacci series (zero index)"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


def lucas(n):
    """return the n_th value in the lucas series (zero index)"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

def sum_series(n, zero=0, one=1):
    """return the n_th value of a series where f(n) = f(n-1) + f(n-2)
    default values for f(0) and f(1) generate fibonacci series"""
    if n == 0:
        return zero
    elif n == 1:
        return one
    else:
        return sum_series(n-2,zero,one) + sum_series(n-1,zero,one)

#Test block

assert fibonacci(9) == 34         #test verifies fibonacci function
assert lucas(5) == 11             #test verifies lucas function
assert sum_series(8) == 21        #test verifies sum_series function with arg[1] and arg[2] unspecified
assert sum_series(8,2,6) == 152   #test verifies sum_series function with all arguments specified