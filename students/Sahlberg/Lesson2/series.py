def fibonacci(n):
    """Returns the nth value of a Fibonacci series"""
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
		
def lucas(n):
    """Returns the nth value of a fibonacci series starting at 2,1..."""

    while n >= 0:
        if n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            return lucas(n - 2) + lucas(n - 1)
			
def sum_series(n, first_in_series = 0, second_in_series = 1):
    """"""
    if first_in_series == 0 and second_in_series == 1:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return sum_series(n - 2) + sum_series(n - 1)
    elif first_in_series == 2 and second_in_series == 1:
        if n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            return sum_series(n - 2) + sum_series(n - 1)
    else:
        if n == 0:
            return first_in_series
        elif n == 1:
            return second_in_series
        else:
            return sum_series(n - 2,first_in_series,second_in_series) + sum_series(n - 1,first_in_series,second_in_series)