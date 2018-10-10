"""module to answer Fibonacci Series Exercise in Lesson 2"""


def fibonacci(n: int):
    """return nth value of fibonacci sequence starting with index 0
    args:
        n: non-negative integer for indicating sequence number to return

    returns:
        fib number at nth position
    """
    return sum_series(n=n, index0=0, index1=1)


def lucas(n: int):
    """return nth value of lucas sequence starting with index 0
    args:
        n: non-negative integer for indicating sequence number to return

    returns:
        lucas number at nth position
    """
    return sum_series(n=n, index0=2, index1=1)


def sum_series(n: int, index0: int=0, index1: int=1):
    """return nth index (starting at 0) of summing series.
    starting values defined by index0 and index1
    args:
        n: non-negative integer for indicating sequence number to return
        index0: number in first index of sereies
        index1: number in second index of series
    returns:
        value at nth position in summing series"""
    
    if n == 0:
        return index0
    elif n == 1:
        return index1
    else:
        counter = 2
        while counter <= n:
            next = index0 + index1
            index0, index1 = index1, next
            counter += 1
        return next


if __name__ == "__main__":
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(7) == 29

    assert fibonacci(7) == sum_series(7)
