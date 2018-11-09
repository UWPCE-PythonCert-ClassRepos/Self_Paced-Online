#!/usr/bin/env python3

#Take this tuple ( 2, 123.4567, 10000, 12345.67)
#and produce 'file_002 :   123.46, 1.00e+04, 1.23e+04'

elements=(( 2, 123.4567, 10000, 12345.67)
#print('file_{0:03d}: {1:.2f}, {2:.2e}, {3:.2e}'.format(elements[0], elements[1], elements[2], elements[3]))

print('file_{:0>3d}: {:.2f}, {:.2e}, {:.2e}'.format(2, 123.4567, 10000, 12345.67))

