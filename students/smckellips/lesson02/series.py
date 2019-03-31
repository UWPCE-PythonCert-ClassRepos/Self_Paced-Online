#! /usr/bin/env python
def fibonacci(n):
    """Return the nth value in the Fibonacci sequence."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    seed = [0,1]
    result = 0
    for i in range(2,n + 1):
        result = seed[0] + seed[1]
        seed[0] = seed[1]
        seed[1] = result
    return result


def lucas(n):
    """Return the nth value in the Lucas sequence."""
    if n == 0:
        return 2
    if n == 1:
        return 1
    seed = [2,1]
    result = 0
    for i in range(2,n + 1):
        result = seed[0] + seed[1]
        seed[0] = seed[1]
        seed[1] = result
    return result
    

def sum_series(n,a=0,b=1):
    """Return the nth value in the sequence with the given seed."""
    if n == 0:
        return a
    if n == 1:
        return b
    if n > 1:
        result = sum_series(n-2,a,b) + sum_series(n-1,a,b)
    return result


if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
