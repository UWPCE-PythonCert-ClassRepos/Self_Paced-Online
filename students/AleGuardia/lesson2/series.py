"""Function that returns the fibonacci and Lucas Numbers"""


def fibonacci(n):
    """Takes n parameter and returns the nth fibonacci number"""
    series = [0,1]
    for i in range(2, n+1):
        series.append(series[i-2]+series[i-1])
    return series[n]


def lucas(n):
    """Takes n parameter and returns the nth lucas number"""
    series = [2,1]
    for i in range(2, n+1):
        series.append(series[i-2]+series[i-1])
    return series[n]


def sum_series(element,first=0,second=1):
    """Takes an element argument thad decides which element in the series to print
    and two optional arguments that determine how the series starts, returns the element
    in the series"""

    series = [first, second]
    for i in range(2, element + 1):
        series.append(series[i - 2] + series[i - 1])
    return series[element]





print(fibonacci(7))
print(lucas(7))
print(sum_series(7))
print(sum_series(7,2,1))