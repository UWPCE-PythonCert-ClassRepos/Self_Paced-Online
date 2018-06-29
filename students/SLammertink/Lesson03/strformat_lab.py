#! /usr/bin/env python3
# UW Self paced Lesson 03 string lambda

# Task 1
''' Write a format string that will take the following four element tuple:
( 2, 123.4567, 10000, 12345.67)
and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04' '''

StrList = (2, 123.4567, 10000, 12345.67)

def Task1():
    print(f"file_{StrList[0]:03d} :  {StrList[1]:.2f}, {StrList[2]:.2e}, {StrList[3]:.2e}")


# task 2

'''Using your results from Task One, repeat the exercise, but this time using
an alternate type of format string (hint: think about alternative ways to use .format()
(keywords anyone?), and also consider f-strings if you’ve not used them already).
'''


def Task2():
    print("file_{0:03d} :  {1:.2f}, {2:.2e}, {3:.2e}".format(StrList[0], StrList[1], StrList[2], StrList[3]))
    print("file_%03d :  %.2f, %.2e, %.2e" % StrList)

# Task 3

''' Rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) to take an arbitrary number of values.'''

def formatter(in_tuple):
    formatter_string = "the " + str(len(in_tuple)) + " numbers are " + ", ".join(["{}"]*len(in_tuple)).format(*in_tuple)
    print(formatter_string)

# Task 4

'''Given a 5 element tuple: ( 4, 30, 2017, 2, 27)
use string formating to print: '02 27 2017 04 30' '''

five_tuple = ( 4, 30, 2017, 2, 27)

def TaskFour(five_tuple):
    reformat = "{0:02d} {1:d} {2:d} {3:02d} {4:d}"
    print(reformat.format(five_tuple[3], five_tu
                           uit_list = ['oranges', 1.3, 'lemons', 1.1]

# Task 5


print(f'The weight of an {str(fruit_list[0])[:-1]} is {fruit_list[1]} and the weight of a {str(fruit_list[2])[:-1]} is {fruit_list[3]}')

# Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher

print(f'The weight of an {str(fruit_list[0])[:-1].upper()} is {fruit_list[1] * 1.2} and the weight of a {str(fruit_list[2].upper())[:-1]} is {fruit_list[3] * 1.2}')

# Task 6

# Write some Python code to print a table of several rows, each with a name, an age and a cost. Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.


rows = [('Name', 'Age', 'Cost'),('Seb', 50, 200),('Kim', 47, 5000), ('Mike', 25, 375.25)]
for row in rows:
    print("{:^10}{:^10}{:^10}".format(*row))

