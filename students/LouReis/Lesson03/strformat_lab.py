#!/usr/bin/env python3
# strformat_lab.py
# Coded by LouReis

# Task 1
# Write a format string that will take the following four element tuple:
#        ( 2, 123.4567, 10000, 12345.67)
#        and produce:
#        'file_002 :   123.46, 1.00e+04, 1.23e+04'
print("Start of Task #1")
"file_{:0>3d}:  {:.2f}, {:.2e}, {:.2e}".format(2,123.4567, 10000, 12345.67)
print("End of Task #1")
print()
print("Start of Task #2")
# Task 2
# Using your results from Task One, repeat the exercise, but this time
# using an alternate type of format string (hint: think about alternative
# ways to use .format() (keywords anyone?), and also consider f-strings if
# you’ve not used them already).

sample = [2, 123.4567, 10000, 12345.67]
f"file_{sample[0]:0>3d}:  {sample[1]:.2f}, {sample[2]:.2e}, {sample[3]:.2e}"

print("End of Task #2")
print()
print("Start of Task #3")
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
print()
formatter([10,20,30,40,50,60,70,80,90,100])
print("End of Task #3")
print()
print("Start of Task #4")

# Task 4
"""
    Given a 5 element tuple:
        ( 4, 30, 2017, 2, 27)
        use string formating to print:
        '02 27 2017 04 30'
Hint: use index numbers to specify positions.
"""

nums = (4,30,2017,2,27)
"{:0>2d} {} {} {:0>2d} {}".format(nums[3],nums[4],nums[2],nums[0],nums[1])

print("End of Task 4")
print()
print("Start of Task 5")

# Task 5
"""
    Given the following four element list:
        ['oranges', 1.3, 'lemons', 1.1]
    Write an f-string that will display:
        The weight of an orange is 1.3 and the weight of a lemon is 1.1
    Now see if you can change the f-string so that it displays the names of the
    fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
"""
fruity = ['oranges', 1.3, 'lemons', 1.1]
f"The weight of an {fruity[0].rstrip('s')} is {fruity[1]} and the weight of a {fruity[2].rstrip('s')} is {fruity[3]}"
f"The weight of an {fruity[0].upper()[0:-1]} is {fruity[1]*1.2} and the weight of a {fruity[2].upper()[0:-1]} is {fruity[3]*1.2}"

print("End of Task #5")
print()
print("Start of Task #6")

# Task 6
"""
    Write some Python code to print a table of several rows, each with a name, an age and a cost.
    Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
    And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly
    print the tuple in columns that are 5 charaters wide? It’s easily done on one short line!
"""
# Print a table of rows with aligned columns.

furniture = ['Antique Name', 'Age', 'Price', 'Chair', 125, '$195.50', 'Table', 210, '$1,995.00', 'Desk', 95, '$85.00', 'Lamp', 65, '$9.25']
items=len(furniture)
items=int(items/3)
print("There are", items, "rows.")
print()
print('{:20}{:>5}{:>20}'.format(furniture[0], furniture[1], furniture[2]))
print('{:20}{:>5}{:>20}'.format(furniture[3], furniture[4], furniture[5]))
print('{:20}{:>5}{:>20}'.format(furniture[6], furniture[7], furniture[8]))
print('{:20}{:>5}{:>20}'.format(furniture[9], furniture[10], furniture[11]))
print('{:20}{:>5}{:>20}'.format(furniture[12], furniture[13], furniture[14]))

numbers=[1,2,3,4,5,6,7,8,9,10]
print('{:5}{:5}{:5}'.format(*numbers))
