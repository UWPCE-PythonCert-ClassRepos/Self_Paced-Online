"""I started by checking to see if n equals 0 or 1, knowing that these values would simply return 0 and 1, since the
numbers are basedon summing the two previous values. There would be no two previous values for 0 and 1.
Then I used the recursion logic provided to us in the lesson that sums two less and 1 less than the n value. """

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(6))

"""This code is very similary to the fibonacci sequence with the only change being that if n is 0, n now equals 2."""

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)

print(lucas(4))

"""I added the optional parameters to this function, with x representing the first number in the sequence and y 
representing the second number in the sequence. The only changes to the code are that if n is 0 or n is 1, the code
now returns the value of the optional parameters rather than a hard-coded value of 2,1 or 0,1."""
def sum_series(n, x=0, y=1):
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return sum_series(n - 2) + sum_series(n - 1)

print(sum_series(4))

"""These tests are using assert to ensure that the functions are providing the desired outcome. """

assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert lucas(0) == 2
assert lucas(3) == 4
assert sum_series(4) == 3
assert sum_series(5) == 5