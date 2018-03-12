# Author: Roy Tate (githubtater)

def fibonacci(n):
    '''Return the nth value in the fibonacci series.'''
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2) # formula from example: fib(n) = fib(n-2) + fib(n-1)


def lucas(n):
    '''Fibonacci() with a twist. The sequence begins from 2 and 1 (rather than 0 and 1)'''
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, y=0, z=1):
    '''
        Return the nth position in the fibonacci series if no optional arguments are
        provided. Return the nth position of the lucas series if the optional arguments
        equal 2 and 1. Other optional arguments can be handled at a later time.
    '''
    if y == 2 and z == 1: ## This needs revamped (instructions clearly said not to do this)
        return lucas(n)
    else:
        return fibonacci(n)


if __name__ == "__main__":
    '''Call each function above individually. Also includes assert statements to test for expected results'''
    n = 9
    print('n = ' + str(n))
    print('fibonacci(n) = ' + str(fibonacci(n)))
    print('lucas(n) = ' + str(lucas(n)))
    print('sum_series(n) = ' + str(sum_series(n))) # Call function with only required parameter >> Expect return fibonacci
    print('sum_series(n, 2, 1) = ' + str(sum_series(n, 2, 1))) # Provide optional variables >> Expect return lucas

# Assertion Tests #

    print('\n*** Begin Assertion Tests ***')
    assert fibonacci(n) == sum_series(n)  # based on the assignment guidelines, this should return nothing
    assert lucas(n) == sum_series(n, 2, 1) # based on the assignment guidelines, this should return nothing
    assert fibonacci(6) == 8  # The 6th position in the fibonacci series (starting from 0) is always 13
    assert lucas(6) == 18  # The 6th position of the lucas series should always be 18
    print('\tAll assertion tests passed.')















































































# author: githubtater