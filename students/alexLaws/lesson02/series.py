def fibonacci(n):
    """Return the nth value in the fibonacci sequence"""
    return sum_series(n)


def lucas(n):
    """Return the nth value in the lucas sequence"""
    return sum_series(n, 2, 1)


def sum_series(n, a=0, b=1):
    """Return the nth value in a fibonacci-type series; 1st values are a & b"""
    if n == 1:
        return (a)
    elif n == 2:
        return (b)
    else:
        return (sum_series(n-1, a, b) + sum_series(n-2, a, b))

"""assert statements to test the program"""
assert fibonacci(8) == 13  # The 8th num in my fibonacci sequence is 13
assert sum_series(8) == 13  # The series function w/1 input returns fibonacci
assert lucas(8) == 29  # The 8th num in my Lucas sequence is 29
assert sum_series(8, 2, 1) == 29  # The series output w/3 inputs is Lucas
