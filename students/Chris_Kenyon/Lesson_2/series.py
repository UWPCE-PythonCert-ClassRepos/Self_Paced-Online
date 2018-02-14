# Lesson 2, Activity 3: Series

# random module for use in testing
import random


def fibonacci(n):
    """Create a sum series with initial values 0 and 1 to create a
    series where each value is the sum of the prior two values"""
    if n > 0:
        # create array of zeros with size n
        fibser = [0] * n
        # set initial values
        fibser[0] = 0
        if n > 1:
            fibser[1] = 1
        # create full fibonacci sequence
        for i in range(2, n):
            fibser[i] = fibser[i-2] + fibser[i-1]
        # print specified nth value (n-1 due to index starting at 0)
        return(fibser[n-1])
    else:
        print("Please select an integer greater than 1")


def lucas(n):
    """Create a sum series with initial values 2 and 1 to create a
    series where each value is the sum of the prior two values"""
    if n > 0:
        # create array of zeros with size n
        lucser = [0] * n
        # set initial values
        lucser[0] = 2
        if n > 1:
            lucser[1] = 1
        # create full fibonacci sequence
        for i in range(2, n):
            lucser[i] = lucser[i-2] + lucser[i-1]
        # print specified nth value (n-1 due to index starting at 0)
        return(lucser[n-1])
    else:
        print("Please select an integer greater than 1")


def sum_series(n, x=0, y=1):
    """Create a sum series with initial values x and y to create a
    series where each value is the sum of the prior two values"""
    if n > 0:
        # create array of zeros with size n
        sumser = [0] * n
        # set initial values
        sumser[0] = x
        if n > 1:
            sumser[1] = y
        # create full fibonacci sequence
        for i in range(2, n):
            sumser[i] = sumser[i-2] + sumser[i-1]
        # print specified nth value (n-1 due to index starting at 0)
        return(sumser[n-1])
    else:
        print("Please select an integer greater than 1")


# testing fibonacci
assert (fibonacci(1) == 0), "fibonacci function failed 1st test"
assert (fibonacci(2) == 1), "fibonacci function failed 2nd test"
assert (fibonacci(10) == 34), "fibonacci function failed 3rd test"
# testing lucas
assert (lucas(1) == 2), "lucas function failed 1st test"
assert (lucas(2) == 1), "lucas function failed 2nd test"
assert (lucas(10) == 76), "lucas function failed 3rd test"

# random integer for testing
testnum = random.randint(1, 16)
# testing sum series
assert (sum_series(testnum, 0, 1) == fibonacci(testnum)),\
    "sum_series function failed fibonacci test"
assert (sum_series(testnum, 2, 1) == lucas(testnum)),\
    "sum_series function failed lucas test"
assert (sum_series(testnum) == fibonacci(testnum)),\
    "sum_series function failed default test"
assert (sum_series(10, 3, 4) == 199),\
    "sum_series function failed specific test"
