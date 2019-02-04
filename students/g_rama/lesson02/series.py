def fibonacci(n):
    """ The function prints the fibonacci series and prints the nth fibonacci number"""
    fib = [0, 1]
    for _ in range(n):
        #print(fib)
        fib.append(fib[_] + fib[_ + 1])
    return fib[n]


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(8))


def lucas(n):
    """ The function prints the lucas series for giving number and prints the nth lucas number"""
    luc = [2, 1]
    for _ in range(n):
        luc.append(luc[_] + luc[_ + 1])
    return luc[n]


print(lucas(0))
print(lucas(1))
print(lucas(2))
print(lucas(3))
print(lucas(8))


def sum_series(n,g1=0,g2=1):
    """ The function prints a generic sequence number for given arguments
    usage: g1 and g2 defaults to fibonacci if no arguments are given
    """
    gen = [g1, g2]
    for _ in range(n):
        gen.append(gen[_] + gen[_ + 1])
    return gen[n]


print(sum_series(8))
print(sum_series(8,2,1))
print(sum_series(8,0,1))
print(sum_series(8,3,1))


def testing():
    assert fibonacci(8) == 21
    assert lucas(8) == 47
    assert sum_series(8) == 21
    assert sum_series(8, 3, 1) == 60
    assert fibonacci(0) != 21


testing()
