def fibonacci(n):
    """Function that returns the nth term in the Fibonacci Sequence, per F(n) = (n-1) + (n-2)."""
    if n < 0:
        print("Error: the first term in the Fibonacci sequence is 0. Please try again.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(30))
