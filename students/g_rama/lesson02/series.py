def fibonacci(n):
    """ The function prints the fibonacci series for giving number"""
    if n<= 1:
        fib = [0, 1]
        print((fib[n]))
    else:
        fib = [0, 1]
        for _ in range(n):
            print(fib)
            fib.append(fib[_]+fib[_+1])
        print(fib[n])


fibonacci(0)
fibonacci(1)
fibonacci(2)
fibonacci(3)
fibonacci(8)


def lucas(n):
    """ The function prints the lucas series for giving number"""
    if n<= 1:
        luc = [2, 1]
        print((luc[n]))
    else:
        luc = [2, 1]
        for _ in range(n):
            print(luc)
            luc.append(luc[_]+luc[_+1])
        print(luc[n])


lucas(0)
lucas(1)
lucas(2)
lucas(3)
lucas(8)


def sum_series(n,g1=0,g2=1):
    """ The function prints a generic sequence number for given arguments
    usage: g1 and g2 defaults to fibonacci if no arguments are given
    """
    if n <= 1:
        gen = [g1, g2]
        print((gen[n]))
    else:
        gen = [g1, g2]
        for _ in range(n):
            print(gen)
            gen.append(gen[_] + gen[_ + 1])
        print(gen[n])


sum_series(8)
sum_series(8,2,1)
sum_series(8,0,1)
sum_series(8,3,1)


def testing():
    assert fibonacci(8) == 21
    assert lucas(8) == 47
    assert sum_series(8) == 21
    assert sum_series(8, 3, 1) == 60
    assert fibonacci(0) != 21


