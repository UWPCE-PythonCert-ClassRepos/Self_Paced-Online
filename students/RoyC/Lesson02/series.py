def fibonacci(n):
    """
    Returns the nth member of the Fibonacci series
    Function is naturally recursive, calling itself for all but the first two members.
    :param n: the index of the series member to be returned
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)