""" Compute and print a generalization of Fibonacci series
when the first 2 numbers are custom."""


def fibonacci(input_number):
    """Computes Fibonacci numbers when the numbers are parameterized."""
    if input_number <= 1:
        return input_number
    return fibonacci(input_number - 1) + fibonacci(input_number - 2)


def lucas(input_number):
    """Computing recursively Lucas numbers."""
    first_number = 2
    second_number = 1
    if input_number == 0:
        return first_number
    if input_number == 1:
        return second_number
    return lucas(input_number - 1) + lucas(input_number - 2)


def sum_series(input_number, first_number=0, second_number=1):
    """Computes sum series when the numbers are parameterized."""
    if input_number == 0:
        return first_number
    if input_number == 1:
        return second_number
    return sum_series(input_number - 1, first_number, second_number) + sum_series(input_number - 2, first_number, second_number)


if __name__ == '__main__':
    """Test suite to verify Fibonacci implementation."""
    assert fibonacci(7) == 13
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    print("Fibonacci numbers tests pass using Fibonacci algorithm.")

    """Test suite to verifying Lucas implementation"""
    assert lucas(7) == 29
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    print("Lucas numbers tests pass using Lucas algorithm.")

    """Test suite to verifying series implementation for Fibonaci"""
    assert sum_series(7) == 13
    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(2) == 1
    print("Fibonacci numbers tests pass using sum_series.")


    """Test suite to verifying series implementation for Fibonaci"""
    assert sum_series(7, 2, 1) == 29
    assert sum_series(0, 2, 1) == 2
    assert sum_series(1, 2, 1) == 1
    assert sum_series(2, 2, 1) == 3
    print("Lucas numbers tests pass using sum_series.")
