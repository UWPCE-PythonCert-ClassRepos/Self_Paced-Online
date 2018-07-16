def fibonacci(n):
    """
    Returns the nth value in the fibonacci sequence starting with 0 index
    :param n: The index into the fibonacci series
    """
    if(n == 1):
        return 1
    elif(n == 0):
        return 0
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):
    """
    Returns the nth value in the lucas sequence starting with 0 index
    :param n: The index into the lucas series
    """
    if(n == 1):
        return 1
    elif(n == 0):
        return 2
    else:
        return lucas(n-2) + lucas(n-1)

def sum_series(n, i0=0, i1=1):
    """
    Returns the nth value in the sequence starting with 0 index
    :param n: The index into the series
    :param i0: The 0 index value
    :param i1: The 1 index value
    """
    if(n == 1):
        return i1
    elif(n == 0):
        return i0
    else:
        return sum_series(n-2, i0, i1) + sum_series(n-1, i0, i1)

if __name__ == '__main__':
    # Test fibonacci method first
    assert(fibonacci(0) == 0)
    assert(fibonacci(1) == 1)
    assert(fibonacci(2) == 1)
    assert(fibonacci(3) == 2)
    assert(fibonacci(6) == 8)
    assert(fibonacci(10) == 55)

    # Test lucas method next
    assert(lucas(0) == 2)
    assert(lucas(1) == 1)
    assert(lucas(2) == 3)
    assert(lucas(3) == 4)
    assert(lucas(6) == 18)
    assert(lucas(8) == 47)

    # Verify sum_series with only 1 arg matches fibonacci
    assert(sum_series(3) == fibonacci(3))
    assert(sum_series(7) == fibonacci(7))
    assert(sum_series(10) == fibonacci(10))
    assert(sum_series(25) == fibonacci(25))

    # Verify sum_series with 2 andd 1 arg matches lucas
    assert(sum_series(3, 2, 1) == lucas(3))
    assert(sum_series(7, 2, 1) == lucas(7))
    assert(sum_series(10, 2, 1) == lucas(10))
    assert(sum_series(25, 2, 1) == lucas(25))

    # Verify sum_series with different values
    assert(sum_series(0, 1, 3) == 1)
    assert(sum_series(1, 1, 3) == 3)
    assert(sum_series(2, 1, 3) == 4)
    assert(sum_series(3, 1, 3) == 7)
    assert(sum_series(7, 1, 3) == 47)
    assert(sum_series(10, 1, 3) == 199)
