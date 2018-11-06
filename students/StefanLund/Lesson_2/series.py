# python3

# series.py

# functions to produce Fibonacci and Lucas number series

def fibonacci(n):
    """
    recursively computes the n'th value in the Fibonacci serie:
    0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    recursively computes the n'th value in the Lucas serie:
    2, 1, 3, 4, 7, 11, 18, 29, ...
    """
    if n == 0:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n + 1)


def sum_series(n, i, j):
    """
    recursively computes the n'th value in the serie:
    n'th:  0, 1,     2,      3,       4,       5,       6
    value: i, j, i + j, i + 2j, 2i + 3j, 3i + 5j, 4i + 8j ...
    for i = 0, j = 1 sum_series returns the fibonacci(n)
    for i = 2, j = 1 sum_series returns the lucas(n)
    """
    if n == 0:
        return i
    elif n == 1:
        return j
    else:
        return sum_series(n - 1, i, j) + sum_series(n - 2, i, j)


def test_sum_series(n):
    """
    n: test values in the range 0 to n - 1
    test if there are any dicrepancies in fiboncci and lucas series
    and the sum_series function.
    """
    for i in range(n):
        assert (fibonacci(i) == sum_series(i, 0, 1)), "If you read this, there is a bug!"
        assert (lucas(i) == sum_series(i, 2, 1)), "If you read this, there is a bug!"
    print("All values matched when tested for all n up to n = {}".
    format(n - 1))
