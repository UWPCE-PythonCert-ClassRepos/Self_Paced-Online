#!/usr/bin/env python3
# James Traub 04-04-18
# Lesson 3 - String Formatting Lab Exercise

# Series 1
tuple_elements = ( 2, 123.4567, 10000, 12345.67)

print('file_{0:03d}: {1:.2f}, {2:.2e}, {3:.2e}'.format(tuple_elements[0], tuple_elements[1], tuple_elements[2], tuple_elements[3]))
