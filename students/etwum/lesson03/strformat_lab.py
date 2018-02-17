#!/usr/bin/env python3

# Task One

x = (2, 123.4567, 10000, 12345.67)

file = "file{0:03d}: {1:.2f}, {2:.2e}, {3:.2e}".format(x[0],x[1],x[2],x[3])
print(file)
