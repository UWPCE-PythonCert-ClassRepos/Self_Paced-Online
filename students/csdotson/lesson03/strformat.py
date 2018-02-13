#!/usr/bin/env python3
# Lesson 3 - String Formatting Excercise

### Task 1 ############################################################
# String formatting the following Tuple using '.format'
a_tuple = (2, 123.4567, 10000, 12345.67)

Output = "file_{:03d}: {:3.2f}, {:.2e}, {:.2e}".format(*a_tuple)

print("*" * 5 + "Task 1" + "*" * 5)
print(Output + '\n')


### Task 2 ############################################################
# String formatting the following Tuple using named parameters
a_tuple = (2, 123.4567, 10000, 12345.67)

Output = "file_{file_num}: {float_num}, {sci_int}, {sci_float}".format(file_num = 1, float_num = float(2), sci_int = 3, sci_float = 4)

print("*" * 5 + "Task 2" + "*" * 5)
print(Output + '\n')


### Task 3 ############################################################
# Dynamically building up format strings

def formatter(in_tuple):
    l = len(in_tuple)
    form_string = "The {} numbers are: ".format(l) + ", ".join(["{}"] * l)
    return form_string.format(*in_tuple)

print("*" * 5 + "Task 3" + "*" * 5)
tup_1 = (1, 2, 3)
print("First tuple:", tup_1)
print("Formatted first tuple:", formatter(tup_1) + '\n')

tup_2 = (1, 2, 3, 4, 5)
print("Second tuple:", tup_2)
print("Formatted second tuple:", formatter(tup_2) + '\n')
