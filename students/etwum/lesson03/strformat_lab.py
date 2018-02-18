#!/usr/bin/env python3

# Task One

x = (2, 123.4567, 10000, 12345.67)

file = "file{0:03d}: {1:.2f}, {2:.2e}, {3:.2e}".format(x[0],x[1],x[2],x[3])
print(file)


# Task Two

x1 = x[0]
x2 = x[1]
x3 = x[2]
x4 = x[3]

string = f"file{x1:03d}: {x2:.2f}, {x3:.2e}, {x4:.2e}"
print(string)


# Task Three

def formatter(*tuple):

    form_string = "the " + str(len(tuple)) + " numbers are " + ", ".join(["{}"]*len(tuple)).format(*tuple)
    return print(form_string)

formatter(1,2,3,4,5,6)

# Task Four

y = ( 4, 30, 2017, 2, 27)

new_string = "{d:02d} {e} {c} {a:02d} {b}".format(a=y[0],b=y[1],c=y[2],d=y[3],e=y[4])

print(new_string)

# Task Five