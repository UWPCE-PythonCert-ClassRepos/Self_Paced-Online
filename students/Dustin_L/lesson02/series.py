#!/usr/bin/env python3


def fibonacci_recursive(n):
    """
    Compute and return the nth value in the fibonacci sequence via recursion.

    Args:
        n (int): nth position in the fibonacci sequence.

    Returns:
        int: nth value in the fibonacci sequence.
    """
    if n < 0:
        return None
    if (n == 0) or (n == 1):
        return n

    return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)


def fibonacci_recursive_mem(n, lookup):
    """
    Compute and return the nth value in the fibonacci sequence via recursion
    and memoization.

    Args:
        n (int): nth position in the fibonacci sequence.
        lookup (list): Empty list of min length of n+1 for memoization lookup.

    Returns:
        int: nth value in the fibonacci sequence.
    """
    if n < 0:
        return None
    if (n == 0) or (n == 1):
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fibonacci_recursive_mem(n-1, lookup) + \
                    fibonacci_recursive_mem(n-2, lookup)

    return lookup[n]


def fibonacci_iterative(n):
    """
    Compute and return the nth value in the fibonacci sequence via iteration.

    Args:
        n (int): nth position in the fibonacci sequence.

    Returns:
        int: nth value in the fibonacci sequence.
    """
    if n < 0:
        return None
    if (n == 0) or (n == 1):
        return n

    val  = 1
    prev = 0

    for _ in range(2, n + 1):
        val, prev = val + prev, val

    return val


def lucas(n):
    """Compute and return the nth value in the Lucas series via iteration.

    Args:
        n (int): nth position in the Lucas series

    Returns:
        int: nth value in the Lucas series
    """
    if n < 0:
        return None
    if n == 0:
        return 2
    if n == 1:
        return 1

    val  = 1
    prev = 2

    for _ in range(2, n + 1):
        val, prev = val + prev, val

    return val


def sum_series(n, firstVal=0, secondVal=1):
    """Compute and return the nth value in a summing series.

    The nth value is equal to the sum of the previous two values.

    Args:
        n (int): nth position in the summing series
        firstVal (int, optional): Defaults to 0. First value in the series
        secondVal (int, optional): Defaults to 1. Second value in the series

    Returns:
        int: nth value in the summing series
    """
    if n < 0:
        return None
    if n == 0:
        return firstVal
    if n == 1:
        return secondVal

    val  = secondVal
    prev = firstVal

    for _ in range(2, n + 1):
        val, prev = val + prev, val

    return val


if __name__ == '__main__':
    lookUp = [None] * 11

    print('Rec: ' + str(fibonacci_recursive(10)))
    print('Itr: ' + str(fibonacci_iterative(10)))
    print('MRc: ' + str(fibonacci_recursive_mem(10, lookUp)))
    print('Luc: ' + str(lucas(10)))

    assert (fibonacci_iterative(10) == sum_series(10)), "Failed!"
    assert (lucas(10) == sum_series(10, 2, 1)), "Failed!"
