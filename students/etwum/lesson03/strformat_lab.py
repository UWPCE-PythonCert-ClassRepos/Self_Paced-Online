#!/usr/bin/env python3

# Task One

x = (2, 123.4567, 10000, 12345.67)

file = "file{0:03d}: {1:.2f}, {2:.2e}, {3:.2e}".format(x[0],x[1],x[2],x[3])
print(file)
print("----------------------------------------------------------------")

# Task Two

x1 = x[0]
x2 = x[1]
x3 = x[2]
x4 = x[3]

string = f"file{x1:03d}: {x2:.2f}, {x3:.2e}, {x4:.2e}"
print(string)
print("----------------------------------------------------------------")

# Task Three

def formatter(*tuple):
    # creates a string which dynamically prints a string based on the numbers passed to the function
    form_string = "the " + str(len(tuple)) + " numbers are " + ", ".join(["{}"]*len(tuple)).format(*tuple)
    return print(form_string)

formatter(1,2,3,4,5,6)
print("----------------------------------------------------------------")
# Task Four

y = ( 4, 30, 2017, 2, 27)

new_string = "{d:02d} {e} {c} {a:02d} {b}".format(a=y[0],b=y[1],c=y[2],d=y[3],e=y[4])

print(new_string)
print("----------------------------------------------------------------")

# Task Five

z = ['oranges', 1.3, 'lemons', 1.1]

y1 = z[0]
y2 = z[1]
y3 = z[2]
y4 = z[3]

# use f-string to format the strings
f_string = f"The weight of an {y1} is {y2} and the weight of a {y3} is {y4}"
print(f_string)

f_string2 = f"The weight of an {y1.upper()} is {y2*1.2} and the weight of a {y3.upper()} is {y4*1.2}"
print(f_string2)
print("----------------------------------------------------------------")
# Task Six

# print a table of several rows, each with a name, an age and a cost
list = [["name", "age", "cost"], ["Mike", "31", 999999.25],["Jordan", "23", 9999.99], ["Wayne", "25", 999],
        ["Brady", "100", 9.99]]

for x in list:
    print('{:<15}{:<5}{:<5}'.format(*x))
print("----------------------------------------------------------------")
# print 10 numbers in two rows of 5
print('{:<5}{:<5}{:<5}{:<5}{:<5}\n{:<5}{:<5}{:<5}{:<5}{:<5}'.format(1,2,3,4,5,6,7,8,9,10))