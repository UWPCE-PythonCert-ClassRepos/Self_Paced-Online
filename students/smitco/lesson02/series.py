#lesson 02 series 
#step 1- print fibonacci value
def fibonacci(n):
    fib = []
    for num in range(n+1):
        if num == 0:
            fib.append(0)
        elif num == 1:
            fib.append(1)
        else:
            f = fib[num-1] + fib[num-2]
            fib.append(f)
    return(fib[n])   


#step 2- print lucas value
def lucas(n):
    luc = []
    for num in range(n+1):
        if num == 0:
            luc.append(2)
        elif num == 1:
            luc.append(1)
        else:
            l = luc[num-1] + luc[num-2]
            luc.append(l)
    return(luc[n])


#step 3= generalize the formula for fib and luc series
def sum_series(n, z=0, o=1):
    ser = []
    for num in range(n+1):
        if num == 0:
            ser.append(z)
        elif num == 1:
            ser.append(o)
        else:
            s = ser[num-1] + ser[num-2]
            ser.append(s)
    return(ser[n])


#using assert to check code
assert sum_series(15) == 610
assert sum_series(9) == 34
assert sum_series(12, 2, 1) == 322
assert sum_series(4, 2, 1) == 7