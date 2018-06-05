# Series.py: implements Fibonacci Series Exercise for Lesson 2 Assignment

intro = '''UWPCE Python Programming: Lesson 2 Assignment
Fibonacci Series Exercise: fibonnaci and lucas functions to return nth value of
each series, generalized series function with three parameters
1. fib(n) - series starts with 0 and 1, returns nth value
2. lucas(n) - series starts with 2 and 1, returns nth value
3. sum_series(n, a, b) - optional arguments a and b default to 0 and 1, returns nth value
'''
print(intro)

def fib(n):
    if n < 1:
        print("Invalid argument")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def lucas(n):
    if n < 1:
        print("Invalid argument")
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

# def sum_series(n,a,b)
