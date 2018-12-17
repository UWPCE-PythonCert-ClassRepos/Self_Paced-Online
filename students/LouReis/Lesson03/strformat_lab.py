#!/usr/bin/env python3
# strformat_lab.py
# Coded by LouReis

# Task 1
# Write a format string that will take the following four element tuple:
#        ( 2, 123.4567, 10000, 12345.67)
#        and produce:
#        'file_002 :   123.46, 1.00e+04, 1.23e+04'

"file_{:0>3d}:  {:.2f}, {:.2e}, {:.2e}".format(2,123.4567, 10000, 12345.67)

# Task 2
# Using your results from Task One, repeat the exercise, but this time
# using an alternate type of format string (hint: think about alternative
# ways to use .format() (keywords anyone?), and also consider f-strings if
# you’ve not used them already).

sample = [2, 123.4567, 10000, 12345.67]
f"file_{sample[0]:0>3d}:  {sample[1]:.2f}, {sample[2]:.2e}, {sample[3]:.2e}"

# Task 3
"""
Rewrite task 1 to take an arbitrary number of values.
Hint: You can pass in a tuple of values to a function with a *.
The idea here is that you may have a tuple of three numbers, but might also have 4 or 5 or 2 or….
so you can dynamically build up the format string to accommodate the length of the tuple.
The string object has the format() method, so you can call it with a string that is bound
to a name, not just a string literal. For example:
So in the example above, how would you make a form_string that was the right length for an arbitrary tuple?
Put your code in a function that will return the final string like so:
def formatter(in_tuple):
    do_something_here_to_make_a_format_string
    return form_string.format(in_tuple)
"""

in_tuple = (1,2,3,4,5)
def formatter(in_tuple):
    num = str(len(in_tuple))
    form_string = "The " + num + " numbers are: "
    for x in range(0,len(in_tuple)):
        form_string = form_string + "{:d}, "
    form_string = form_string + "end."
    return form_string.format(*in_tuple)

formatter(in_tuple)
formatter([10,20,30,40,50,60,70,80,90,100])
