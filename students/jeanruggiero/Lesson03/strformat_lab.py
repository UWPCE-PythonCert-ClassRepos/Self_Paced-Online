#!/usr/bin/env python

##################################TASK 1#######################################
# Tuple containing info about the file
file_info = ( 2, 123.4567, 10000, 12345.67)

# Format string to format file_info
file_format = 'file_{:03d} :  {:.2f}, {:.2e}, {:.3G}'

# Apply format string to file_info and print results
file_disp = file_format.format(*file_info)
print(file_disp)

##################################TASK 1#######################################

file_info2 = {'name': 2, 'size': 123.4567, 'use': 10000, 'key': 12345.67}
file_disp2 = "file_{name} :  {size}, {use}, {key}".format(**file_info2)
print(file_disp2)
