#!/usr/bin/env python3
# strformat_lab.py implements the Lesson 3 - STring Formatting Lab Exercise assignment from UWPCE Python Programming

intro = '''UWPCE Python Programming: Lesson 3 Assignment -- String Formatting Lab Exercises
'''
print(intro)

#Task 1
print("Task 1")
t = (2, 123.4567, 10000, 12345.67)    # starting tuple
print("Initial tuple: ", t)              # show starting tuple
# show formatted output -  should be 'file_002, 123.46, 1.00e+04, 1.23e+04'
print("Formatted tuple: 'file_{:0>3d}: {:.2f}, {:.2e}, {:.2e}'".format(t[0], t[1], t[2], t[3]))


#Task 2
print("Task 2")
t = (2, 123.4567, 10000, 12345.67)    # starting tuple
print("Initial tuple: ", t)              # show starting tuple
# show alternative formatted output -  should be 'file_002, 123.46, 1.00e+04, 1.23e+04'
print("Formatted tuple: 'file_{fname}: {fnum:.2f}, {enum:.2e}, {efloat:.2e}".format\
    (fname = str(t[0]).zfill(3),\
    fnum = t[1],\
    enum = t[2],\
    efloat = t[3]))

#Task 3
print("Task 3: dynamic formatter")
def formatter(in_tuple):
    fstring = ""
    for item in in_tuple:
        fstring = fstring + "{:d}"
        if item != len(in_tuple):
            fstring = fstring + ","
    return "The {} numbers are: ".format(len(in_tuple)) + fstring.format(*in_tuple)
# Test formatter function
result = formatter((1,2,3,4,5,6,7,8,9))
print(result)

#Task 4
print("Task 4")
t = ( 4, 30, 2017, 2, 27)
print("'{3:0>2d} {4} {2} {0:0>2d} {1}'".format(*t))

#Task 5
print("Task 5")
l = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {(l[0])[:-1]} is {l[1]} and the weight of a {(l[2])[:-1]} is {l[3]}")
print(f"The weight of an {(l[0])[:-1].capitalize()} is {l[1]*1.2} and the weight of a {(l[2])[:-1].capitalize()} is {l[3]*1.2}")


#Task 6
print("Task 6")
table_data = ('Sam', 45,1030, 'Nancy', 50, 25069, 'Andrew', 35, 503, 'Margaret', 48, 2045, 'Brian',  23, 750)
while table_data:
    print("{:<10}{:>3d}    ${:>7,d}".format(*table_data))
    table_data = table_data[3:]


print("Task Extra")
t = (1,2,3,4,5,6,7,8,9,10)
print(("{:>5d}" * len(t)).format(*t))
