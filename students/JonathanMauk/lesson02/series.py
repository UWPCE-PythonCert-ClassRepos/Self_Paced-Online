def fibonacci(n):
    """Function that returns the nth term in the Fibonacci sequence, per F(n) = (n-1) + (n-2)."""
    if n < 0:
        print("Error: the first term in the Fibonacci sequence is 0. Please try again.")
    else:
        return sum_series(n)


def lucas(n):
    """Function that returns the nth term in the Lucas series, per F(n) = (n-1) + (n-2), and F(0) = 2 while F(1) = 1."""
    if n < 0:
        print("Error: the first term in the Lucas series is 2. Please try again.")
    else:
        return sum_series(n, 2, 1)


def sum_series(n, x=0, y=1):
    """
    Generalized function that returns nth term in recursive sequences like Fibonacci and Lucas.
    Defaults to Fibonacci sequence.
    """
    if n == 0:
        return x
    if n == 1:
        return y
    else:
        return sum_series(n-1, x, y) + sum_series(n-2, x, y)

# Assert statements: Fibonacci edition
print(fibonacci(0))
print(fibonacci(2))
print(fibonacci(15))

# Assert statements: Lucas edition
print(lucas(0))
print(lucas(3))
print(lucas(8))

# Assert statements: sum series edition
print(sum_series(4))  # defaults to Fibonacci
print(sum_series(5, 2, 1))  # Lucas series
print(sum_series(8, 7, 5))  # random
