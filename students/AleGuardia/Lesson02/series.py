"""Function that returns the fibonacci and Lucas Numbers"""


def fibonacci(n):
    """Takes n parameter and returns the nth fibonacci number"""
    return sum_series(n)


def lucas(n):
    """Takes n parameter and returns the nth lucas number"""
    return sum_series(n,2,1)


def sum_series(element,first=0,second=1):
    """Takes an element argument thad decides which element in the series to print
    and two optional arguments that determine how the series starts, returns the element
    in the series"""

    series = [first, second]
    for i in range(2, element + 1):
        series.append(series[i - 2] + series[i - 1])
    return series[element]


# The following block of code builds the fibonacci and lucas series and tests the formulas

fib_series = [0,1,1,2,3,5,8,13,21,34,55,89]
luc_series = [2,1,3,4,7,11,18,29,47,76,123]


def test_series(series,name):
    """Takes the sequence and its name and tests the formula"""
    if name == "Fibonacci" : first, second = 0,1
    if name == "Lucas": first, second = 2,1
    for i in range(len(series)):
        print("The expected " + str(i) + " element in the " + name + " sequence is: " + str(series[i]))
        print("The result from the function is " + str(sum_series(i,first,second)))
        if sum_series(i,first,second) == series[i]:
            print("Test Passed")
        else:
            print("Test Failed)")


test_series(fib_series,"Fibonacci")
test_series(luc_series,"Lucas")


