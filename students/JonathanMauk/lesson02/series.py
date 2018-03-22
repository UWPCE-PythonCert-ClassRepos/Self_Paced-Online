def fibonacci(n):
    """Function that returns the nth term in the Fibonacci sequence, per F(n) = (n-1) + (n-2)."""
    if n < 0:
        print("Error: the first term in the Fibonacci sequence is 0. Please try again.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """Function that returns the nth term in the Lucas series, per F(n) = (n-1) + (n-2)."""
    if n < 0:
        print("Error: the first term in the Lucas series is 2. Please try again.")
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

print(lucas(2))
