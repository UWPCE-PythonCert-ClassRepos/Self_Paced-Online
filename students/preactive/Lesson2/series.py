def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
# print(fib(8))


def lucas(n):
    a, b = -1, 2
    for i in range(n):
        a, b = b, a + b
    return a
# lucas(5)


def sum_series(n, a=0, b=1):
    if n == 1:
        return a
    if n == 2:
        return b
    return sum_series(n - 2, a, b) + sum_series(n - 1, a, b)
# print(sum_series(2))


def assert_testing():
    """
    Building arrays to test against in a loop

    """
    fib_test_arr = [0, 1, 1, 2, 3, 5, 8, 13]
    lucas_test_arr = [2, 1, 3, 4, 7, 11, 18, 29]
    for fib_index, fib_test in enumerate(fib_test_arr):
        assert fib(fib_index + 1) == fib_test, "Fib Fail"
        assert sum_series(fib_index + 1, 0, 1) == fib_test, \
            "Sum Series Fib Failed"
    for lucas_index, lucas_test in enumerate(lucas_test_arr):
        assert lucas(lucas_index + 1) == lucas_test, "Lucas Fail"
        assert sum_series(lucas_index + 1, 2, 1) == lucas_test, \
            "Sum Series Lucas Failed"
assert_testing()
