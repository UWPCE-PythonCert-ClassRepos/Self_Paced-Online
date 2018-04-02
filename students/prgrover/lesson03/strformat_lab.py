#!/usr/bin/env python3

#Task 1
"""
Write a format string that will take the following four element tuple:

( 2, 123.4567, 10000, 12345.67)

and produce:

'file_002 :   123.46, 1.00e+04, 1.23e+04'
"""
task_1 = (2, 123.4567, 10000, 12345.67)

print("file_{:0>3d} :   {:.2f}, {:.2e}, {:.2e}".format(task_1[0], task_1[1], task_1[2], task_1[3]))



#Task 2
"""
Using your results from Task One, repeat the exercise, but this time using an alternate type of format string.
"""
print (f"file_{task_1[0]:0>3d} :   {task_1[1]:.2f}, {task_1[2]:.2e}, {task_1[3]:.2e}")



#Task 3
"""
Rewrite:
"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)

to take an arbitrary number of values.

Args:
seq: Tuple with an arbitraty number of values. Required.
"""
task_3 = (3, 10, 23, 32, 42)

def formatter(seq):
    l = len(seq)
    return (("The {} numbers are: " + ", ".join(["{}"] * l)).format(l, *seq))

print(formatter(task_3))



#Task 4
"""
Given a 5 element tuple:

( 4, 30, 2017, 2, 27)

use string formating to print:

'02 27 2017 04 30'
"""
task_4 = ( 4, 30, 2017, 2, 27)

print("{:0>2d} {:d} {:d} {:0>2d} {:d}".format(task_4[3], task_4[4], task_4[2], task_4[0], task_4[1]))



#Task 5
"""
Given the following four element list:

['oranges', 1.3, 'lemons', 1.1]

Write an f-string that will display:

The weight of an orange is 1.3 and the weight of a lemon is 1.1
"""

task_5 = ['oranges', 1.3, 'lemons', 1.1]

print (f"The weight of an {task_5[0][:-1]} is {task_5[1]} and the weight of a {task_5[2][:-1]} is {task_5[3]}")
print (f"The weight of an {task_5[0][:-1]} is {task_5[1] * 1.2} and the weight of a {task_5[2][:-1]} is {task_5[3] * 1.2}")



#Task 6
"""
Write some Python code to print a table of several rows, each with a name, an age and a cost. Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.

And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple in columns that are 5 charaters wide? It’s easily done on one short line!
"""
cars = [('Honda', '2000', 999.00), ('Toyota', '2018', 30000.23), ('Acura', '2008', 9995.99), ('Infinity', '2015', 23000.00)]

for car in cars:
    print("{:10} {:10} ${:9.2f}".format(*car))

task_6 = (0,1,2,3,4,5,6,7,8,9)
print (("{:5d}" * 10).format(*task_6))