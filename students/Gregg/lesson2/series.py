

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
    Series = []
    for i in range(1,n+1):
        if i == 1:
            Series.append(first)
        elif i == 2:
            Series.append(second)
        else:
            Series.append(Series[-1]+Series[-2])
    #Seems like this works because the series is simple and very orderly -
    #one after the other, with only one option
    #I could see how something with more of a tree structure, or with more options
    #would actually requre recursion
    return Series[-1]


def series_tests():
    """Test the fibonocci and lucas series functions"""
    #The 8th element of fibonocci should be 13
    assert(fibonocci(8)==13)
    #The 8th element of lucas should be 29
    assert(lucas(8)==29)
    #The 8th element of fibonocci produced using sum series should be 13
    assert(sum_series(8)==13)
    #The 8th element of lucas produced using sum series should be 29
    assert(sum_series(8,first = 2)==29)
    return True


def first_n_series(n, func):
    """Produce the firs n elements of a series defined by func and return as a list"""
    series = []
    for i in range(n):
        series.append(func(i+1))
    series.append(' ...')
    return series

if __name__ == "__main__":
    series_tests()
    print('Lesson2: Series Exercise')
    print('Lesson2: Series Exercise - Fibonacci Only')
    print(first_n_series(8,fibonocci))
    print('Lesson2: Series Exercise - Lucas Only')
    print(first_n_series(8,lucas))
