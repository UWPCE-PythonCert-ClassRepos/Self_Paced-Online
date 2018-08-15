#uw python 210
#lesson 02
#max anderson

#series module containing fibonacci, lucas, and sum_series functions
#fibonacci and lucas index 0

def fibonacci(n):
    """Return the nth value in the fibonacci series."""
    if n == 0: return 0
    elif n == 1: return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

def lucas(n):
    """Return the nth value in the lucas series."""
    if n == 0: return 2
    elif n == 1: return 1
    else:
        return (lucas(n-1) + lucas(n-2))

def sum_series(n, o=0, p=1):
    """Return the nth value of a series with optional seed values o, p."""
    if n == 0: return o
    elif n == 1: return p
    else:
        return (sum_series(n-1, o, p) + sum_series(n-2, o, p))

if __name__ == "__main__":
    #tests ran when loaded as script

    print()
    print("Running Tests...")

    #loading test list w/ first 10 known values of fib seq
    fibolist = 0,1,1,2,3,5,8,13,21,34
    #asserting with known values
    for i in range(10):
        assert fibonacci(i) == fibolist[i]

    #loading test list w/ first 10 known values of lucas seq
    lucalist = 2,1,3,4,7,11,18,29,47,76
    #asserting with known values
    for i in range(10):
        assert lucas(i) == lucalist[i]

    #asserting sum_series w/ known values of test lists
    for i in range(10):
        assert sum_series(i) == fibolist[i]
        assert sum_series(i, 2, 1) == lucalist[i]

    print("All Tests Passed.")