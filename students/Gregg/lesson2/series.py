

def fibonocci(n):
    """Find the nth element of the fibonocci series"""
    Sn = sum_series(n, first = 0, second = 1)
    return Sn

def lucas(n):
    """find the nth element of the lucas series"""
    Sn = sum_series(n, first = 2, second = 1)
    return Sn

def sum_series(n, first = 0, second = 1):
    """find the nth element of a series defined by its first and second elements
    where S(n) = S(n-1)+S(n-2)
    """
    if n<1:
        raise ValueError('Sum Series is not defined for values less than 1')
    if n == 1:
        Sn = first
    elif n == 2:
        Sn = second
    else:
        Sn = sum_series(n-1, first, second)+sum_series(n-2, first, second)
    return Sn

def sum_series_non_recursive(n, first = 0, second = 1):
    """find the nth element of a series defined by its first and second elements
    where S(n) = S(n-1)+S(n-2)
    Wanted to see how it looked without recursion and thinking about when it
    would and wouldn't make code better
    """

    return True


def series_tests():
    """Test the fibonocci and lucas series functions"""
    return True


def first_n_series(n, func):
    """Produce the firs n elements of a series defined by func and return as a list"""
    series = []
    for i in range(n):
        series.append(func(i+1))
    series.append(' ...')
    return series

if __name__ == "__main__":
    print('Lesson2: Series Exercise')
    print('Lesson2: Series Exercise - Fibonacci Only')
    print(first_n_series(8,fibonocci))
    print('Lesson2: Series Exercise - Lucas Only')
    print(first_n_series(8,lucas))
