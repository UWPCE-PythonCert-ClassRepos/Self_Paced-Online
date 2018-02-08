######################STEP1#########################################
def fibonacci(n):
    """The first line (n = n - 1) ensures that we get the nth number in the series.
    For example fibonacci(1) should return 0. Without this line it would return
    the secoond element.
    I also built in a test so that only positive numbers can be used in the
    function.
    """
    if n<1:
            print("Please use number larger than 0")
    else:
        n = n - 1
        a, b = 0, 1
        while n > 0:
            a, b = b, a + b
            n -= 1
        return a

print("fibonacci(8): ",fibonacci(8))
######################STEP1#########################################

######################Lucas Numbers#########################################
def lucas(n):
    """The lucas numbers are very similar to fibonacci. The only difference is
    the first 2 numbers of the series, which are 2 for n = 0 and 1 for n = 1.
    The rest of the series is like for fibonacci numbers the sum of the 2
    previous numbers."""
    if n<1:
            print("Please use number larger than 0")
    else:
        n = n - 1
        a, b = 2, 1
        while n > 0:
            a, b = b, a + b
            n -= 1
        return a

print("lucas(8): ",lucas(8))
######################Lucas Numbers#########################################

######################Generalizing#########################################
def sum_series(n,x=0,y=1):
    """This function generalizes and allows to produce by default fibonacci
    numbers (by only entering a value for n). If you also specify the first
    and second value of the series, then this function can also produce
    other series like lucas (first value 2 and second value 1) or other."""
    if n<1:
            print("Please use number larger than 0")
    else:
        n = n - 1
        a, b = x, y
        while n > 0:
            a, b = b, a + b
            n -= 1
        return a

print("sum_series(8,2,1): " ,sum_series(8,2,1))
print("sum_series(8,0,1): " ,sum_series(8,0,1))
######################Generalizing#########################################

print("testing fibonacci:")
assert fibonacci(8) == 13, "fibonacci function generates wrong output"
print("testing lucas:")
assert lucas(8) == 29, "fibonacci function generates wrong output"
print("testing sum_series:")
assert sum_series(8) == fibonacci(8), "sum_series can produce fibonacci numbers"
