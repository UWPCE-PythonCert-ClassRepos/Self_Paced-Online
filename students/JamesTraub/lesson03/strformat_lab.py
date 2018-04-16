#!/usr/bin/env python3
# James Traub 04-04-18
# Lesson 3 - String Formatting Lab Exercise

# Task 1
tuple_elements = ( 2, 123.4567, 10000, 12345.67)
print('file_{0:03d}: {1:.2f}, {2:.2e}, {3:.2e}'.format(tuple_elements[0], tuple_elements[1], tuple_elements[2], tuple_elements[3]))

# Task 2
# te1 = tuple_elements[0]
# te2 = tuple_elements[1]
# te3 = tuple_elements[2]
# te4 = tuple_elements[3]

#print(f"file{te1:03d}: {te2:.2f}, {te3:.2e}, {te4:.2e}")


# Task 3 - Rewrite the following: 
# "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
# to allow it take an arbitrary number of values.

# def arb_val(*tuple):
#     # creates a string which dynamically prints a string based on the numbers passed to the function
#     new_string = "the " + str(len(tuple)) + " numbers are " + ", ".join(["{}"]*len(tuple)).format(*tuple)
#     print(new_string)

# arb_val(1,2,3,4,5)



# Task 4 - Given a 5 element tuple: ( 4, 30, 2017, 2, 27)
#          use string formating to print: '02 27 2017 04 30'