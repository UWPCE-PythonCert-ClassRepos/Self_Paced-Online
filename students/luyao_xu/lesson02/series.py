"""
A function that returns the nth number in a sequence formed by summing each number's two immediate previous terms.
:param n: index within the sequence
:param first: first term of the sequence
:param second: second term of the sequence
:returns: the nth term in the sequence
"""

def sum_series(n, first=0, second=1):
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 2, first, second) + sum_series(n - 1, first, second)

"""
A function that returns the nth term in a Fibonacci sequence.
:param n: index within the sequence
:returns: the nth term in the sequence
"""
def fibonacci(n):
    return sum_series(n)


"""
A function that returns the nth term in a Lucas number sequence.
:param n: index within the sequence
:returns: the nth term in the sequence
"""
def lucas(n):
    return sum_series(n, 2, 1)


if __name__ == '__main__':
    # unit tests
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert sum_series(3) == 2
    assert sum_series(3, 4, 5) == 14
