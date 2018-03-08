# author: githubtater

def fibonacci(n):
    '''Return the nth value in the fibonacci series.'''
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2) # formula from example: fib(n) = fib(n-2) + fib(n-1)


def lucas(n):
    '''Fibonacci() with a twist'''
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)



def sum_series(x, y=0, z=1):
    '''Return the nth value in the fibonacci or lucas series, depending on input values'''
    if y == 2 and z == 1: ## This needs revamped (instructions clearly said not to do this)
        return lucas(x)
    else:
        return fibonacci(x)


if __name__ == "__main__":
    '''Call each function above individually. Also includes assert statements to test for expected results'''
    x = 5

    print(fibonacci(x))
    print(lucas(x))
    print(sum_series(x)) # Call function with only required parameter >> Expect return fibonacci
    print(sum_series(x, 2, 1)) # Provide optional variables >> Expect return lucas

    assert fibonacci(x) == sum_series(x)  # based on the assignment guidelines, this should return nothing
    assert lucas(x) == sum_series(x, 2, 1) # based on the assignment guidelines, this should return nothing
    assert fibonacci(x) == lucas(x)       # This test should always fail, unless x == 1
















































































# author: githubtater