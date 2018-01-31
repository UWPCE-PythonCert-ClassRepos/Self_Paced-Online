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
    return sum_series(n, 0, 1)


def lucas(n):
    """Compute and return the nth value in the Lucas series via iteration.

    Args:
        n (int): nth position in the Lucas series

    Returns:
        int: nth value in the Lucas series
    """
    return sum_series(n, 2, 1)


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
    lookUp = [None] * 51
    fibValsLookup = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
                     987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368,
                     75025, 121393, 196418, 317811, 514229, 832040, 1346269,
                     2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
                     39088169, 63245986, 102334155, 165580141, 267914296,
                     433494437, 701408733, 1134903170, 1836311903, 2971215073,
                     4807526976, 7778742049, 12586269025]

    lucasValsLookup = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521,
                       843, 1364, 2207, 3571, 5778, 9349, 15127, 24476, 39603,
                       64079, 103682, 167761, 271443, 439204, 710647, 1149851,
                       1860498, 3010349, 4870847, 7881196, 12752043, 20633239,
                       33385282, 54018521, 87403803, 141422324, 228826127,
                       370248451, 599074578, 969323029, 1568397607, 2537720636,
                       4106118243, 6643838879, 10749957122, 17393796001, 28143753123]

    # Test that each function computes the correct first 50 values
    # Note: Testing the recursive fib function (w/o memoization) takes a long
    #       time to complete. For quick testing, that test is ignored.
    for i in range(50):
        assert(lucas(i) == lucasValsLookup[i]), \
            'lucas failed at %i' % i
        assert(fibonacci_iterative(i) == fibValsLookup[i]), \
            'fibonacci_iterative failed at %i' % i
        # assert(fibonacci_recursive(i) == fibValsLookup[i]), \
        #   'fibonacci_recursive failed at %i' % i
        assert(sum_series(i) == fibValsLookup[i]), \
            'sum_series(i) failed at %i' % i
        assert(sum_series(i, 2, 1) == lucasValsLookup[i]), \
            'sum_series(i,2,1) failed at %i' % i
        assert(fibonacci_recursive_mem(i, lookUp) == fibValsLookup[i]), \
            'fibonacci_recursive_mem failed at %i' % i

    # Test each function with a single value and print the result
    print('Rec: ' + str(fibonacci_recursive(10)))
    print('Itr: ' + str(fibonacci_iterative(10)))
    print('MRc: ' + str(fibonacci_recursive_mem(10, lookUp)))
    print('Luc: ' + str(lucas(10)))
