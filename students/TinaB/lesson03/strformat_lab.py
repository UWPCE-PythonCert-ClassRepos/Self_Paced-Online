#!/usr/bin/env python3

# Task One ------------------
"""Write a format string that will take the following four element tuple:
( 2, 123.4567, 10000, 12345.67) and produce: 'file_002 :   123.46, 1.00e+04, 1.23e+04'
So you need to find a string formatting operator that will “pad” the number with zeros for you.
The second element is a floating point number. You should display it with 2 decimal places shown.
The third value is an integer, but could be any number. You should display it in scientific notation, with 2 decimal places shown.
The fourth value is a float with a lot of digits – display it in scientific notation with 3 significant figures.
"""
print("Task One:")
#output to match
print("file_002 :   123.46, 1.00e+04, 1.23e+04")
#print("file_{:03d} :   {:06.2f}, {:.2E}, {:.2E}".format(2, 123.4567, 10000, 12345.67))
print("file_{:0>03} :   {:06.2f}, {:.2E}, {:.2E}".format(
    2, 123.4567, 10000, 12345.67))

# Task Two ------------------
"""Using your results from Task One, repeat the exercise, but this time using an alternate type of format string
(hint: think about alternative ways to use .format() (keywords anyone?), and also consider f-strings if you’ve not used them already)."""
print("Task Two:")
#output to match
input_tuple = (2, 123.4567, 10000, 12345.67)

print(f"file_{input_tuple[0]:0>03} :   {input_tuple[1]:06.2f}, {input_tuple[2]:.2E}, {input_tuple[3]:.2E}")

# Task Three ----------------------
"""
Dynamically Building up Format Strings
Rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
to take an arbitrary number of values.
 """
print("Task Three:")

def formatter(in_tuple):
    """ function to print input tuple """
    formatted_string = "the numbers are: "
    form_string = "{:d}, " * (len(in_tuple)-1) + "{:d}"
    formatted_string = "the " + \
        str(len(in_tuple)) + " numbers are: " + form_string
    return formatted_string.format(*in_tuple)


print(formatter((2, 3, 5, 7, 9)))

# Task Four ----------------------
"""
Given a 5 element tuple: ( 4, 30, 2017, 2, 27)
use string formating to print: '02 27 2017 04 30'
Hint: use index numbers to specify positions."""

print("Task Four:")
input_tuple = (4, 30, 2017, 2, 27)
# test print to match:
print("02 27 2017 04 30")
print("{:02} {:02} {} {:02} {:02}".format(
    input_tuple[3], input_tuple[4], input_tuple[2], input_tuple[0], input_tuple[1]))
print(f"{input_tuple[3]:02} {input_tuple[4]:02} {input_tuple[2]} {input_tuple[0]:02} {input_tuple[1]:02}")

# Task Five -----------------------
"""
Given the following four element list:['oranges', 1.3, 'lemons', 1.1] 
Write an f-string that will display: The weight of an orange is 1.3 and the weight of a lemon is 1.1
Now see if you can change the f-string so that it displays the names of the fruit in upper case, 
and the weight 20% higher.
"""
print("Task Five:")
element_list = ['oranges', 1.3, 'lemons', 1.1]
# String to match:
print("The weight of an orange is 1.3 and the weight of a lemon is 1.1")
# part one match test string
print(f"The weight of an {element_list[0][:-1]} is {element_list[1]} and the weight of a {element_list[2][:-1]} is {element_list[3]}")
# part two - print fruit upper case
print(f"The weight of an {element_list[0][:-1].upper()} is {element_list[1]} and the weight of a {element_list[2][:-1].upper()} is {element_list[3]}")
# part three - print weight 20% higher.
print(f"The weight of an {element_list[0][:-1].upper()} is {element_list[1]*1.20} and the weight of a {element_list[2][:-1].upper()} is {element_list[3]*1.20}")

# Task Six -----------------------
"""
Write some Python code to print a table of several rows, each with a name, an age and a cost. 
Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
"""
print("Task Six:")

table_list = [('Carina', 27, 15, 156.25), ('Timothy', 2, 127.63),
              ('Paul', 12, 1758.17), ('Jeffery', 65, 199), ('Ruben', 107, 165, 248.25),
              ('Tristan', 85, 8, 156.92), ('Shannon', 44, 556.2), ('Elizabeth', 15, 166, 156.25),
              ('Tom', 39, 825), ('Tricia', 93, 156), ('Allegra', 68, 962.30)]

# print table header:
print('{:<10}{:<6}{:>12}'.format('Name', 'Age', 'Cost'))
# table
for item in table_list:
    print('{:<12s}{:<6}{:>10,.2f}'.format(*item))

# task 6 part two
"""Create consecutive range of numbers in 5-character columns"""
input_tuple = range(10)
print(("{:5}"*10).format(*input_tuple))
