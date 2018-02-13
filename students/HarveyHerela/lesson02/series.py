def fibonacci(n):
    """Return the nth member of the fibonacci sequence."""
    if n == 1:
        return 1
    if n == 0:
        return 0
    if n < 0:
        print("Bad element")
        return 0
    return fibonacci(n - 2) + fibonacci(n - 1)

def lucas(n):
    """Return the nth Lucas number."""
    if n == 1:
        return 1
    if n == 0:
        return 2
    if n < 0:
        print("Bad element")
        return 0
    return lucas(n - 2) + lucas(n - 1)

def sum_series(n, item0=0, item1=1):
    """Return the nth element in the sequence.
    
    n is the number of the element to retrieve. Must be greater than 0.
    item0 is the first element in the sequence. Default is 0 (Fibonacci).
    item1 is the first element in the sequence. Default is 1 (Fibonacci).
    """
    if n == 1:
        return item1
    if n == 0:
        return item0
    if n < 0:
        print("Bad element")
        return 0
    return sum_series(n - 2, item0, item1) + sum_series(n - 1, item0, item1)
    
# Test the fibonacci function
assert fibonacci(2) == 1
assert fibonacci(5) == 5
assert fibonacci(8) == 21

# Test the lucas function
assert lucas(2) == 3
assert lucas(5) == 11
assert lucas(8) == 47

# Test sum_series with default parameters
assert sum_series(2) == 1
assert sum_series(5) == 5
assert sum_series(8) == 21

# Test sum_series as a Fibonacci sequence
assert sum_series(2, 0, 1) == 1
assert sum_series(5, 0, 1) == 5
assert sum_series(8, 0, 1) == 21

# Test sum_series as a Lucas sequence
assert sum_series(2, 2, 1) == 3
assert sum_series(5, 2, 1) == 11
assert sum_series(8, 2, 1) == 47

