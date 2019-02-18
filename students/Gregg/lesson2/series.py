

def fibonocci(n):
    """Find the nth element of the fibonocci series"""
    return True

def lucas(n):
    """find the nth element of the lucas series"""
    return True

def sum_series(n, first = 0, second = 1):
    """find the nth element of a series defined by its first and second elements
    where S(n) = S(n-1)+S(n-2)
    """

    return True

def series_tests():
    """Test the fibonocci and lucas series functions"""
    return True


def first_n_series(n, func):
    """Produce the firs n elements of a series defined by func and return as a list"""
    series = []
    for i in range(n):
        series.append(func(n))
    series.append(' ...')
    return series

if __name__ == "__main__"
    print('Lesson2: Series Exercise')
    print('Lesson2: Series Exercise - Fibonacci Only')
    print(first_n_series(8,fibonocci))
    print('Lesson2: Series Exercise - Lucas Only')
    print(first_n_series(8,lucas))
