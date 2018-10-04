def fibonacci(n):
    """ Return the nth value in the fibonacci series."""   
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

# print(fibonacci(7))
# print(fibonacci(6))
# print(fibonacci(5))
# print(fibonacci(4))
# print(fibonacci(3))
# print(fibonacci(2))
# print(fibonacci(1))
# print(fibonacci(0))


def lucas(n):
    """Return the nth value in the Lucas series"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)


# print(lucas(7))
# print(lucas(6))
# print(lucas(5))
# print(lucas(4))
# print(lucas(3))
# print(lucas(2))
# print(lucas(1))
# print(lucas(0))





def sum_series(n, a = 0, b = 1):
    """
    Return the nth value either in the fibonacci or lucas series.
    Param n: required parameter that determines which element in the series to print.
    Param a, b: optional parameters, determine the first two values in the series.
    """
    if n == 0:
        return a
    elif n == 1:
        return b
    else: 
        return sum_series(n-2, a, b)+sum_series(n-1, a, b)
                                                



# print(sum_series(7, a = 2, b = 1))
# print(sum_series(6, a = 2, b = 1))
# print(sum_series(5, a = 2, b = 1))
# print(sum_series(4, a = 2, b = 1))
# print(sum_series(3, a = 2, b = 1))
# print(sum_series(2, a = 2, b = 1))
# print(sum_series(1, a = 2, b = 1))
# print(sum_series(0, a = 2, b = 1))

# print(sum_series(7))
# print(sum_series(6))
# print(sum_series(5))
# print(sum_series(4))
# print(sum_series(3))
# print(sum_series(2))
# print(sum_series(1))
# print(sum_series(0))


def fibonacci_update(n):
    """Return the nth value in the Fibonacci series implementing sum_series function"""
    return sum_series(n, 0, 1)

def lucas_update(n):
    """Return the nth value in the Lucas series implementing sum_series function"""
    return sum_series(n, 2, 1)

# print(fibonacci_update(4))
# print(lucas_update(4))


#Series of Assert Statements to test whether the above functions run correctly:

# Assert statements to test whether our fibonacci function is correct.
assert fibonacci(7) == 13
assert fibonacci(6) == 8
assert fibonacci(5) == 5
assert fibonacci(4) == 3
assert fibonacci(3) == 2
assert fibonacci(2) == 1
assert fibonacci(1) == 1
assert fibonacci(0) == 0

#Assert statements to test whether our lucas function is correct. 
assert lucas(7) == 29
assert lucas(6) == 18
assert lucas(5) == 11
assert lucas(4) == 7
assert lucas(3) == 4
assert lucas(2) == 3
assert lucas(1) == 1
assert lucas(0) == 2


#Assert statements to test whether our sum_series function is correct. 
#The following 8 assert statements test sum_series function calling it with optional of a = 2 and b = 1, which should result in lucas series. 
assert sum_series(7, a = 2, b = 1) == 29
assert sum_series(6, a = 2, b = 1) == 18
assert sum_series(5, a = 2, b = 1) == 11
assert sum_series(4, a = 2, b = 1) == 7
assert sum_series(3, a = 2, b = 1) == 4
assert sum_series(2, a = 2, b = 1) == 3 
assert sum_series(1, a = 2, b = 1) == 1
assert sum_series(0, a = 2, b = 1) == 2
#The following 8 assert statements test sum_series function without no optional parameters, which should result in fibonacci series.
assert sum_series(7) == 13
assert sum_series(6) == 8
assert sum_series(5) == 5
assert sum_series(4) == 3
assert sum_series(3) == 2
assert sum_series(2) == 1
assert sum_series(1) == 1
assert sum_series(0) == 0


assert lucas_update(4) == 7 #an assert statement testing whether our re-implemented function returns the nth value in the lucas series. 
assert fibonacci_update(4) == 3 #an assert statement testing whether our re-implemented function returns the nth value in the fibonacci series. 