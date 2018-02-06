"""This modules contain three functions that calculates the fibonacci,
lucas series, and sum series.

"""


def fibonacci(nth):
    """Return the value of nth element in the fibonacci series."""
    return sum_series(nth)


def lucas(nth):
    """Return the value of nth element in the lucas series."""
    return sum_series(nth, 2, 1)


def sum_series(nth, ref1=0, ref2=1):
    """Return the value of nth element in the sum series.

    Calling this function with no optional parameters will produce
    numbers from the fibonacci series. Calling it with the optional
    arguments 2 and 1 will produce values from the lucas numbers.
    Other values for the optional parameters will produce other
    series.

    """
    nth = int(round(abs(nth)))
    if nth == 0:
        value = ref1
    elif nth == 1:
        value = ref2
    else:
        for i in range(1, nth):
            value = ref1 + ref2
            ref1 = ref2
            ref2 = value
    return value


# check optional inputs
assert sum_series(5, 0, 1) == sum_series(5)
# check decimal get rounded to integer
assert sum_series(5.4) == sum_series(5)
# check absolute value of integer
assert sum_series(-5) == sum_series(5)
# check if fibonacci is calling sum_series
assert sum_series(5) == fibonacci(5)
# check if lucas is calling sum_series
assert sum_series(5, 2, 1) == lucas(5)
# check fibonacci series for 5th element, zeroth element = 0
assert fibonacci(5) == 5
# check lucas series for 5th element, zeroth element = 2
assert lucas(5) == 11
