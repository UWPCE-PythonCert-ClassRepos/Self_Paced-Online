#!/usr/bin/env python3
# James Traub 04-04-18
# Lesson 3 - String Formatting Lab Exercise

# Task 1
# tuple_elements = ( 2, 123.4567, 10000, 12345.67)
# print('file_{0:03d}: {1:.2f}, {2:.2e}, {3:.2e}'.format(tuple_elements[0], tuple_elements[1], tuple_elements[2], tuple_elements[3]))

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


""" Task 4 - Given a 5 element tuple: ( 4, 30, 2017, 2, 27)
    use string formatting to print: '02 27 2017 04 30' """
# cinco = ( 4, 30, 2017, 2, 27)
# print("{c3:0>2d} {c4:0>2d} {c2:0>2d} {c0:0>2d} {c1:0>2d}".format(c0=cinco[0], c1=cinco[1], c2=cinco[2], c3=cinco[3], c4=cinco[4]))


""" Task 5 - Given a 4 element tuple: ['oranges', 1.3, 'lemons', 1.1]
    use string formatting to print: The weight of an orange is 1.3 and the weight of a lemon is 1.1 """
# orange = ("orange", 1.3)
# lemon = ("lemon", 1.1)
# print(f"The weight of an {orange[0]} is {orange[1]} and the weight of a {lemon[0]} is {lemon[1]}")
# print(f"The weight of an {orange[0].upper()} is {orange[1] * 1.2} and the weight of a {lemon[0].upper()} is {lemon[1] * 1.2}")


""" Task 6 - 