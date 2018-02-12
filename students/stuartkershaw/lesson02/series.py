def fibonacci(n):
    """Takes integer and returns corresponding fibonacci value"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Takes integer and returns corresponding lucas value"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, x=0, y=1):
    """Takes required integer and optional start params."""
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)


if __name__ == "__main__":
    assert fibonacci(6) == 8
    assert lucas(6) == 18
    assert sum_series(6, 2) == 18
