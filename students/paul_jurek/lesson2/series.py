"""module to answer Fibonacci Series Exercise in Lesson 2"""


def fibonacci(n: int):
    """return nth value of fibonacci sequence starting with index 0
    args:
        n: positive integer for indicating sequence number to return


    returns:
        fib number at nth position
    """
    pass

    if n < 0:
        raise ValueError('input must be greater than or equal to 0')

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        counter = 2
        previous = 0
        current = 1

        while counter <= n:
            next = previous + current
            previous, current = current, next
            counter += 1
        return next
