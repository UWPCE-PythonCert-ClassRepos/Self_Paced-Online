def fibonacci(n):
    return sum_series(n, 0, 1)


def lucas(n):
    return sum_series(n, 2, 1)


def sum_series(n, first=0, second=1):
    # function returns the sum of the two numbers preceding the
    # 'nth' position in the series, where the first two numbers
    # are 0 and 1 by default
    if n < 0:
        return None
        # if n is less than zero return nothing
    elif n == 0:
        return first
        # if n is equal to zero return first in series
    elif n == 1:
        return second
        # if n is equal to zero return second in series
    else:
        # use the recursive function where
        # the output of the function is equal to the sum of the preceding
        # two values. Stop the loop when the counter reaches the 2nd
        # position in the sequence
        count = n
        while count > 2:
            first, second = second, first + second
            count -= 1
        return first + second


# assertion test for fibonacci
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2

# assertion test for lucas
assert lucas(0) == 2
assert lucas(1) == 1
assert lucas(2) == 3
assert lucas(3) == 4

# assertion test for sum_series
assert sum_series(0, 2, 2) == 2
assert sum_series(1, 2, 2) == 2
assert sum_series(2, 2, 2) == 4
assert sum_series(3, 2, 2) == 6
