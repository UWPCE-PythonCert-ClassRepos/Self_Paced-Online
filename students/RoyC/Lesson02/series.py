def fibonacci(n):
    """
    Returns the nth member of the Fibonacci series
    Function is naturally recursive, calling itself for all but the first two members.
    :param n: the index of the Lucas series member to be returned
    """
    return sum_series(n)
        
def lucas(n):
    """
    Returns the nth member of the Lucas series
    Function is naturally recursive, calling itself for all but the first two members.
    :param n: the index of the Lucas series member to be returned
    """
    return sum_series(n, 2, 1)
        
def sum_series(n, num0=0, num1=1):
    """
    Returns the nth member of the generalized number series, where each number in the 
    series is the sum of the previous two numbers. The optional two arguments, num0 and num1,
    are the first two numbers in the series, the defaults of 0 and 1 represent the Fibonacci series.
    Function is naturally recursive, calling itself for all but the first two members.
    :param n: the index of the Lucas series member to be returned
    :param num0: the first number in the series
    :param num1: the second number in the series
    """
    if n == 0:
        return num0
    elif n == 1:
        return num1
    else:
        return sum_series(n-2, num0, num1) + sum_series(n-1, num0, num1)