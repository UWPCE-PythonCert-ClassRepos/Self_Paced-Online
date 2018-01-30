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


if __name__ == '__main__':
    lookUp = [None] * 11

    print('Rec: ' + str(fibonacci_recursive(10)))
    print('Itr: ' + str(fibonacci_iterative(10)))
    print('MRc: ' + str(fibonacci_recursive_mem(10, lookUp)))
