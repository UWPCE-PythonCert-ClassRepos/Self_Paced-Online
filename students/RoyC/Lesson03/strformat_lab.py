#!/usr/bin/env python3
# Lesson 03, String formatting lab

# Task One
in_tuple = ( 2, 123.4567, 10000, 12345.67)
print("file_{:03d}: {:.2f}, {:.2e}, {:.2e}".format(*in_tuple))

# Task Two
print(f"file_{in_tuple[0]:03}: {in_tuple[1]:.2f}, {in_tuple[2]:.2e}, {in_tuple[3]:.2e}")

# Task Three
def formatter(in_tuple):
    """
    Return formatted string with the integer values in the given tuple
    """
    out_string = "The {:d} numbers are " + ("{:d},"*len(in_tuple))
    # print out formatted string, minus last extranneous comma
    return out_string.format(len(in_tuple), *in_tuple)[:-1]
    
print(formatter((1, 4, 2, 11, 9)))
print(formatter((5, 1, 0)))
print(formatter((3, 6, 9, 12, 15, 18)))

# Task Four
it = ( 4, 30, 2017, 2, 27)
print(f"{it[3]:02} {it[4]:02} {it[2]:04} {it[0]:02} {it[1]:02}")
