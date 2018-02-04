def fibonacci(n):
    """
    Given integer parameter n, this function returns the nth value
    in the Fibonacci series. This series is recursive, that is,
    each value in the series is the result of summing the two values
    immediately before it. The series moves forward, so to speak,
    by summing backward. Computationally, this is accomplished by
    calling the function from within the function, which leads
    to more function calls until a result is generated--recursion.
    """

    if n == 1:
        v = 0
    elif n == 2:
        v = 1
    else:
        v = fibonacci(n - 2) + fibonacci(n - 1)

    return v


def lucas(n):
    """
    Given integer parameter n, this function returns the nth value
    in the Lucas series. Like the Fibonacci series, this series
    is recursive.
    """

    if n == 1:
        v = 2
    elif n == 2:
        v = 1
    else:
        v = lucas(n - 2) + lucas(n - 1)

    return v
    

def sum_series(i, v1=0, v2=1):
    """
    This function also recursively returns a series element. Given
    integer parameter i (for index) plus default v1 and v2 values,
    it returns the Fibonacci series value at i. The Lucas series
    value at i can be obtained by passing v1=2 when calling the
    function. Other series will result if different integers are
    passed to v1 and/or v2.
    """
    if i == 1:
        v = v1
    elif i == 2: 
        v = v2
    else: 
        v = sum_series(i - 2, v1, v2) + sum_series(i - 1, v1, v2)
    return v


# Tests
# In the following lines, each of the series functions will be
# tested, respectively.

if __name__ != "__main__":
# Fibonacci
# This sequence starts with 0, 1, 1, 2, 3, 5, 8, 13
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(8) == 13

# Lucas
# This sequence starts with 2, 1, 3, 4, 7, 11, 18, 29
    assert lucas(1) == 2
    assert lucas(2) == 1
    assert lucas(3) == 3
    assert lucas(8) == 29

# Sum series
# This function is also a recursive series element finder.
# Its default series is Fibonacci, but Lucas series elements
# may be obtained by passing 2 after the element index number.
    assert sum_series(1) == 0  # returns first Fibonacci element
    assert sum_series(2) == 1  # returns second Fibonacci element
    assert sum_series(3) == 1  # returns third Fibonacci element
    assert sum_series(7) == 8  # returns seventh Fibonacci element
    assert sum_series(1, 2) == 2  # returns first Lucas element
    assert sum_series(2, 2) == 1  # returns second Lucas element
    assert sum_series(3, 2) == 3  # returns third Lucas element
    assert sum_series(7, 2) == 18  # returns seventh Lucas element

    if True:
        print('All tests passed for fibonacci, lucas, and sum_series.')
        