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








print(fibonacci(7))
print(lucas(7))