#!/usr/bin/env python3
"""
File Name: strformat_lab.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 4/5/2018
Python Version: 3.6.4
"""

a, b, c, d = (2, 123.4567, 10000, 12345.67)
# Task 1
"file_{:03d}: {:.2f}, {:.2e}, {:.2e}".format(a, b, c, d)
print("\n")


# Task 2
f"file_{a:03d}: {b:.2f}, {c:.2e}, {d:.2e}"
print("\n")


# Task 3
t = (4, 30, 2017, 2, 27)


def formatter(t):
    form_string = "the {:d} numbers are: " + "{:d}, " * (len(t) - 1) + "{:d}"
    return form_string.format(len(t), *t)


print(formatter(t))
print("\n")


# Task 4
t = (4, 30, 2017, 2, 27)
f_string = "{:02d} " * len(t)
print(f_string.format(t[3], t[4], t[2], t[0], t[1]))
print("\n")

# Task 5
fruit1, weight1, fruit2, weight2 = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {fruit1[:-1]} is {weight1} and the weight of a {fruit2[:-1]} is {weight2}")
print(f"The weight of an {fruit1[:-1].upper()} is {weight1 * 1.2} and the weight of a {fruit2[:-1].upper()} is {weight2 * 1.2}")
print("\n")


# Task 6
rows = (('VW Rabbit', 23, 800.53), ('Buick', 8, 15012.20), ('Ferrari', 5, 100000))
for row in rows:
    print("{:<10} {:>10} {:>10.2f}".format(*row))
print("\n")

numbers = (1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009)
print(("{:>5d}" * len(numbers)).format(*numbers))
