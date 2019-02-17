#Compute the Fibonacci and Lucas Series
#Jason Virtue 1/8/2019
#Lesson 2
#Python Self-Course @ UW

#Compute Fibonacci Series
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10))


#Compute Lucas Series
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
    
print(lucas(6))

#Compute Generic series to compute Fibonacci or Lucas series
def sum_series(n, y=0, z=1):
    if n == 0:
        return y
    elif n==1:
        return z
    else:
        return sum_series(n-1,y,z) + sum_series(n-2,y,z)

print(sum_series(7, y = 2, z = 1))
print(sum_series(7))

#Test out Fib series to see if it works
assert fibonacci(10) == 55
assert fibonacci(7) == 13

#Test out Lucas series to see if it works
assert lucas(6) == 18
assert lucas(7) == 29

#Test out sum_series to see if it works
assert sum_series(5) == 5
assert sum_series(7) == 13

#Test out sum_series with optional parameters
assert sum_series(5,2,1) == 11
assert sum_series(7,2,1) == 29

