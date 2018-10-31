def fibonacci(n):
    """Fibonacci Series 0,1,1,2,3...returning the nth number in the list starting with index 0."""  
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n-2)+fibonacci(n-1)


def lucas(n):
    """Create a Lucas Series 2,1,3,4....and returns the nth value starting with index 0."""
    if n == 0:
        return 2
    if n == 1:
        return 1
    if n>1:
        return lucas(n-2)+lucas(n-1)


def sum_series(n, x=0, y=1):
    """Creates a Fibonacci series with a firs value x second value y, and a Lucas series if you change x,y=2,1.
    This function returns the nth value starting with index 0."""
    if n == 0:
        return x
    if n == 1:
        return y
    if n > 1:
        return sum_series(n-2, x, y)+sum_series(n-1, x, y)
        

print('This is th 4th result of Fibonacci series, starting at index 0')
print(fibonacci(4))

print('This is the 4th result of the Lucas series, starting at index 0')
print(lucas(4))

print('This is the 4th result of a series starting'
      'with x and y,where sum_series=sum_series[n-2]+sum_series[n-1].'
      'The nth result is displayed, staring index 0.')
print(sum_series(4, 3, 2), end=' ')
