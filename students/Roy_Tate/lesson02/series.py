# author: githubtater

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # formula from example: fib(n) = fib(n-2) + fib(n-1)

print(fibonacci(5))


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

print(lucas(6))


















































































# author: githubtater