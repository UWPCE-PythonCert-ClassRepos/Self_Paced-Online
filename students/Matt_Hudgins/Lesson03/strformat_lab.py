#!/usr/bin/env python3

# chmod +x strformat_lab.py needs to be performed before executable

'''
    File Name: strformat_lab.py
    Author: Matt Hudgins
    Date created: 5/5/18
    Date last modified: 5/5/18
    Python Version 3.6.4
'''


# Task One
# Formating string using f-strings


print("Starting Task 1")
new_tuple = (2, 123.4567, 10000, 12345.67)  # Defining the touple


def task_one():
    print(f"file_{new_tuple[0]:03d}: {new_tuple[1]:.2f}, {new_tuple[2]:.2e}, {new_tuple[3]:.2e}")


task_one()

# Task Two
# This is for formatting a sting using the .format

print("Starting Task 2")


def task_two():
    print("file_{0:03d}: {1:.2f}, {2:.2e}, {3:.2e}".format(new_tuple[0], new_tuple[1], new_tuple[2], new_tuple[3]))


task_two()


# Task Three
# Dynamically building up format strings

print("Starting Task 3")


def formatter(*tuple):
    tuple_length = len(tuple)
    format_string = '{:d},' * (tuple_length - 1) + '{:d}'
    print("There are {} items, and they are: ".format(tuple_length) + format_string.format(*tuple))


formatter(2, 3, 4, 5, 6, 7)  # This is just a test of the function


# Task Four
# Another test with a five element tuple:

print("Starting Task 4")
print("Let's reformat this 5 element tuple! 4,30,2017,2,27")

data = (4, 30, 2017, 2, 27)


def task_four(data):
    reformat = "{0:02d} {1:d} {2:d} {3:02d} {4:d}"
    print(reformat.format(data[3], data[4], data[2], data[0],
        data[1]))


task_four(data)

# Task Five

print("Starting Task 5")

fruits = ["orange", 1.3, "lemon", 1.1]

string = f"The weight of an {fruits[0]} is {fruits[1]} and the weight of a {fruits[2]} is {fruits[3]}"
string_updated = f"The weight of an {fruits[0].upper()} is {fruits[1]*1.2} and the weight of a {fruits[2].upper()} is {fruits[3]*1.2}"

print("This is the orginal string:", string)
print("This is the updated string:", string_updated)

# Task Six

print("Starting Task 6")

new_data = [("Name", "Age", "Cost"), ("Matt", "30", "10,000"),
            ("Nilou", "27", "20,000")]
for row in new_data:
    print("{:^10}{:^12}${:12}".format(*row))