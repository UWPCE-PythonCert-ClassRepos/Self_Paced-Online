#!/usr/bin/env python3

# task 1
tuple1 = (2, 123.4567, 10000, 12345.67)

# first value
#print("the number is {:03.0f}".format(tuple1[0]))
print("the number is {:0>3d}".format(tuple1[0]))

# second value
#print("the number is {:06.2f}".format(tuple1[1]))
print("the number is {:.2f}".format(tuple1[1]))


# third value
print("the number is {:.2e}".format(tuple1[2]))


# fourth value
print("the number is {:.3e}".format(tuple1[3]))
