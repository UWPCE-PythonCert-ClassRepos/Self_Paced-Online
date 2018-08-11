def fibonacci(n):
    """
    Returns the nth member of the Fibonacci series
    Function is naturally recursive, calling itself for all but the first two members.

    Arguments:
        n: the index of the Lucas series member to be returned
    """
    return sum_series(n)
        
def lucas(n):
    """
    Returns the nth member of the Lucas series
    Function is naturally recursive, calling itself for all but the first two members.

    Arguments:
        n: the index of the Lucas series member to be returned
    """
    return sum_series(n, 2, 1)
        
def sum_series(n, num0=0, num1=1):
    """
    Returns the nth member of the generalized number series, where each number in the 
    series is the sum of the previous two numbers. The optional two arguments, num0 and num1,
    are the first two numbers in the series, the defaults of 0 and 1 represent the Fibonacci series.
    Function is naturally recursive, calling itself for all but the first two members.
    
    Arguments:
        n: the index of the Lucas series member to be returned
        num0: the first number in the series (default 0)
        num1: the second number in the series (default 1)
    """
    if n == 0:
        return num0
    elif n == 1:
        return num1
    else:
        return sum_series(n-2, num0, num1) + sum_series(n-1, num0, num1)
        
if __name__ == "__main__":

    # Test random values in the Fibonacci series
    assert(fibonacci(0) == 0)
    assert(fibonacci(1) == 1)
    assert(fibonacci(2) == 1)
    assert(fibonacci(3) == 2)
    assert(fibonacci(4) == 3)
    assert(fibonacci(8) == 21)
    assert(fibonacci(10) == 55)
    assert(fibonacci(12) == 144)
    
    # Test random values in the Lucas series
    assert(lucas(0) == 2)
    assert(lucas(1) == 1)
    assert(lucas(2) == 3)
    assert(lucas(3) == 4)
    assert(lucas(4) == 7)
    assert(lucas(8) == 47)
    assert(lucas(10) == 123)
    assert(lucas(12) == 322)

    # Test random values in sum_series (though above tests were also tests)
    assert(sum_series(4, 5, 3) == 19)
    assert(sum_series(3, 2, 4) == 10)
    assert(sum_series(6, 1, 5) == 45)
    assert(sum_series(4, 4, 4) == 20)
    assert(sum_series(6, 12, 12) == 156)